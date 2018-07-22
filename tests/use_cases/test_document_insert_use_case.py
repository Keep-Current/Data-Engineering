import pytest
from unittest import mock

from keep_current_storage.domain.document import Document
from keep_current_storage.use_cases import request_objects as ro
from keep_current_storage.use_cases import document_use_cases as uc
from keep_current_storage.shared import response_object as res

def test_document_insert_valid_json():
    repo = mock.Mock()
    repo.insert_document.return_value = None
    document_insert_use_case = uc.DocumentInsertUseCase(repo)
    document_1_dict = {
        'id' : '1111-11111-22222',
        'url' :  'https://arxiv.org/pdf/12345.pdf'
    }
    request_object = ro.RequestObject.from_dict(document_1_dict)
    response_object = document_insert_use_case.execute(request_object)

    repo.insert_document.assert_called_with(document_1_dict)
    assert bool(response_object) is True
    

def test_document_insert_invalid_json_id():
    repo = mock.Mock()
    repo.insert_document.return_value = None
    document_insert_use_case = uc.DocumentInsertUseCase(repo)
    document_1_dict = {
        '_id_' : '1111-11111-22222',
        'url' :  'https://arxiv.org/pdf/12345.pdf'
    }
    request_object = ro.RequestObject.from_dict(document_1_dict)
    response_object = document_insert_use_case.execute(request_object)

    repo.insert_document.assert_not_called()
    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "id: not provided"
    }

def test_document_insert_invalid_json_url():
    repo = mock.Mock()
    repo.insert_document.return_value = None
    document_insert_use_case = uc.DocumentInsertUseCase(repo)
    document_1_dict = {
        'id' : '1111-11111-22222',
        '_url_' :  'https://arxiv.org/pdf/12345.pdf'
    }
    request_object = ro.RequestObject.from_dict(document_1_dict)
    response_object = document_insert_use_case.execute(request_object)

    repo.insert_document.assert_not_called()
    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "url: not provided"
    }