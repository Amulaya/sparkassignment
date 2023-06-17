from decouple import config
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/test'.format(config('MYSQL_USER'), config('MYSQL_PASSWORD'),
                                                                 config('MYSQL_HOST'), config('MYSQL_PORT')))
meta = MetaData()
conn = engine.connect()
