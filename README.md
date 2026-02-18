# CrawlIQ
## AI-Powered Competitor Intelligence & Product Insight Engine

CrawlIQ is a multi-agent AI system that helps Product Owners and Company Leaders analyze competitor product pages and generate actionable strategic insights.

It combines web scraping and AI-driven analysis through a clean orchestration layer, exposed as a service and visualized via a Streamlit MVP interface.

## Problem It Solves
**In competitive markets, product leaders need to:**
- Understand competitor positioning
- Extract insights from product pages
- Identify differentiation opportunities
- Improve feature strategy

Manually doing this is slow and inconsistent.
*CrawlIQ automates this workflow using AI agents.*

## Core Components
**Scraper Agent**

*Responsible for:*
- Fetching competitor product pages
- Cleaning and structuring webpage content
- Returning structured text data

EndPoint
```bash
    POST /api/scrape/post
```
Input
```bash
{
  "url": "https://competitor.com/product"
}
```

## Insights Agent
**Responsible for:**
- Analyzing structured competitor content
- Processing strategic queries
- Generating differentiation strategies and recommendations

Endpoint
```bash
    POST /api/insight/post
```
Input
```bash
{
  "summary": {"...cleaned text..."},
  "query": "How can we differentiate our product?"
}
```

## Orchestrator Service
*Acts as a unified AI workflow engine.*

**Flow:**
- Calls Scraper Agent
- Passes structured output to Insights Agent
- Returns final strategic analysis

Endpoint
```bash
    POST /api/orchestration/post
```
Input
```bash
{
  "url": "https://competitor.com/product",
  "query": "What unique features should we introduce?"
}
```

## Streamlit MVP Interface
**The Streamlit frontend allows users to:**
- Enter competitor product URL
- Provide strategic query
- Trigger execution
- View structured AI-generated insights

This acts as the MVP layer and can later be replaced with React or another frontend framework.

## Project Structure

```bash
CrawlIQ/
│
├── docker-compose.yml
│
├── scraper_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── core/
│       ├── db/
│       ├── routers/
│       ├── schema/
│       └── service/
│
├── insights_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── core/
│       ├── db/
│       ├── routers/
│       ├── schema/
│       └── service/
│
├── orchestrator_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── core/
│       ├── routers/
│       ├── schema/
│       └── service/
│
├── app.py                  # Streamlit MVP
├── .env.example
└── requirements.txt
```

## Running with Docker

Build and run all services:
```bash
    docker-compose up --build
```

## Tech Stack
- Python 3.11+
- FastAPI
- Pydantic
- HTTPX (Async API calls)
- Streamlit
- Docker & Docker Compose

## Engineering Highlights
**CrawlIQ demonstrates:**
- Multi-agent architecture
- Service-to-service communication
- Asynchronous orchestration
- Clean separation of concerns
- MVP-ready AI service design
- Microservice-based system architecture

## Future Enhancements
- Multi-competitor comparison
- Feature gap analysis engine
- SWOT auto-generation
- AI-powered market positioning suggestions
- Agent registry pattern
- JWT authentication
- Observability & monitoring
- Cloud deployment (AWS/GCP/Azure)

## Ideal Users
- Startup Founders
- Product Managers
- Strategy Teams
- Competitive Intelligence Analysts

## Vision
CrawlIQ aims to evolve into a full AI-powered Product Strategy Engine that transforms competitor data into structured, actionable product decisions.