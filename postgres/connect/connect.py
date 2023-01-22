import pandas as pd
from sqlalchemy import create_engine
# Important: need to install psycopg2 with conda, conda install psycopg2. Do this after activating conda env
import os 

# connect to db
# replace {database} with name of postgresql database 
engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5432/{database}')
path = r'/src/00_data'
# individual trips
# replace {file} with name of file
path_com = os.path.join(path, '{file}.csv')
table = pd.read_csv(path_com, memory_map=True, nrows=0)
table.columns = table.columns.str.lower()
# replace {table} with name of table and {schema} with name of psql schema 
table.to_sql(name='{table}', schema='{schema}', if_exists='replace', index=True, con=engine)
