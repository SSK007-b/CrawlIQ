from pydantic import BaseModel, HttpUrl

class APIResponse(BaseModel):
    url: HttpUrl
    summary: dict
    query: str
    insights: str