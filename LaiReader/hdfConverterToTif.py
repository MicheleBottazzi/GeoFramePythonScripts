#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:49:56 2018

@author: drugo
"""

# LEGGO I FILE   

import os
# Open a file
path = "/home/drugo/pyModis/scripts/lst_terra"
dirs = os.listdir( path )

# This would print all the files and directories
for files in dirs:
    fileHDFinput = files
    #print('1 ' + fileHDFinput)
    fileTIFoutput = fileHDFinput.replace('.', '_')
   #print('2 ' + fileTIFoutput)
    fileTIFoutput = fileTIFoutput.replace('_hdf', '')
    #print('3 ' + fileTIFoutput)
    #print(fileTIFoutput)
    first = 'modis_convert.py -s "( 0 1 )" -o '
    second =' -g 500 -e 32632 '    
    stringToLaunch =first+fileTIFoutput+second+fileHDFinput
    print(stringToLaunch)
   # os.system(stringToLaunch)
    
