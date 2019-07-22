db_path = r".\db\test.db"

from flask import Flask, render_template, request
# from flask_bootstrap import Bootstrap
from Database import Database
import os
import hashlib
from PIL import Image
import json

app = Flask(__name__, template_folder =  './assets')

def readFromSBP(plate_id):
    try:
        hash_code = "0"
        status = "NOT OK"
        with open("example.json", encoding='utf-8') as f:
            data = json.load(f)
            hash_code = data[plate_id]["hash"]
            status = data[plate_id]["status"]
        return hash_code, status
    except Exception as e:
        print(e)
        return "0", "NOT OK"



@app.route('/', methods = ['GET', 'POST'])
def homePage():
    hash_key = "0"
    filename = "images/template.png"
    if request.method == 'POST':
        try:
            db = Database(db_path)
            hash_key, photo_path = db.selectLast()
            img = Image.open(photo_path)
            img.save("./static/images/car_image.png", "PNG")
            filename = 'images/car_image.png'
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
    filename = "images/template.png"
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
            img.save("./static/images/input_car_image.png", "PNG")
            filename = 'images/input_car_image.png'
            hide = 0
        else:
            hide = 2
            hash_key = "0"
        
    return render_template("input.html", hide = hide, new_hash_key = new_hash_key, hash_key = hash_key, filename = filename)


@app.route('/input-v2', methods = ['GET' , 'POST'])
def inputV2Page():
    hide = 1
    new_hash_key = "0"
    hash_key = "0"
    filename = "images/template.png"
    status = "NOT OK"
    if(request.method == 'POST'):
        iin = request.form['iin']
        plate_id = request.form['plate_id']
        print(plate_id)
        new_hash_key = hashlib.sha256(plate_id.encode()).hexdigest()
        print(new_hash_key)
        db = Database(db_path)
        new_hash_key, photo_path = db.selectByHash(new_hash_key)
        hash_key, status = readFromSBP(plate_id)

        if(new_hash_key != None):
            img = Image.open(photo_path)
            img.save("./static/images/input_car_image.png", "PNG")
            filename = 'images/input_car_image.png'
            hide = 0
        else:
            new_hash_key = ""
            hide = 2
        
    return render_template("input_v2.html", hide = hide, status = status ,new_hash_key = new_hash_key, hash_key = hash_key, filename = filename)

if __name__ == '__main__':
    app.run(host = "localhost", port = 5000)