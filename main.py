from engine import run
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os


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
    out = run(IMAGE_PATH)
    return out
