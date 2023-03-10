from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)

# Import routes
from api.resources import file_blueprint
from api.resources import processing_blueprint

CORS(app)
app.register_blueprint(file_blueprint, url_prefix="/api/v1/file");
app.register_blueprint(processing_blueprint, url_prefix="/api/v1/processing");


@app.route('/health', methods=['GET'])
def index():
    return 'ok', 200
