import os

# mongo_db = { 'connection_string': 'your_mongo_connection_string' }
try:
    mongo_conn_string = os.environ['MONGO_CONNECTION_STRING']
except KeyError:
    mongo_conn_string = 'SET_YOUR_MONGO_DB_CONN_STRING'

mongo_db = { 'connection_string': mongo_conn_string }
