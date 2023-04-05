from sqlalchemy import  create_engine

db_conn_str = "mysql+pymysql://pzzz55wxbxerfsaqc60q:pscale_pw_fMbvXDrFA3mzsPnOwKKRPmrwUVXfpWGnCp22d4cUgRC@aws.connect.psdb.cloud/ridewave?charset=utf8mb4"

engine = create_engine(db_conn_str, connect_args={
  "ssl":{
    "ca": "/etc/ssl/cert.pem"
  }
})