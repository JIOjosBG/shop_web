from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask('__name__')
app.config['SECRET_KEY'] = '352503b0a28a1e79a92dde75ea02b971'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes