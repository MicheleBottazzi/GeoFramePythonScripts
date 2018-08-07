#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 12:44:08 2018

@author: drugo
"""

import os
# Open a file
path = "/home/drugo/Sim/Meledrio/data/Temp"
dirs = os.listdir( path )

# This would print all the files and directories
for indice in range(1,52):
    print(indice)
    T='Temperatura_'+str(indice)+'.csv '
    E='EPT_'+str(indice)+'.csv '
    Net='NetRadiation_'+str(indice)+'.csv '
    SWR='SWdirect_'+str(indice)+'.csv '
    SWF='SWdiffuse_'+str(indice)+'.csv '
    LAI='LAI_'+str(indice)+'.csv '
    PRP='PRP_'+str(indice)+'.csv '
    DEM='DEM_'+str(indice)+'.asc '
    DEMprj='DEM_'+str(indice)+'.prj '
    skyview='skyview_'+str(indice)+'.asc '
    skyviewprj='skyview_'+str(indice)+'.prj ' 
    centroid='centroids_id_'+str(indice)+'.* ' 
    folder=str(indice)
   
   
    stringToLaunch ="mv "+T+E+SWR+SWF+Net+LAI+PRP+DEM+DEMprj+skyview+skyviewprj+centroid+folder+'/'
    
    print(stringToLaunch)
    os.system(stringToLaunch)
    