import uuid
from keep_current_storage.domain.document import Document

test_url = 'https://arxiv.org/pdf/1606.04155.pdf'
test_title = 'Rationalizing Neural Predictions'
test_content = '''Abstract
Prediction without justification has limited ap-
plicability. '''

def test_document_model_init():
    id = uuid.uuid4()
    document = Document(
        id,
        url = test_url,
        title = test_title,
        content = test_content
        )
    assert document.id ==  id
    assert document.url == test_url
    assert document.title == test_title
    assert document.content == test_content


def test_document_model_from_dict():
    id = uuid.uuid4()
    document = Document.from_dict(
        {
            'id' : id,
            'url': test_url,
            'title': test_title,
            'content': test_content
        }
    )

    assert document.id == id
    assert document.url == test_url
    assert document.title == test_title
    assert document.content == test_content