import json
from flask import Blueprint, request, Response

from keep_current_storage.use_cases import request_objects as req
from keep_current_storage.repository.mongo_db_repo import MongoDBRepo
from keep_current_storage.use_cases import document_use_cases as uc
from keep_current_storage.serializers import document_serializer as ser
from keep_current_storage.shared import response_object as res

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

blueprint = Blueprint('document', __name__)

@blueprint.route('/documents', methods=['GET'])
def documents():
    qrystr_params = {
        'filters': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_object = req.DocumentListRequestObject.from_dict(qrystr_params)

    repo = MongoDBRepo()
    use_case = uc.DocumentListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.DocumentEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])

@blueprint.route('/document', methods=['POST'])
def document():
    if (isinstance(request.json, str)):
        dict = json.loads(request.json)
    else:
        dict = request.json

    request_object = req.DocumentInsertRequestObject.from_dict(dict)

    repo = MongoDBRepo()
    use_case = uc.DocumentInsertUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.DocumentEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])