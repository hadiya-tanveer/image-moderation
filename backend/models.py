import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

tokens_collection = db.tokens
usages_collection = db.usages

def is_valid_token(token: str) -> dict:
    """Return token data if valid, else None."""
    return tokens_collection.find_one({"token": token})

def log_usage(token: str, endpoint: str):
    usages_collection.insert_one({
        "token": token,
        "endpoint": endpoint,
        "timestamp": datetime.utcnow()
    })

def create_token(token: str, is_admin=False):
    tokens_collection.insert_one({
        "token": token,
        "isAdmin": is_admin,
        "createdAt": datetime.utcnow()
    })

def delete_token(token: str):
    tokens_collection.delete_one({"token": token})

def get_all_tokens():
    return list(tokens_collection.find({}, {"_id": 0}))
