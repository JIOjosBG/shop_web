from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask('__name__')
app.config['SECRET_KEY'] = '352503b0a28a1e79a92dde75ea02b971'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category = 'info'

from flaskblog.users.routes import users
from flaskblog.items.routes import items
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(items)
app.register_blueprint(main)
