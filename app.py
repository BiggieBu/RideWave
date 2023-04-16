from flask import Flask, render_template, request, redirect, flash,session, jsonify
from db import login

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
    print(username, password)
    result = login(username, password)
    if result == "Welcome":
      session['username'] = username
      session['password'] = password
      return redirect('/login/attempt?username={}'.format(username))
    else:
      flash(result, 'error')
  return render_template('login.html')

@app.route("/login/attempt")
def data_page():
  username = session.get('username')
  password = session.get('password')
  return render_template('loggedin.html',username = username)
@app.route("/signup")
def signup():
  return render_template('signup.html')

@app.route("/users/apply", methods=['post'])
def register_user():
  data = request.form
  return jsonify(data)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
