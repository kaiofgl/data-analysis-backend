from flask import Blueprint, jsonify, request, make_response

# Services
from api.services.processing import ProcessingService

processing_blueprint = Blueprint(name='processing', import_name=__name__)

ProcessingService = ProcessingService()

@processing_blueprint.route('single', methods=['POST'])
def single():
    data = request.json
    result = ProcessingService.single(data['filename'], data['column'])
    if not result:
        return jsonify("An error has ocurred"), 404

    response = make_response(result)
    response.headers['Content-Type'] = 'application/json'
    return response, 200