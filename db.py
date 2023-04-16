from sqlalchemy import  create_engine,text

db_conn_str = "mysql+pymysql://pzzz55wxbxerfsaqc60q:pscale_pw_fMbvXDrFA3mzsPnOwKKRPmrwUVXfpWGnCp22d4cUgRC@aws.connect.psdb.cloud/ridewave?charset=utf8mb4"

engine = create_engine(db_conn_str, connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
},echo=True) 
def row_to_dict(result_proxy, i):
    row = result_proxy.fetchone()
    if row:
        column_names = result_proxy.keys()
        values = row
        diction = dict(zip(column_names, values))
        return diction
    else:
        return {}

def login(name, pword):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT username, password FROM Users WHERE username = :val"), {"val": name})
        d = row_to_dict(result, 0)
        if not d:
            print("Username not found")
        elif d['password'] == pword:
            print("Welcome")
        else:
            print("Wrong password")

