from sqlalchemy import  create_engine,text

db_conn_str = "mysql+pymysql://617onh5prl2dg7bx8zmk:pscale_pw_M3XjrIaych0xj9g1Asob8s7LkVXSKqFuYtlET238843@aws.connect.psdb.cloud/ridewave?charset=utf8mb4"

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
            return("Username not found")
        elif d['password'] == pword:
            return("Welcome")
        else:
            return("Wrong password")

login('Parv','suparv')

