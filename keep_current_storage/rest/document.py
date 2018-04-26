import json
from flask import Blueprint, request, Response

from keep_current_storage.use_cases import request_objects as req
from keep_current_storage.repository import memrepo as mr
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

document_1 =  {
        'id' : 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'url' : 'https://arxiv.org/pdf/1606.04155.pdf'
    }

document_2 = {
        'id' : 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        'url' : 'https://arxiv.org/pdf/1506.08941.pdf'
    }

document_3 = {
        'id' : '913694c6-435a-4366-ba0d-da5334a611b2',
        'url' : 'https://arxiv.org/pdf/1705.09655v2.pdf'
    }

@blueprint.route('/documents', methods=['GET'])
def document():
    qrystr_params = {
        'filters': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_object = req.DocumentListRequestObject.from_dict(qrystr_params)

    repo = mr.MemRepo([document_1, document_2, document_3])
    use_case = uc.DocumentListUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.DocumentEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])