from fastapi import FastAPI
from app.routers import insight
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="Insight Scraper Service")

app.include_router(insight.router)