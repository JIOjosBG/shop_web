from flask import render_template, flash, redirect, url_for, request
from flaskblog import app, db, bcrypt
from flaskblog.models import Users, Items
from flaskblog.forms import RegistrationForm,LoginForm, NewItemForm
from flask_login import login_user, current_user, logout_user, login_required

itemlist=Items.query.all()


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
        hashed_password=bcrypt.generate_password_hash(password).decode("utf-8")
        if Users.query.filter_by(username=username).first() or Users.query.filter_by(email=email).first():
            flash(f'Could not create account.Username or email is already taken!','danger')
            return redirect(url_for('register'))
        else:
            user=Users(username=username,password=hashed_password,email=email)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!','success')
            print(Users.query.all())
            return redirect(url_for('login'))
            
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    email=form.email.data
    password=form.password.data
    remember=form.remember.data
    if form.validate_on_submit():
        print(Users.query.all())
        user = Users.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user, remember=remember)
            next_page=request.args.get('next')
            return  redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)


@app.route('/newitem', methods=['GET','POST'])
def newitem():

    form= NewItemForm()
    if form.validate_on_submit():
        print(Items.query.all())
        name=form.name.data
        price=form.price.data
        type=form.type.data
        image_file=form.image.data
        if Items.query.filter_by(name=name).first():
            flash(f'Name already used!','danger')
            return redirect(url_for('newitem'))
        else:

            new_item=Items(price=price,name=name,type=type,image_file=image_file)
            db.session.add(new_item)
            db.session.commit()
            flash(f'Item added {form.name.data}!','success')
            return redirect(url_for('items'))
            
    return render_template('newitem.html',title='New Item',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title='Account')