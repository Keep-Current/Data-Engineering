import uuid
from keep_current_storage.domain.document import Document


def test_document_model_init():
    id = uuid.uuid4()
    document = Document(id, url = 'https://arxiv.org/pdf/1606.04155.pdf')
    assert document.id ==  id
    assert document.url == 'https://arxiv.org/pdf/1606.04155.pdf'


def test_document_model_from_dict():
    id = uuid.uuid4()
    document = Document.from_dict(
        {
            'id' : id,
            'url': 'https://arxiv.org/pdf/1606.04155.pdf'
        }
    )

    assert document.id == id
    assert document.url == 'https://arxiv.org/pdf/1606.04155.pdf'