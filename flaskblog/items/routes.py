import os
import secrets
from flaskblog.items.utils import save_picture
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_user, current_user
from flaskblog import db
from flaskblog.models import Items
from flaskblog.items.forms import NewItemForm



items = Blueprint('items',__name__)

@items.route('/items')
def allitems():
    page = request.args.get('page',1,type=int)
    show_items = Items.query.order_by(Items.id.desc()).paginate(page=page, per_page=10)
    return render_template("items.html",title='items',items=show_items)


#def save_picture(form_picture):
#    random_hex = secrets.token_hex(8)
#    _,f_ext = os.path.splitext(form_picture.filename)
#    picture_fn = random_hex + f_ext
#    picture_path = os.path.join(app.root_path,'static/item_pics', picture_fn)
#    outpu_size = (125,125)
#    i = Image.open(form_picture)
#    i.thumbnail(outpu_size)
#    i.save(picture_path)
#    return picture_fn

@items.route('/newitem', methods=['GET','POST'])
def newitem():
    form = NewItemForm()
    if form.validate_on_submit():
        print(Items.query.all())
        name=form.name.data
        price=form.price.data
        type=form.type.data
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            image_file =  picture_file
            new_item=Items(price=price,name=name,type=type,image_file=image_file)
        if Items.query.filter_by(name=name).first():
            flash(f'Name already used!','danger')
            return redirect(url_for('items.newitem'))
        else:

            if new_item:
                db.session.add(new_item)
                db.session.commit()
                flash(f'Item added {form.name.data}!','success')
                return redirect(url_for('items.allitems'))
            else:
                flash(f'Put image','danger')
                return redirect(url_for('items.newitem'))


    return render_template('newitem.html',title='New Item',form=form)



@items.route('/specific_items/')
def specific_items():
    page = request.args.get('page',1,type=int)
    item_type = request.args.get('type',"ranica",type=str)
    print(page,item_type,"\n\n\n\n\n\n\n\n")
    show_items = Items.query.filter_by(type=item_type)\
    .order_by(Items.id.desc())\
    .paginate(page=page, per_page=10)
    return render_template("items.html",title='items',items=show_items)



    #show_items = Items.query.filter_by(type=type)\
    #.order_by(Items.id.desc())\
    #.paginate(page=page, per_page=10)
