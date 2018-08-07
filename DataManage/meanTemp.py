#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:51:45 2018

@author: drugo
"""

import pandas as pd
import numpy as np

"""
Skiprows va messo uguale al numero di riga dove si trova 'Type,Date,Double...Double'.
 Generalmente skiprows = 6 per le intestazioni di Oms di 8 righe
"""
dfTA= pd.read_csv('OMSdf_TA.csv',sep=',',skiprows=2,low_memory=False)
dfPRP= pd.read_csv('OMSdf_PRP.csv',sep=',',skiprows=2,low_memory=False)
dfFLOW= pd.read_csv('OMSdf_FLOW.csv',sep=',',skiprows=2,low_memory=False)
dfRAD= pd.read_csv('OMSdf_RAD.csv',sep=',',skiprows=2,low_memory=False)
dfRH= pd.read_csv('OMSdf_RH.csv',sep=',',skiprows=2,low_memory=False)


dfTA[dfTA <= -9999]=np.nan
dfTA[dfTA <= -50]=np.nan
dfTA[dfTA > 50]=np.nan

[m,n]=dfTA.shape
m = m/720
df = dfTA.iloc[0:1,:]
for mimmo in range(0,m+1):
    vettorino=dfTA.iloc[mimmo*720:((mimmo+1)*720)-1,:]
    mean= vettorino.mean()
    df.loc[mimmo] = mean
    
dfPRP[dfPRP <= -9999]=np.nan
dfPRP[dfPRP <= -0]=np.nan
dfPRP[dfPRP > 200]=np.nan

[M,N]=dfPRP.shape
M = M/720
dfpr = dfPRP.iloc[0:1,:]
for mimmo in range(0,M+1):
    vettorinopr=dfPRP.iloc[mimmo*720:((mimmo+1)*720)-1,:]
    summa= vettorinopr.sum()
    dfpr.loc[mimmo] = summa
    
df.plot()    
dfpr.plot()    
 

df=df.fillna(-9999)
df[df==0]=-9999