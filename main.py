from engine import run
from flask import Flask, request
from werkzeug.utils import secure_filename
import os
from flask import jsonify


app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')

os.makedirs(uploads_dir, exist_ok=True)


@app.route("/detect", methods=['POST'])
def detect():
    if not request.method == "POST":
        return
    video = request.files['image']
    video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
    IMAGE_PATH = os.path.join(uploads_dir, secure_filename(video.filename))
    out,bbox = run(IMAGE_PATH)
    return jsonify([out,bbox])

if __name__ == '__main__':
    port = 8080
    app.run(host='0.0.0.0',port=port)