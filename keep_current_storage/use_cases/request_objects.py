import collections


class InvalidRequestObject(object):

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        return False

    __bool__ = __nonzero__


class ValidRequestObject(object):

    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    __bool__ = __nonzero__


class DocumentListRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return DocumentListRequestObject(filters=adict.get('filters', None))

class DocumentInsertRequestObject(ValidRequestObject):

    def __init__(self, document=None):
        self.document = document

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'id' not in adict:
            invalid_req.add_error('id', 'not provided')

        if 'url' not in adict: 
            invalid_req.add_error('url', 'not provided')

        if invalid_req.has_errors():
            return invalid_req

        return DocumentInsertRequestObject(document=adict)