#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:47:27 2018

@author: drugo
"""
import pandas as pd

"""
Skiprows va messo uguale al numero di riga dove si trova 'Type,Date,Double...Double'.
 Generalmente skiprows = 6 per le intestazioni di Oms di 8 righe
"""
Variabile = 'PRP'
df= pd.read_csv('PRP.csv',sep=',',skiprows=6,low_memory=False)

df=df.set_index('yyyy-MM-dd HH:mm')
df = df.iloc[:,1:]
[m,n]=df.shape
for indice in range(0,n):
    dfColonna = df.iloc[:,indice]
    indiceplusone = indice+1
    nomeFile=Variabile+'_'+str(indiceplusone)+'.csv'
    dfColonna.to_csv(nomeFile, sep=',', header=False, encoding='utf-8')
    
    riga = "@T,table\n@H,timestamp,value_"+str(indiceplusone)+"\nID,,"+str(indiceplusone)+"\nType,Date,Double\nFormat,yyyy-MM-dd HH:mm\n"
    with file(nomeFile, 'r') as original: data = original.read()
    with file(nomeFile, 'w') as modified: 
        modified.write(riga + data)
        
        
        
    