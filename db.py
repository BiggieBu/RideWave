from sqlalchemy import  create_engine,text
#Username=ldx9p3zooxyyff0jt88o
#Password=pscale_pw_5zBWA58QAqQucdH9cBoW5dwKzAiD4ZRyyUu1TKbdPaA
db_conn_str = "mysql+pymysql://ldx9p3zooxyyff0jt88o:pscale_pw_5zBWA58QAqQucdH9cBoW5dwKzAiD4ZRyyUu1TKbdPaA@aws.connect.psdb.cloud/ridewave?charset=utf8mb4"

engine = create_engine(db_conn_str, connect_args={
  "ssl":{
    "ssl_ca": "/etc/ssl/cert.pem"
  }
},echo=True) 
def row_to_dict(result_proxy):
    row = result_proxy.fetchone()
    if row:
        column_names = result_proxy.keys()
        values = row
        diction = dict(zip(column_names, values))
        return diction
    else:
        return {}
def rows_to_list_of_dicts(result_proxy):
    rows = []
    for row in result_proxy:
        column_names = result_proxy.keys()
        values = row
        diction = dict(zip(column_names, values))
        rows.append(diction)
    return rows

def login(name, pword):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT username, password FROM Users WHERE username = :val"), {"val": name})
        d = row_to_dict(result)
        if not d:
          print("no user")
          return("Username not found")
        elif d['password'] == pword:
          print("welcome")
          return("Welcome")
        else:
          print("no pass")
          return("Wrong password")



def signupinsert(data):
  username = data['uname']
  firstname = data['fname']
  lastname = data['lname']
  email = data['mail']
  phoneNo = data['phone']
  password = data['pass']
  try:
        with engine.connect() as conn:
           conn.execute(
               text("insert into Users(`username`, `userFirstName`, `userLastName`, `EmailID`, `PhoneNo.`, `password`)values(:z,:x,:y,:a,:b,:c)"),
              {"x": firstname, "y": lastname, "z": username, "a": email, "b": phoneNo, "c": password}
           )
        return "Success"
  except Exception as e:
        return str(e)
def requestinsert(id,data):
  carname= data['carname']
  carno= data['carno']
  cost=data['cost']
  initx=data['initx']
  inity=data['inity']
  finalx=data['finalx']
  finaly=data['finaly']
  leavedate=data['leavedate']
  leavetime=data['leavetime']
  seats=data['seats']
  try:
        with engine.connect() as conn:
           conn.execute(
               text("insert into Cluster(`adminusername`,`carname`, `carNo`, `cost`, `initiallocationx`, `initiallocationy`, `finallocationx`,`finallocationy`,`leavingtime`,`leavedate`,`seats`)values(:v0,:v1,:v2,:v3,:v4,:v5,:v6,:v7,:v8,:v9,:v10)"),
              {"v0":id,"v1": carname, "v2": carno, "v3": cost, "v4": initx, "v5": inity, "v6": finalx,"v7":finaly,"v9":leavedate,"v8":leavetime,"v10":seats}
           )
        return "Success"
  except Exception as e:
        return str(e)
def loadclusters(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Cluster where adminusername=:val"), {"val": id})
    return rows_to_list_of_dicts(result)

def loaddetails(cid):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Cluster where clusterid=:val"), {"val": cid})
    return row_to_dict(result)

def loadpool(cid):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Users where clusterid=:val"), {"val": cid})
    return rows_to_list_of_dicts(result)