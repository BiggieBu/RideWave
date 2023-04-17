from flask import Flask, render_template, request, redirect, flash,session, jsonify
from db import login,signupinsert,clusterinsert,loadclusters,loaddetails,loadpool,loadrequests,requestaccepted,requestinsert,loadstatus,match,loadcluster_part

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route("/")
def hello():
  return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    result = login(username, password)
    if result == "Welcome":
      session['username'] = username
      return redirect('/user/{}'.format(username))
    else:
      flash(result, 'error')
  return render_template('login.html')

@app.route("/user/<id>")
def data_page(id):
  return render_template('loggedin.html',username = id)

@app.route("/signup",methods=['GET','POST'])
def signup():
  if request.method=='POST':
    data=request.form
    result=signupinsert(data)
    if result == "Success":
      return redirect('/login')
    else:
      flash(result, 'error')
  return render_template('signup.html')
  
@app.route("/user/<id>/driver_form",methods=['GET','POST'])
def driver_form(id):
  if request.method=='POST':
    data=request.form
    result=clusterinsert(id,data)
    if result=="Success":
      return redirect('/user/{}/clusters'.format(id))
    else:
      flash(result,'error')
  return render_template("driver_form.html",username=id)
@app.route("/user/<id>/clusters")
def cluster(id):
  clusters=loadclusters(id)
  cluster_part=loadcluster_part(id)
  return render_template('cluster.html',username=id,clusters=clusters,clusters_part=cluster_part)
@app.route("/user/<id>/clusters/<cid>")
def details(id,cid):
  det=loaddetails(cid)
  passengers=loadpool(cid)
  return render_template('details.html',username=id,clusters=cid,details=det,passengers=passengers)
@app.route("/user/<id>/requests")
def req(id):
  requests=loadrequests(id)
  return render_template('request.html',username=id,requests=requests)
@app.route("/processing/<what>/<id>/<rid>", methods=['GET', 'POST'])
def accept_request(id,rid,what):
  c=requestaccepted(rid,what)
  if what=='0':
    return redirect('/user/{}/requests'.format(id))
  else:
    return redirect('/user/{}/clusters/{}'.format(id, c))
@app.route("/user/<id>/rider_form",methods=['GET','POST'])
def rider_form(id):
  if request.method=='POST':
    data=request.form
    lat=data.get('lat')
    lng=data.get('lng')
    return redirect("/user/{}/rider_form/options/{}/{}".format(id,lat,lng))
  return render_template("rider_form.html",username=id)
@app.route("/user/<id>/rider_form/options/<lat>/<lng>")
def options(id,lat,lng):
  m=match(id,lat,lng)
  return render_template("options.html",username=id,lat=lat,lng=lng,match=m)
@app.route("/user/<id>/rider_form/options/<lat>/<lng>/<cid>/<admin>",methods=['GET','POST'])
def req_insert(cid,id,lat,lng,admin):
  requestinsert(admin,cid,id,lat,lng)
  return redirect('/user/{}/request_status'.format(id))
@app.route("/user/<id>/request_status")
def status(id):
  stat=loadstatus(id)
  return render_template('request_status.html',username=id,status=stat)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)



