import os

# mongo_db = { 'connection_string': 'your_mongo_connection_string' }
mongo_db = { 'connection_string': os.environ['MONGO_CONNECTION_STRING']}