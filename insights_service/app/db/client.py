import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
MONGO_DB = os.getenv("MONGO_DB", "insights_db")

# Create Mongo Client
client = MongoClient(MONGO_URI)

# Select Database
database = client[MONGO_DB]

def get_collection(collection_name: str):
    return database[collection_name]