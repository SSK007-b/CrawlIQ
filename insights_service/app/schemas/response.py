from pydantic import BaseModel
from datetime import datetime

class InsightResponse(BaseModel):
    id: str
    summary: dict
    query: str
    insights: str
    analyzed_at: datetime