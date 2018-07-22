from keep_current_storage.shared import use_case as uc
from keep_current_storage.shared import response_object as res


class TopicListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_topic = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_topic)

class TopicInsertUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.insert_topic(request_object.topic)
        return res.ResponseSuccess()
