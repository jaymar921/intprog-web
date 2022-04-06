from flask import Flask, redirect, url_for,render_template,request
from database import register_account, hashString, getAccount
from random import randint

app = Flask(__name__)


# go to landing page
@app.route("/")
def landing_page():
    return render_template("LandingPage.html")


# calls the login.html, asks the user to enter email and password
@app.route("/login")
def login():
    return render_template("Login.html")


# retrieves data from login form, check if account exist in database
@app.route("/login_account", methods=['POST'])
def loginAccount():
    if getAccount(request.form["email"], hashString(request.form["psw"])):
        return render_template("LandingPage.html", account=request.form["email"])
    else:
        return "invalid"


# calls the registration.html
@app.route("/register")
def register():
    return render_template("registration.html", remark="")


# retrieves the data from registration form
@app.route("/register_account", methods=["POST"])
def registerAccount():
    if "deny" in request.form['flag']:
        return render_template("registration.html", remark="Password Mismatch!")
    data: dict = {
        "lastname": request.form['lastname'],
        "firstname": request.form['firstname'],
        "email": request.form['email'],
        "contact": request.form['number'],
        "password": request.form['password']
    }
    register_account(randint(0, 19999), data['lastname'], data['firstname'], data['email'], data['contact'], hashString(data['password']))
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
