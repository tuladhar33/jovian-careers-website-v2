import os
from sqlalchemy import create_engine, text

my_user = os.environ['user']
my_pass = os.environ['passwd']

db_connect = f"mysql+pymysql://{my_user}:{my_pass}@aws.connect.psdb.cloud/joviancareer?charset=utf8mb4"
engine = create_engine(db_connect,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs;"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(row._mapping)

  print(result_dicts)
