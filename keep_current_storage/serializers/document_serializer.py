import json


class DocumentEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'id': o.id,
                'url': o.url
            }
            return to_serialize
        except AttributeError:
            return super().default(o)