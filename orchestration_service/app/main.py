from fastapi import FastAPI
from app.routers import orchestration

app = FastAPI(title="Insight Scraper Service")

app.include_router(orchestration.router)