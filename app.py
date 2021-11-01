from flask import Flask, jsonify, request
from yolo_detection_images import YoloDetection

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, please send a pic'


@app.route('/<path:img_path>')
def home(img_path):

    return YoloDetection(img_path)


if __name__ == '__main__':
    app.run(debug=True)
