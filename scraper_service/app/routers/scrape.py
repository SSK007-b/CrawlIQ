from fastapi import APIRouter
from app.schemas.request import ScrapeRequest
from app.schemas.response import ScrapeGetResponse, ScrapePostResponse
from app.services.generic_scraper import GenericScraper
from app.db.crud import save_product, get_product_by_url
from datetime import datetime

router = APIRouter()

@router.post("/api/scrape/post", response_model=ScrapePostResponse)
def scrape_data(payload: ScrapeRequest):

    scraper = GenericScraper(payload.url)
    data = scraper.extract()
    data["url"] = str(data["url"]) 
    data["scraped_at"] = datetime.utcnow()

    save_product(data)

    return data

@router.post("/api/scrape/get", response_model=ScrapeGetResponse)
def get_scraped_data(payload: str):
    data = get_product_by_url(payload)
    print("The Data id is: ", data["_id"])
    data["id"] = str(data["_id"])
    return data