from flask import Flask , render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

app = Flask('__name__')
app.config['SECRET_KEY'] = '352503b0a28a1e79a92dde75ea02b971'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

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


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title='home')

@app.route('/about')
def about():
    return render_template("about.html",title='about')

@app.route('/items')
def items():
    return render_template("items.html",title='items',items=Items.query.all())

@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        print(Users.query.all())
        username=form.username.data
        email=form.email.data
        password=form.password.data
        if Users.query.filter_by(username=username).first():
            flash(f'Could not create account.Username or email is already taken!','danger')
            return redirect(url_for('register'))
        else:
            user=Users(username=username,password=password,email=email)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!','success')
            print(Users.query.all())
            return redirect(url_for('home'))
            
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    email=form.email.data
    password=form.password.data
    user=Users(email=email,password=password)

    if form.validate_on_submit():
        if Users.query.filter_by(email=email,password=password).first():
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)
