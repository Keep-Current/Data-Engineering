import pytest

from keep_current_storage.shared.domain_model import DomainModel
from keep_current_storage.domain.document import Document
from keep_current_storage.repository import memrepo

document_1 = { 
        'id' : 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        'url' :  'https://arxiv.org/pdf/1606.04155.pdf'
        }

document_2 = {
        'id' : 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
        'url' : 'https://arxiv.org/pdf/1506.08941.pdf'
        }

document_3 = {
        'id' : '913694c6-435a-4366-ba0d-da5334a611b2',
        'url' : 'https://arxiv.org/pdf/1705.09655v2.pdf'
        }

@pytest.fixture
def documents():
    return [document_1, document_2, document_3]

def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.id for dm in domain_models_list]) == set([d['id'] for d in data_list])

def test_repository_list_without_parameters(documents):
    repo = memrepo.MemRepo(documents)
    assert repo.list() == documents

def test_repository_list_with_filters_unknown_key(documents):
    repo = memrepo.MemRepo(documents)

    with pytest.raises(KeyError):
        repo.list(filters={'name': 'aname'})

def test_repository_list_with_filters_unknown_operator(documents):
    repo = memrepo.MemRepo(documents)

    with pytest.raises(ValueError):
        repo.list(filters={'id__in': [20, 30]})

def test_repository_list_with_filters_id(documents):
    repo = memrepo.MemRepo(documents)

    _check_results(repo.list(filters={'id': 'f853578c-fc0f-4e65-81b8-566c5dffa35a'}), [document_1])
    _check_results(repo.list(filters={'id__eq': 'f853578c-fc0f-4e65-81b8-566c5dffa35a'}), [document_1])

def test_repository_insert(documents):
    repo = memrepo.MemRepo(documents)
    len1 = len(repo.list())
    
    document1 = {
        'id' : '1111-2222',
        'url' : 'https://arxiv.org/pdf/1705.09655v2.pdf'
        }

    repo.insert_document(document1)
    len2 = len(repo.list())
    assert len2 == len1 + 1
