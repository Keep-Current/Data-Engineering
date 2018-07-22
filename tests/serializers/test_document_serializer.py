import json

from keep_current_storage.serializers import document_serializer as srs
from keep_current_storage.domain.document import Document


def test_serialize_domain_document():
    document = Document('f853578c-fc0f-4e65-81b8-566c5dffa35a',
                        url='https://arxiv.org/pdf/1606.04155.pdf',
                        title = 'Rationalizing Neural Predictions',
                        content = '''Abstract
Prediction without justification has limited ap-
plicability. ''')

    expected_json = """
        {
            "id" : "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "url" : "https://arxiv.org/pdf/1606.04155.pdf",
            "title" : "Rationalizing Neural Predictions",
            "content" : "Abstract
Prediction without justification has limited ap-
plicability. "
        }
    """
    
    assert json.loads(json.dumps(document, cls=srs.DocumentEncoder)) == json.loads(expected_json)