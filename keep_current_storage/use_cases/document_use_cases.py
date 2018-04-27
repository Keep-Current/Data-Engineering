from keep_current_storage.shared import use_case as uc
from keep_current_storage.shared import response_object as res


class DocumentListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        domain_document = self.repo.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_document)

class DocumentInsertUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        self.repo.insert_document(request_object.document)
        return res.ResponseSuccess()