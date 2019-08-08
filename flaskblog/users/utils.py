import os
import secrets


def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static\item_pics',picture_fn)
    print(picture_path,"\n \n \n \n ")
    form_picture.save(picture_path)
    return picture_fn
