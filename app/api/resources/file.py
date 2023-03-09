from flask import Blueprint, jsonify, request

# Services
from api.services.file import FileService

file_blueprint = Blueprint(name='debug', import_name=__name__)

FileService = FileService()

@file_blueprint.route('upload', methods=['POST'])
def upload():
    return "", 200
    # file = request.files['file']
    # response = uploadFile(file);
    # if(response):
    #     return "", 200
    # else:
    #     return "", 400

@file_blueprint.route('get', methods=['POST'])
def get():
    data = request.json
    result = FileService.getFile(data['filename'])
    if not result:
        return jsonify("An error has ocurred"), 404
    return jsonify(result), 200
    # data = request.json
    # file = getFile(data)
    # if(file):
    #     return file
    # else:
    #     return "", 400