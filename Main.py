db_path = r".\db\test.db"

from flask import Flask, render_template, request
# from flask_bootstrap import Bootstrap
from Database import Database
import os
import hashlib
from PIL import Image

app = Flask(__name__, template_folder =  './assets')


@app.route('/', methods = ['GET', 'POST'])
def homePage():
    hash_key = "0"
    filename = "template.png"
    if request.method == 'POST':
        try:
            db = Database(db_path)
            hash_key, photo_path = db.selectLast()
            img = Image.open(photo_path)
            img.save("./static/car_image.png", "PNG")
            filename = 'car_image.png'
            # photo_path = photo_path.replace("\\", "/")
        except:
            print("Couldn't connect to database or load image")
        
        first_two = hash_key[:2]
        last_two = hash_key[-2:]
        hash_key = hash_key

    return render_template("index.html", hash_key = hash_key, filename = filename)

@app.route('/input', methods = ['GET' , 'POST'])
def inputPage():
    hide = 1
    new_hash_key = "0"
    hash_key = "0"
    filename = "template.png"
    if(request.method == 'POST'):
        iin = request.form['iin']
        plate_id = request.form['plate_id']
        print(plate_id)
        new_hash_key = hashlib.sha256(plate_id.encode()).hexdigest()
        print(new_hash_key)
        db = Database(db_path)
        hash_key, photo_path = db.selectByHash(new_hash_key)
        if(hash_key != None):
            img = Image.open(photo_path)
            img.save("./static/input_car_image.png", "PNG")
            filename = 'input_car_image.png'
            hide = 0
        else:
            hide = 2
            hash_key = "0"
        
    return render_template("input.html", hide = hide, new_hash_key = new_hash_key, hash_key = hash_key, filename = filename)

if __name__ == '__main__':
    app.run(host = "localhost", port = 5000)