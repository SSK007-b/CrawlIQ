from pydantic import BaseModel

class InsightRequest(BaseModel):
    summary: dict
    query: str