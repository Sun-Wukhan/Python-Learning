from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt
import os 
import logging 
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

if not app.debug: 
    file_handler = RotatingFileHandler("instance/flask_app.log", maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Flask app startup')

@app.before_request 
def before_request_logging(): 
    app.logger.info(f"Request: {request.method} {request.url}")

@app.after_request 
def after_request_logging(response): 
    app.logger.info(f"Response: {response.status} {response.content_type}")
    return response  # Ensure this line is present

from app import routes
from app import models 