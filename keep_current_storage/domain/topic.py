from keep_current_storage.shared.domain_model import DomainModel

class Topic(object):

    def __init__(self, id, user_id, name):
        self.id = id
        self.user_id = user_id
        self.name = name

    @classmethod
    def from_dict(cls, adict):
        topic = Topic(
            id=adict['id'],
            user_id=adict['user_id'],
            name=adict['name'],
        )

        return topic


DomainModel.register(Topic)