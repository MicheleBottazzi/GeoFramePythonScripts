#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:44:58 2018

@author: drugo
"""

# LEGGO I FILE   

import os
# Open a file
path = "/home/drugo/Sim/prova"
dirs = os.listdir( path )
pathOut = "/home/drugo/Sim/prova"


    
import glob
filesSHP=glob.glob("/home/drugo/Sim/prova/subbasin*.shp")
for fileSHP in filesSHP:        
    print(fileSHP)
    fileHDFinput = fileSHP
    fileTIFoutput = fileHDFinput.replace('subbasins_A_DN', 'DEM')
    fileTIFoutput = fileTIFoutput.replace('.shp', '.tif')
    first = 'gdalwarp -q -cutline '
    second = fileHDFinput
    third = ' -crop_to_cutline -tr 30.0053561864 30.0053561864 -of GTiff '
    fourth = '/home/drugo/Sim/prova/DEM_bacino_A.asc '
    fifth = fileTIFoutput
    stringToLaunch=first+second+third+fourth+fifth
    os.system(stringToLaunch)
    

filesTIF=glob.glob("/home/drugo/Sim/prova/*.tif")    
for fileTIF in filesTIF:        
    fileHDFoutput = fileSHP
    fileHDFoutput = fileTIF.replace('.tif', '.asc')
    first = 'gdal_translate -of AAIGrid '
   
    stringToLaunchII=first+fileTIF+' '+fileHDFoutput
    os.system(stringToLaunchII)
