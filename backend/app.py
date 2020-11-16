import os
from flask import Flask, render_template, request
# from flask_cors import CORS, cross_origin
# import json
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
PORT = 5000
DEBUG = True
# cors = CORS(app, resources={r"/api/*":{"origins":"*"}})
app.config['UPLOAD_IMAGE'] = "./uploaded_images"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/uploader', methods=['POST'])
# @cross_origin(allow_headers=['Content-Type'])
def uploader():
    if request.method == "POST":
        f = request.files['image']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_IMAGE'], filename))
        return "File uploaded successfully"



if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
# -------------- API - fin--------------------------
