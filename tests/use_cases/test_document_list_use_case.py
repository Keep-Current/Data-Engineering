import pytest
from unittest import mock

from keep_current_storage.domain.document import Document
from keep_current_storage.use_cases import request_objects as ro
from keep_current_storage.use_cases import document_use_cases as uc
from keep_current_storage.shared import response_object as res


@pytest.fixture
def domain_documents():
    document_1 = Document(
        id='f853578c-fc0f-4e65-81b8-566c5dffa35a',
        url =  'https://arxiv.org/pdf/1606.04155.pdf',
        title = 'Rationalizing Neural Predictions',
        content = '''Abstract
Prediction without justification has limited ap-
plicability. '''
    )

    document_2 = Document(
        id='fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        url = 'https://arxiv.org/pdf/1506.08941.pdf',
        title = 'Language Understanding for Text-based Games using Deep Reinforcement Learning',
        content = '''Abstract
In this paper, we consider the task of learn-
ing control policies for text-based games.
In these games, all interactions in the vir-
tual  world  are  through  text  and  the  un-
derlying  state  is  not  observed.  '''
    )

    document_3 = Document(
        id='913694c6-435a-4366-ba0d-da5334a611b2',
        url = 'https://arxiv.org/pdf/1705.09655v2.pdf',
        title = 'Style Transfer from Non-Parallel Text by Cross-Alignment',
        content = '''Abstract
This paper focuses on style transfer on the basis of non-parallel text. '''
    )

    return [document_1, document_2, document_3]


def test_document_list_without_parameters(domain_documents):
    repo = mock.Mock()
    repo.list.return_value = domain_documents

    document_list_use_case = uc.DocumentListUseCase(repo)
    request_object = ro.RequestObject.from_dict({})

    response_object = document_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == domain_documents

def test_document_list_with_filters(domain_documents):
    repo = mock.Mock()
    repo.list.return_value = domain_documents

    document_list_use_case = uc.DocumentListUseCase(repo)
    qry_filters = {'a': 5}
    request_object = ro.RequestObject.from_dict({'filters': qry_filters})

    response_object = document_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_documents

def test_document_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    document_list_use_case = uc.DocumentListUseCase(repo)
    request_object = ro.RequestObject.from_dict({})

    response_object = document_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_document_list_handles_bad_request():
    repo = mock.Mock()

    document_list_use_case = uc.DocumentListUseCase(repo)
    request_object = ro.RequestObject.from_dict({'filters': 5})

    response_object = document_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'message': "filters: Is not iterable"
    }