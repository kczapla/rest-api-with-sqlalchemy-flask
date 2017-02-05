from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)

from app import mod_users
from app.mod_users.view import users
app.register_blueprint(users, url_prefix='/api/v1/users')
