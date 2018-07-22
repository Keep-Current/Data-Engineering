from keep_current_storage.use_cases import request_objects as ro


def test_build_document_list_request_object_without_parameters():
    req = ro.RequestObject()

    assert req.filters is None
    assert bool(req) is True

def test_build_document_list_request_object_from_empty_dict():
    req = ro.RequestObject.from_dict({})

    assert req.filters is None
    assert bool(req) is True

def test_build_document_list_request_object_with_empty_filters():
    req = ro.RequestObject(filters={})

    assert req.filters == {}
    assert bool(req) is True


def test_build_document_list_request_object_from_dict_with_empty_filters():
    req = ro.RequestObject.from_dict({'filters': {}})

    assert req.filters == {}
    assert bool(req) is True


def test_build_document_list_request_object_with_filters():
    req = ro.RequestObject(filters={'a': 1, 'b': 2})

    assert req.filters == {'a': 1, 'b': 2}
    assert bool(req) is True


def test_build_document_list_request_object_from_dict_with_filters():
    req = ro.RequestObject.from_dict({'filters': {'a': 1, 'b': 2}})

    assert req.filters == {'a': 1, 'b': 2}
    assert bool(req) is True


def test_build_document_list_request_object_from_dict_with_invalid_filters():
    req = ro.RequestObject.from_dict({'filters': 5})

    assert req.has_errors()
    assert req.errors[0]['parameter'] == 'filters'
    assert bool(req) is False