from pydantic import BaseModel
from datetime import datetime

class ScrapeGetResponse(BaseModel):
    id: str
    url: str
    product_name: str
    cleaned_text: str
    scraped_at: datetime

class ScrapePostResponse(BaseModel):
    url: str
    product_name: str
    cleaned_text: str
    scraped_at: datetime