from flask import Flask, render_template,jsonify,request
from db import login

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('home.html')
  
@app.route("/login")
def login_page():
  return render_template('login.html')
  
@app.route("/login/attempt", methods=["POST"])
def data_page():
    username = request.form.get("username")
    password = request.form.get("password")
    login(username, password)
    return jsonify({"username": username, "password": password})

  
@app.route("/signup")
def signup():
  return render_template('signup.html')
  
@app.route("/users/apply", methods =['post'])
def register_user():
  data = request.form
  
  return jsonify(data)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)