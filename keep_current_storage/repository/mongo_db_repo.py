from keep_current_storage.domain.document import Document
from pymongo import MongoClient
import databaseconfig as cfg


class MongoDBRepo:

    def __init__(self):
        self._client = MongoClient(cfg.mongo_db['connection_string'])

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)
        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        db = self._client.keep_current
        documents = db.Documents
        cursor = documents.find({})
        result = []
        for document in cursor:
            result.append(document)

        return result