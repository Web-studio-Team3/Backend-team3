import os
from uuid import uuid4
from PIL import Image

static = "static"


def save_picture(file):
    random_uid = str(uuid4())
    _, f_ext = os.path.splitext(file.filename)

    picture_name = random_uid + f_ext

    path = os.path.join(static)
    if not os.path.exists(path):
        os.makedirs(path)

    picture_path = os.path.join(path, picture_name)

    img = Image.open(file.file)
    img.save(picture_path)

    return f'{static}/{picture_name}'


def delete_picture(photo_url: str):
    os.remove(photo_url)
