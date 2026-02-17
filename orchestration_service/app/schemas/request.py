from pydantic import BaseModel, HttpUrl

class APIRequest(BaseModel):
    url: HttpUrl
    query: str