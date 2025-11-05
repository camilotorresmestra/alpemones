from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()
username = quote_plus(os.getenv("MONGODB_USERNAME", "grupo5_mdd"))
password = quote_plus(os.getenv("MONGODB_PASSWORD"))
host = "172.24.98.13"
port = 27017
db_name = "alpemones_G05"
auth_db = "admin"

CONNECTION_STRING = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource={auth_db}"
DATABASE_NAME = db_name

PLAYERS_COLLECTION = "players"
BATTLES_COLLECTION = "battles"
   

def get_alpemons_by_type(username: str, type_name: str):
    """
    Return list of alpemons of `type_name` for user `username` using aggregation ($filter).
    """
    pipeline = [
        {"$match": {"name": username}},
        {"$project": {
            "_id": 0,
            "alpemons": {
                "$filter": {
                    "input": "$alpemons",
                    "as": "a",
                    "cond": {"$eq": ["$$a.type", type_name]}
                }
            }
        }}
    ]
    #TODO: return the aggregation cursor or the list of documents???
    docs = players.aggregate(pipeline)
    return docs

if __name__ == "__main__":
    with MongoClient(CONNECTION_STRING) as client:
        db = client[DATABASE_NAME]
        players = db[PLAYERS_COLLECTION]
        battles = db[BATTLES_COLLECTION]
        
        print("Connected to database:", DATABASE_NAME)
        print("Collections:", db.list_collection_names())

