from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}','{self.password}')"

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemid = db.Column(db.Integer,nullable=False)
    userid = db.Column(db.Integer,nullable=False)
    time = db.Column(db.DateTime,nullable=False,default=datetime.utcnow )

    def __repr__(self):
        return f"Orders('{self.id}','{self.itemid}','{self.userid}')"

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False,unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='no.jpg')
    price = db.Column(db.String(10),nullable=False)
    type = db.Column(db.String(30),nullable=False,default='NOT_GIVEN')

    def __repr__(self):
        return f"Items('{self.type}','{self.name}','{self.price}','{self.id}','{self.image_file}')"
