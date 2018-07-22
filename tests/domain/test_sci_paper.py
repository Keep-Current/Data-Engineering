import uuid
from keep_current_storage.domain.sci_paper import SciPaper

test_url = 'https://arxiv.org/pdf/1606.04155.pdf'
test_title = 'Rationalizing Neural Predictions'
test_content = '''Abstract
Prediction without justification has limited ap-
plicability.'''
test_abstract = 'The use of relevant metrics of software systems could improve various software engineering tasks, but'
test_authors = ['Maral Azizi', 'Hyunsook Do']
test_publish_date = 'Sat, 20 Jan 2018 00:11:42'
test_pdf_url = 'https://arxiv.org/pdf/1801.06605'

def test_document_model_init():
    id = uuid.uuid4()
    document = SciPaper(
        id,
        url = test_url,
        title = test_title,
        content = test_content,
        abstract = test_abstract,
        authors = test_authors,
        pdf_url = test_pdf_url,
        publish_date = test_publish_date
        )
    assert document.id ==  id
    assert document.url == test_url
    assert document.title == test_title
    assert document.content == test_content
    assert document.authors == test_authors
    assert document.abstract == test_abstract
    assert document.pdf_url == test_pdf_url
    assert document.publish_date == test_publish_date


def test_document_model_from_dict():
    id = uuid.uuid4()
    document = SciPaper.from_dict(
        {
            'id' : id,
            'url': test_url,
            'title': test_title,
            'content': test_content,
            'abstract' : test_abstract,
            'authors' : test_authors,
            'pdf_url' : test_pdf_url,
            'publish_date' : test_publish_date
        }
    )

    assert document.id == id
    assert document.url == test_url
    assert document.title == test_title
    assert document.content == test_content
    assert document.authors == test_authors
    assert document.abstract == test_abstract
    assert document.pdf_url == test_pdf_url
    assert document.publish_date == test_publish_date
