import json
from unittest import mock
from keep_current_storage.shared import response_object as res

document_1_dict = { "id" : "f853578c-fc0f-4e65-81b8-566c5dffa35a", "url" :  "https://arxiv.org/pdf/1606.04155.pdf" }



@mock.patch('keep_current_storage.use_cases.document_use_cases.DocumentInsertUseCase')
def test_post(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess()
    http_response = client.post('/document', data = json.dumps(document_1_dict), content_type='application/json', charset='UTF-8')
    assert http_response.status_code == 200

