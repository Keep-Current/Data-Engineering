import json
import bson

class TopicEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            if isinstance(o, bson.ObjectId):
                return str(o)
            to_serialize = {
                'id': o.id,
                'user_id': o.user_id,
                'name': o.name
            }
            return to_serialize
        except AttributeError:
            return super().default(o)