from flask import Flask, request, jsonify
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
import json
from main import uploadFile, getFile, getStructure

from helper import sequalizeData

from flask_cors import CORS

app = Flask(__name__)
# limiter = Limiter(app, key_func=get_remote_address)

# @limiter.limit("10 per minute")
CORS(app)
@app.route('/heath', methods=['GET'])
def index():
    return 'ok', 200

CORS(app)
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    response = uploadFile(file);
    if(response):
        return "", 200
    else:
        return "", 400

CORS(app)
@app.route('/file', methods=['POST'])
def file():
    data = request.json
    file = getFile(data)
    if(file):
        return file
    else:
        return "", 400

CORS(app)
@app.route('/processing', methods=['POST'])
def structure():
    data = request.json
    structure = getStructure(data)
    if(structure):
        return sequalizeData(structure)
    else:
        return "", 400

if __name__ == '__main__':
    app.run(debug=True, port=3333)