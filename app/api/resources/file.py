from flask import Blueprint, jsonify, request, make_response

# Services
from api.services.file import FileService

file_blueprint = Blueprint(name='file', import_name=__name__)

FileService = FileService()

@file_blueprint.route('upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = request.form["name"]

    result = FileService.upload(file, filename)

    if not result:
        return jsonify("An error has ocurred"), 404

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200

@file_blueprint.route('get', methods=['POST'])
def get():
    data = request.json
    result = FileService.getFile(data['filename'])
    if not result:
        return jsonify("An error has ocurred"), 404
    return jsonify(result), 200

def structure():
    data = request.json
    result = FileService.structure(data['filename'])
    if not result:
        return jsonify("An error has ocurred"), 404
    return jsonify(result), 200