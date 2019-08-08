from flask import render_template, flash, redirect, url_for, request, Blueprint
from flaskblog import db, bcrypt
from flaskblog.models import Users
from flaskblog.users.forms import RegistrationForm,LoginForm
from flask_login import login_user, current_user, logout_user, login_required




users = Blueprint('users',__name__)
@users.route('/register', methods=['GET','POST'])
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
            return redirect(url_for('users.register'))
        else:
            user=Users(username=username,password=hashed_password,email=email)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!','success')
            print(Users.query.all())
            return redirect(url_for('users.login'))

        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('main.home'))
    return render_template('register.html',title='Register',form=form)


@users.route('/login', methods=['GET','POST'])
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
            return  redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful','danger')
    return render_template('login.html',title='Login',form=form)

@users.route("/account")
@login_required
def account():
    image_file = url_for('static',filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',title='Account',image_file=image_file)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))
