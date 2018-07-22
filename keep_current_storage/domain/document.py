from keep_current_storage.shared.domain_model import DomainModel

class Document(object):

    def __init__(self, id, url, title, content):
        self.id = id
        self.url = url
        self.title = title
        self.content = content

    @classmethod
    def from_dict(cls, adict):
        document = Document(
            id=adict['id'],
            url=adict['url'],
            title=adict['title'],
            content=adict['content'],
        )

        return document


DomainModel.register(Document)