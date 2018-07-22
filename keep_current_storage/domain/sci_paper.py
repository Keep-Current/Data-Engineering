from keep_current_storage.shared.domain_model import DomainModel
from keep_current_storage.domain.document import Document

class SciPaper(Document):

    def __init__(self, id, url, title, content,
        abstract, authors, publish_date, pdf_url
    ):
        super(SciPaper, self).__init__(id, url, title, content)
        self.abstract = abstract
        self.authors = authors
        self.publish_date = publish_date
        self.pdf_url = pdf_url

    @classmethod
    def from_dict(cls, adict):
        sci_paper = SciPaper(
            id=adict['id'],
            url=adict['url'],
            title=adict['title'],
            content=adict['content'],
            abstract=adict['abstract'],
            authors=adict['authors'],
            publish_date=adict['publish_date'],
            pdf_url=adict['pdf_url']
        )

        return sci_paper


DomainModel.register(Document)