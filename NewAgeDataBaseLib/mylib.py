import pandas as pd

def h5store(filename, df, **kwargs):
	store = pd.HDFStore(filename)
	store.put('mydata', df)
	store.get_storer('mydata').attrs.metadata = kwargs
	store.close()


def h5load(store):
	data = store['mydata']
	metadata = store.get_storer('mydata').attrs.metadata
	return data, metadata


def readOMS(file):
	"Read OMS dataframe"
	with open(file) as f:
		l=0
		v=f.readline().split(',')
		while v[0]!='':
			l=l+1
			v=f.readline().split(',')
			if v[0]=='@H':
				lh=l+1
				ncols=len(v)
	skip=list(range(l))
	skip.remove(lh)
	#df = pd.read_csv(file, skiprows=skip, index_col='timestamp', usecols=range(1,ncols), na_values='-9999.0')
	df = pd.read_csv(file, skiprows=skip, na_values='-9999.0')
	st_id=df.columns.values[0]
	df = df.drop(st_id, 1)
	df.columns = [st_id + '_' + str(col) for col in df.columns]
	df.columns.values[0] = 'timestamp'
	df = df.set_index(['timestamp'])
	df.index = pd.DatetimeIndex(df.index)
	df = round(df,3)
	#metadata= dict(st_id='ID')
	#h5store('/tmp/data.h5', df, **metadata)
	return df


def writeOMS(df,path):
	"Write OMS dataframe"
	df.to_csv(path, sep=",", na_rep="-9999",index_label='timestamp',date_format='%Y-%m-%d %H:%M', header=False)

	st_id = str(df.columns.values[0].rpartition('_')[0])
	ids=[c.replace(st_id + '_', '') for c in df.columns.values]

	# header with numbered columns
	h1 = '@T,table\n'
	h2 = '@H,timestamp,' + 'val_' + ',val_'.join(ids) + '\n'
	h3 = st_id + ',  ,' + ','.join(ids) + '\n'
		
	#with pd.HDFStore('/tmp/data.h5') as store:
	#	data, metadata = h5load(store)
		
	# add OMS header
	with open(path, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write(h1 + h2 + h3 + ',' + ','.join(content.splitlines(True)))



def shp2df(shp_path):
	"""
	Read a shapefile into a Pandas dataframe with a 'coords' column holding
	the geometry information. This uses the pyshp package
	"""
	import shapefile

	#read file, parse out the records and shapes
	sf = shapefile.Reader(shp_path)
	fields = [x[0] for x in sf.fields][1:]
	records = sf.records()
	shps = [s.points for s in sf.shapes()]

	#write into a dataframe
	df = pd.DataFrame(columns=fields, data=records)
	df = df.assign(coords=shps)
	return df


