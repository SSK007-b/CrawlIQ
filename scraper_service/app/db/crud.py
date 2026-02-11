from datetime import datetime
from app.db.client import get_collection
import os

COLLECTION_NAME = os.getenv("SCRAPER_MONGO_COLLECTION", "scraped_products")

collection = get_collection(COLLECTION_NAME)


def save_product(data: dict):
    """
    Save scraped product into MongoDB.
    If URL already exists, update it.
    """
    data["scraped_at"] = datetime.utcnow()

    existing = collection.find_one({"url": data["url"]})

    if existing:
        collection.update_one(
            {"url": data["url"]},
            {"$set": data}
        )
        return "updated"
    else:
        collection.insert_one(data)
        return "inserted"


def get_product_by_url(url: str):
    return collection.find_one({"url": url})