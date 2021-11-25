import os
from flask import Flask, send_from_directory

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
IMAGES_FOLDER = f"{os.getenv('APP_FOLDER')}/images"

@app.route('/')
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/images/<path:filename>")
def imagefiles(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

