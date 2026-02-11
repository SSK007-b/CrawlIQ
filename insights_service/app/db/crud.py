from datetime import datetime
from app.db.client import get_collection
import os

COLLECTION_NAME = os.getenv("INSIGHTS_MONGO_COLLECTION", "product_insights")

collection = get_collection(COLLECTION_NAME)


def save_insight(data: dict):
    data["analyzed_at"] = datetime.utcnow()
    result = collection.insert_one(data)
    return str(result.inserted_id)


def get_insights_by_id(id: str):
    return collection.find_one({"_id": id})