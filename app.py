from flask import Flask, render_template, request, redirect, flash,session, jsonify
from db import login,signupinsert,requestinsert,loadclusters,loaddetails,loadpool

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
    result=requestinsert(id,data)
    if result=="Success":
      return redirect('/user/{}/clusters'.format(id))
    else:
      flash(result,'error')
  return render_template("driver_form.html",username=id)
@app.route("/user/<id>/clusters")
def req(id):
  clusters=loadclusters(id)
  return render_template('cluster.html',username=id,clusters=clusters)
@app.route("/user/<id>/clusters/<cid>")
def cluster(id,cid):
  details=loaddetails(cid)
  passengers=loadpool(cid)
  return render_template('details.html',username=id,clusters=cid,details=details,passengers=passengers)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)



