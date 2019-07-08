from flaskblog import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False,unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='no.jpg')
    price = db.Column(db.String(10),nullable=False)
    type = db.Column(db.String(30),nullable=False,default='NOT_GIVEN')

    def __repr__(self):
        return f"User('{self.type}','{self.name}','{self.price}','{self.id}','{self.image_file}')"
