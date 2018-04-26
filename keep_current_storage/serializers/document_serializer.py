import json
import bson

class DocumentEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            if isinstance(o, bson.ObjectId):
                return str(o)
            to_serialize = {
                'id': o.id,
                'url': o.url
            }
            return to_serialize
        except AttributeError:
            return super().default(o)