from yolo_detection_images import YoloDetection, YoloDetectionImg, YoloDetectionOnlyTags
from flask import Flask, jsonify, request
import requests
import shutil
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hello, please send a pic'


# @app.route('/image', methods=['POST'])
# def detect():
#     if request.method == 'POST':
#         file = request.value['image']
#         result = YoloDetectionImg(file)

#         return jsonify(result)
#     else:
#         return jsonify({'error': 'Please send a pic'})

@app.route('/detect', methods=['POST'])
@cross_origin()
def detect():
    data = request.get_json()
    image_url = data['img_url']
    name = image_url.split('?')[-2]
    filename = name.split("/")[-1]

    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
        results = YoloDetectionOnlyTags(filename)
        # write command to delete file
        os.remove(filename)
        return jsonify(results)

    else:
        print('Image Couldn\'t be retreived')


@app.route('/<path:img_path>')
def home(img_path):

    return YoloDetection(img_path)


if __name__ == '__main__':
    app.run(debug=True)
