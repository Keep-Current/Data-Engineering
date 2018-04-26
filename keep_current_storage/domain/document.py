from keep_current_storage.shared.domain_model import DomainModel

class Document(object):

    def __init__(self, id, url):
        self.id = id
        self.url = url

    @classmethod
    def from_dict(cls, adict):
        document = Document(
            id=adict['id'],
            url=adict['url'],
        )

        return document


DomainModel.register(Document)