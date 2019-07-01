from flask import Flask , render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

app = Flask('__name__')
app.config['SECRET_KEY'] = '352503b0a28a1e79a92dde75ea02b971'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    email = db.Column(db.String(120),nullable=False,unique=True)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

itemlist=[
    {
    "type":"ranica",
    "name":"ranica",
    "prise":"100lv",
    "avalable":"100"
    },
    {
    "type":"chanta",
    "name":"sak",
    "prise":"50lv",
    "avalable":"200"
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title='home')

@app.route('/about')
def about():
    return render_template("about.html",title='about')

@app.route('/items')
def items():
    return render_template("items.html",title='items',items=itemlist,all=all)

@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():

        username=form.username.data
        email=form.email.data
        password=form.password.data
        user=User(username=username,email=email,password=password)
        print(user,"\n \n \n")
        db.session.add(user)
        db.session.commit()
        print(user.query.all())
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data=='email@gmail.com' and form.password.data=='password':
            flash('You have been logged in','success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)

if __name__=='__main__':
    app.run(debug=True)
