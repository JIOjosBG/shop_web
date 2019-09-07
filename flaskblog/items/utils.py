import os
import secrets
from PIL import Image
from flask import url_for
from flaskblog import app


def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/item_pics',picture_fn)

    outpu_size=(200,200)
    i = Image.open(form_picture)
    i.thumbnail(outpu_size)
    i.save(picture_path)

    #form_picture.save(picture_path)
    return picture_fn
