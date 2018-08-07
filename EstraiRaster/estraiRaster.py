#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:44:58 2018

@author: Michele Bottazzi
@mail michele.bottazzi@gmail.com
"""

# LEGGO I FILE   

############################################
#####     First part of the script     #####
#  Cut a raster.asc using shapefile masks  #
###    Save the cutted raster as .tif    ###
############################################

import os
# Open a file
path = "/home/drugo/GeoFramePythonScripts/EstraiRaster/InputFolder"                # Inut folder
dirs = os.listdir( path )           # Set the current directory as the input folder
pathOut = "/home/drugo/GeoFramePythonScripts/EstraiRaster/OutputFolder"            # Output folder
listOfTheFiles ="subbasin5000_ID"   # Name of the mask shapefile
xresolution="30.005356186395"         # resolution of raster
yresolution="30.005356186395"         # resolution of raster
rasterFileInput = 'DEM'             # Name of the raster

    
import glob
filesSHP=glob.glob(path+'/'+listOfTheFiles+'*.shp')
for fileSHP in filesSHP:        
    #print(fileSHP)
    fileHDFinput = fileSHP
    fileTIFoutput = fileHDFinput.replace(path, pathOut)
    fileTIFoutput = fileTIFoutput.replace(listOfTheFiles, rasterFileInput)
    fileTIFoutput = fileTIFoutput.replace('.shp', '.tif')
    first = 'gdalwarp -q -cutline '
    second = fileHDFinput
    third = ' -crop_to_cutline -tr '+xresolution+' '+yresolution+' -of GTiff '
    fourth = path+'/'+rasterFileInput+'.asc '
    fifth = fileTIFoutput
    stringToLaunch='sudo '+first+second+third+fourth+fifth
    print(stringToLaunch)
    os.system(stringToLaunch)
    



############################################
###     Second part of the script        ###
###  Convert output file of the previous ###
#####      script from .tif to .asc    #####
############################################

filesTIF=glob.glob(pathOut+"/*.tif")    
for fileTIF in filesTIF:        
    fileHDFoutput = fileSHP
    fileHDFoutput = fileTIF.replace('.tif', '.asc')
    first = 'gdal_translate -of AAIGrid '
   
    stringToLaunchII='sudo '+first+fileTIF+' '+fileHDFoutput
    print(stringToLaunchII)

    #os.system(stringToLaunchII)
