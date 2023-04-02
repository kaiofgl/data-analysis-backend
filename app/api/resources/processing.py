from flask import Blueprint, jsonify, request, make_response

# Services
from api.services.processing import ProcessingService

processing_blueprint = Blueprint(name='processing', import_name=__name__)

ProcessingService = ProcessingService()

@processing_blueprint.route('single', methods=['POST'])
def single():
    data = request.json
    result = ProcessingService.single(data['filename'], data['column'], data['normalize'])
    if not result:
        return jsonify("An error has ocurred"), 404

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200

@processing_blueprint.route('double', methods=['POST'])
def double():
    data = request.json
    result = ProcessingService.double(data['filename'], data['first_column'], data['second_column'])
    if not result:
        return jsonify("An error has ocurred"), 404

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200

@processing_blueprint.route('structure', methods=['POST'])
def structure():
    data = request.json
    result = ProcessingService.structure(data['filename'])
    if not result:
        return jsonify("An error has ocurred"), 400

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200

@processing_blueprint.route('pre-structure', methods=['POST'])
def preStructure():
    file = request.files['file']

    result = ProcessingService.preStructure(file)

    if not result:
        return jsonify("An error has ocurred"), 400

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return result, 200

@processing_blueprint.route('pre-structure/column', methods=['POST'])
def columnPreProcessing():
    file = request.files['file']
    column = request.form['column'];

    result = ProcessingService.columnPreProcessing(file, column)

    if not result:
        return jsonify("An error has ocurred"), 400

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200