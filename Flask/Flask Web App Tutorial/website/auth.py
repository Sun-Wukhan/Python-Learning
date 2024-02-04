from flask import Flask, redirect, url_for
from flask import Blueprint, render_template, request, flash
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
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
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4: 
            flash('Email too short', category='error')
        elif len(first_name) < 2: 
            flash('name must be a valid name', category='error')
        elif password1 != password2: 
            flash('Password not matching', category='error')
        else: 
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash("YAY!", category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")

