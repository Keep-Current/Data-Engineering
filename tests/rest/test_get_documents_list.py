import json
from unittest import mock

from keep_current_storage.domain.document import Document
from keep_current_storage.shared import response_object as res

document_1_dict = { 
        'id' : 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'url' :  'https://arxiv.org/pdf/1606.04155.pdf',
        'title': 'Rationalizing Neural Predictions',
        'content': '''Abstract
Prediction without justification has limited ap-
plicability. '''
        }

document1_domain_model = Document.from_dict(document_1_dict)

documents = [document1_domain_model]


@mock.patch('keep_current_storage.use_cases.document_use_cases.DocumentListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(documents)

    http_response = client.get('/documents')

    assert json.loads(http_response.data.decode('UTF-8')) == [document_1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'

@mock.patch('keep_current_storage.use_cases.document_use_cases.DocumentListUseCase')
def test_get_failed_response(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseFailure.build_system_error('test message')

    http_response = client.get('/documents')

    assert json.loads(http_response.data.decode('UTF-8')) == {'type': 'SYSTEM_ERROR',
                                                              'message': 'test message'}
    assert http_response.status_code == 500
    assert http_response.mimetype == 'application/json'


@mock.patch('keep_current_storage.use_cases.document_use_cases.DocumentListUseCase')
def test_request_object_initialisation_and_use_with_filters(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess([])
    internal_request_object = mock.Mock()

    request_object_class = 'keep_current_storage.use_cases.request_objects.RequestObject'
    with mock.patch(request_object_class) as mock_request_object:
        mock_request_object.from_dict.return_value = internal_request_object
        client.get('/documents?filter_param1=value1&filter_param2=value2')

    mock_request_object.from_dict.assert_called_with(
        {'filters': {'param1': 'value1', 'param2': 'value2'}}
        )
    
    mock_use_case().execute.assert_called_with(internal_request_object)