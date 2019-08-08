from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_user, current_user
from flaskblog import db
from flaskblog.models import Items
from flaskblog.items.forms import NewItemForm


itemlist=Items.query.all()

items = Blueprint('items',__name__)

@items.route('/items')
def allitems():
    return render_template("items.html",title='items',items=itemlist)


@items.route('/newitem', methods=['GET','POST'])
def newitem():
    form= NewItemForm()
    if form.validate_on_submit():
        print(Items.query.all())
        name=form.name.data
        price=form.price.data
        type=form.type.data
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            image_file =  picture_file
        if Items.query.filter_by(name=name).first():
            flash(f'Name already used!','danger')
            return redirect(url_for('items.newitem'))
        else:

            new_item=Items(price=price,name=name,type=type,image_file=image_file)
            db.session.add(new_item)
            db.session.commit()
            flash(f'Item added {form.name.data}!','success')
            return redirect(url_for('items.allitems'))

    return render_template('newitem.html',title='New Item',form=form)
