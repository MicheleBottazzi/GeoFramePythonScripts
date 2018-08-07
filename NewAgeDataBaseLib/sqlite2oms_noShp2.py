#!/usr/bin/python2

import pandas as pd
from pyspatialite import dbapi2 as db
from mylib import *
#import matplotlib.pyplot as plt
import csv

##### Configuration ####################################################
## percorso al DB
DBpath='/home/drugo/Downloads/NewAgeDB.sqlite'

## maschera di bacino da caricare
mask="a_meledrio"

## buffer dalla maschera di bacino [m]
buff ="50000"

# variable meteo: Precipitazione 2, Temperatura 6, Umidita Relativa 8, Radiazione 13, Velocita Vento 7
#var=['TA','RH','PREC','RAD']
#var=['PREC','TA','RAD','RH']
var=['FLOW','PRP','PRES','TA','WIND','RH','RAD']
#var=['PRES','WIND','RH','RAD']

## periodo
t_start="1994-01-01 00:00:00"
t_end="2008-12-31 23:00:00"
# timestep
#tstep=60
prj_name = ""
prj_path = "/home/drugo/Desktop/"

########################################################################
# creating/connecting the test_db
conn = db.connect(DBpath)
cur = conn.cursor()

pm_ids=[]
#dict = {'PREC':'2', 'TA':'6', 'RH':'8', 'RAD':'13', 'HS':'10'}

dict = {'FLOW':'0','PRP':'2','PRES':'4','TA':'6','WIND':'7', 'RH':'8', 'RAD':'13'}
for v in var:
	print "############ ", v, " ##############"

	# selezione punti di monitoraggio
	q_pm="SELECT p.id FROM " + mask + " a, punti_monitoraggio p \
	WHERE ST_Intersects(a.geom, ST_Buffer(p.the_geom," + buff + ")) \
	AND p.tipologia_nodi_id IN (0,2,4,6,7,8,13)"
#AND p.tipologia_nodi_id IN (2,3,6,7,15,17)"

#	AND p.tipologia_nodi_id IN (2,7,15,17,18)"
	
	# selezione metadati
	q_meta="SELECT m.punti_monitoraggio_id, group_concat(m.id) FROM metadati m \
	WHERE m.tipologia_serie_temporali_id=" + dict[v] + " \
	AND m.punti_monitoraggio_id IN (" + q_pm + ") \
	AND m.intervallo <= 60 \
	GROUP BY m.punti_monitoraggio_id"
	
	#print q_meta
	out_query = cur.execute(q_meta)
	
	func='avg'
	i=0
	for row in out_query:
		pm_id = str(row[0])
		m_id = str(row[1])
		m2=str(row[1]).split(',')
		if v == 'PREC':
			func='sum'
			if len(m2)>1:
				m_id=str(m2[0])
		print "------------------- pm_id=", pm_id, " - m_id=", m_id ," -------------------"
		q_data="SELECT strftime('%Y-%m-%d %H', s.dataora / 1000, 'unixepoch') || ':00' as dataora,\
		round("+ func +"(s.valore),1) as val_" + pm_id + " \
		FROM serie_temporali s, metadati m  \
		WHERE s.metadati_id IN (" + m_id + ") \
		AND s.dataora>=strftime('%s','" + t_start + "')*1000 \
		AND s.dataora<strftime('%s','" + t_end+ "')*1000 \
		AND s.metadati_id=m.id \
		GROUP BY m.punti_monitoraggio_id, strftime('%Y-%m-%d %H', s.dataora / 1000, 'unixepoch')"
		tmp_df = pd.read_sql_query(q_data, conn, index_col='dataora')
		tmp_df.index = pd.DatetimeIndex(tmp_df.index)
		if len(tmp_df) < 1: continue
		pm_ids.append(pm_id) # tengo in memoria i punti con dati meteo
		if i == 0: 
			df=tmp_df
		else:
			df = pd.concat([df, tmp_df], axis=1)
		i=i+1

	#print df
	print "trovate ", i, " stazioni con dati nel periodo!"	
	if i==0: continue

	
#	# write CSV
	writeOMS(df,prj_path + "OMSdf_" + v + ".csv")


##### creazione file csv con info stazioni meteo utilizzate
q_shp="SELECT pm_id ID, nome, quota, geom \
FROM view_sensori \
WHERE pm_id IN (" + ', '.join(pm_ids) + ") \
GROUP BY pm_id"
#print ', '.join(pm_ids)
ms_df = pd.read_sql_query(q_shp, conn)

# write CSV
ms_df.to_csv(prj_path + "Meteo" + prj_name + ".csv", sep=",", na_rep="-9999",encoding='utf8',index=False)




