from fastapi import FastAPI
from app.routers import scrape
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="Insight Scraper Service")

app.include_router(scrape.router)