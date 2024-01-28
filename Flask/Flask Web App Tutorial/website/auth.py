from flask import Flask 
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def log_out(): 
    return "<p>Log out</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up(): 
    return render_template("sign_up.html")
