import httpx
from fastapi import APIRouter
from app.schemas.request import APIRequest
from app.schemas.response import APIResponse


router = APIRouter()

@router.post("/api/orchestrator/post", response_model=APIResponse)
async def scrape_data(payload: APIRequest):

    async with httpx.AsyncClient(timeout=60.0) as client:
        scraper_response = await client.post(
            "http://scraper:8000/api/scrape/post",
            json={"url": str(payload.url)}
        )

        print(f"The Scraper Response is {scraper_response.json()}")

        insight_response = await client.post(
            "http://insights:8000/api/insight/post",
            json={"summary": scraper_response.json(), "query": payload.query}
        )

        print(f"The insight response is {insight_response.json()}")
        data = insight_response.json()
        data['url'] = payload.url
    return data
