from keep_current_storage.domain.document import Document
from pymongo import MongoClient
import databaseconfig as cfg


class MongoDBRepo:        

    def _checkFilter(self, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        return key, operator

    def list(self, filters=None):
        self._client = MongoClient(cfg.mongo_db['connection_string'])
        parsed_filter = {}

        for key, value in filters.items():            
            key, _ = self._checkFilter(key, value)
            parsed_filter[key] = value
            
        db = self._client.keep_current
        documents = db.Documents
        cursor = documents.find(parsed_filter)
        result = []
        for document in cursor:
            result.append(document)

        return result

    def insert_document(self, document):
        self._client = MongoClient(cfg.mongo_db['connection_string'])
        db = self._client.keep_current
        documents = db.Documents
        documents.insert_one(document)