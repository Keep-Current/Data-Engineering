import json

from keep_current_storage.serializers import topic_serializer as srs
from keep_current_storage.domain.topic import Topic


def test_serialize_domain_topic():
    topic = Topic('f853578c-fc0f-4e65-81b8-566c5dffa35a',
                user_id='user_andrew_ng_1234',
                name = 'NLP - chatbots')

    expected_json = """
        {
            "id" : "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "user_id" : "user_andrew_ng_1234",
            "content" : "NLP - chatbots"
        }
    """
    
    assert json.loads(json.dumps(topic, cls=srs.TopicEncoder)) == json.loads(expected_json)