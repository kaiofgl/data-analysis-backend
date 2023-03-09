from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Import routes
from api.resources import file_blueprint

app.register_blueprint(file_blueprint, url_prefix="/api/v1/file");

@app.route('/heath', methods=['GET'])
def index():
    return 'ok', 200

# CORS(app)
# @app.route('/file', methods=['POST'])
# def file():
#     data = request.json
#     file = getFile(data)
#     if(file):
#         return file
#     else:
#         return "", 400

# CORS(app)
# @app.route('/processing', methods=['POST'])
# def structure():
#     data = request.json
#     structure = getStructure(data)
#     if(structure):
#         return sequalizeData(structure)
#     else:
#         return "", 400

# if __name__ == '__main__':
#     app.run(debug=True, port=3333)