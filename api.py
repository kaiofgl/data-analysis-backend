from flask import Flask, request, jsonify
# from flask_limiter import Limiter
# from flask_limiter.util import get_remote_address
import json
from main import getJsonFromFile;

app = Flask(__name__)
# limiter = Limiter(app, key_func=get_remote_address)

# @limiter.limit("10 per minute")
@app.route('/heath', methods=['GET'])
def index():
    return 'ok', 200

@app.route('/getFromJson', methods=['GET'])
def getFromJson():
    getJson = getJsonFromFile();
    return json.loads(getJson) 

if __name__ == '__main__':
    app.run(debug=True, port=3333)