from flask import Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return 'No video file provided', 400

    video_file = request.files['video']
    video_file.save(r'E:\Flutter Projects\flaskserver\Videos' + video_file.filename)
    return 'Video file uploaded successfully', 200

if __name__ == '__main__':
    app.run(host="YourIp", port=5000, debug=True)
