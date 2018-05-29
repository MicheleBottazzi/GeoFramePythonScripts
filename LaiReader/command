
#With this command, pymodis download all the lai hdf files from 2007-01-01 to 2007-12-31
# and store it into the folder cartella_dei_hdf
modis_download.py -I -r -s MOLT -p MOD15A2H.006 -t h18v04  -f 2007-01-01 -e 2007-12-31 cartella_dei_hdf/


#With this command convert lai into 32632 and extract tif
modis_convert.py -s "( 0 1 )" -o best_FILE -g 500 -e 32632 MOD15A2H.A2007001.h18v04.006.2015126043506.hdf
