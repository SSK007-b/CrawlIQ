from fastapi import APIRouter
from app.schemas.request import InsightRequest
from app.schemas.response import InsightResponse
from app.services.gemini_client import Gemini_Client
from app.db.crud import save_insight, get_insights_by_id
from datetime import datetime

router = APIRouter()

@router.post("/api/insight/post", response_model=InsightResponse)
def scrape_data(payload: InsightRequest):

    insight = Gemini_Client()
    data = insight.generate_insights(payload)
    data["analyzed_at"] = datetime.utcnow()
    data["id"] = save_insight(data)

    return data

@router.post("/api/insight/get", response_model=InsightResponse)
def get_scraped_data(payload: str):
    data = get_insights_by_id(payload)
    print("The Data id is: ", data["_id"])
    data["id"] = str(data["_id"])
    return data