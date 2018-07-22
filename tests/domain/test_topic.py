import uuid
from keep_current_storage.domain.topic import Topic

test_name = 'NLP - chatbots'
test_user_id = 'user_andrew_ng_12345'

def test_topic_model_init():
    id = uuid.uuid4()
    topic = Topic(
        id,
        user_id = test_user_id,
        name = test_name
        )
    assert topic.id ==  id
    assert topic.user_id == test_user_id
    assert topic.name == test_name


def test_topic_model_from_dict():
    id = uuid.uuid4()
    topic = Topic.from_dict(
        {
            'id' : id,
            'user_id': test_user_id,
            'name': test_name
        }
    )

    assert topic.id == id
    assert topic.name == test_name
    assert topic.user_id == test_user_id