from sqlalchemy import create_engine, text

db_connect = "mysql+pymysql://ifizevr80rkvnwrv6pnz:pscale_pw_ASH46oqQxFWN0QQxqz2ma1cERUtPY7UvSzF7WMGc8z3@aws.connect.psdb.cloud/joviancareer?charset=utf8mb4"
engine = create_engine(db_connect,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs;"))
  result_dicts = []
  for row in result.all():
    result_dicts.append(row._mapping)

  print(result.dicts)