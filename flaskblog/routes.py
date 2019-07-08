from flask import render_template, flash, redirect, url_for
from flaskblog import app, db
from flaskblog.models import Users, Items
from flaskblog.forms import RegistrationForm,LoginForm

print(Items.query.all(),Users.query.all())
itemlist=Users.query.all()

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",title='home')

@app.route('/about')
def about():
    return render_template("about.html",title='about')

@app.route('/items')
def items():
    return render_template("items.html",title='items',items=itemlist)

@app.route('/register', methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        print(Users.query.all())
        username=form.username.data
        email=form.email.data
        password=form.password.data
        if Users.query.filter_by(username=username).first()or Users.query.filter_by(email=email).first():
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
