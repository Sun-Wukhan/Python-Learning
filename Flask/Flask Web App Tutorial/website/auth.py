from flask import Flask 
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    return render_template("login.html", boolean=True, text="Hello World", user="Navid")

@auth.route('/logout')
def log_out(): 
    return "<p>Log out</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up(): 
    
    if request.method == 'POST': 
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4: 
            flash('Email too short', category='error')
        elif len(firstName) < 2: 
            flash('name must be a valid name', category='error')
        elif password1 != password2: 
            flash('Password not matching', category='error')
        else: 
            flash("YAY!", category='success')
    
    return render_template("sign_up.html")

