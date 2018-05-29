"""
Created on Tue Apr 17 10:33:08 2018
@author: Michele Bottazzi
"""

import pandas as pd

"""
Skiprows va messo uguale al numero di riga dove si trova 'Type,Date,Double...Double'.
 Generalmente skiprows = 6 per le intestazioni di Oms di 8 righe
"""
df= pd.read_csv('Temperature.csv',sep=',',skiprows=6,low_memory=False)

Data = df.iloc[1:,1:]
Data = Data.set_index('Date')