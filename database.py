import pymongo
import json

def mongo_connect(db_host: str=None, db_port: int=27017):

    if db_host is None:
        with open('config.json') as f:
            config = json.load(f)
            db_host = config['db_host']
            db_port = config['db_port']

    mongo_client = pymongo.MongoClient(f"mongodb://{db_host}:{db_port}/")
    return mongo_client

def get_database(client, db_name):
    return client[db_name]

