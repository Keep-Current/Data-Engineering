import collections
from keep_current_storage.shared import request_object as req

class DocumentListRequestObject(req.ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return DocumentListRequestObject(filters=adict.get('filters', None))

class DocumentInsertRequestObject(req.ValidRequestObject):

    def __init__(self, document=None):
        self.document = document

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if 'id' not in adict:
            invalid_req.add_error('id', 'not provided')

        if 'url' not in adict: 
            invalid_req.add_error('url', 'not provided')

        if invalid_req.has_errors():
            return invalid_req

        return DocumentInsertRequestObject(document=adict)