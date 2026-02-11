import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


class Gemini_Client:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=os.getenv("GEMINI_MODEL_NAME"), api_key=os.getenv("GEMINI_API_KEY")
        )

    def prompt(self, summary: dict, query: str):
        prompt = f"""
            You are a senior Product Strategy Consultant and Competitive Intelligence Analyst.

            Your task is to analyze competitor product summaries and generate strategic, actionable, and market-driven business insights.

            OBJECTIVE:
            Help the organization strengthen market position, improve product differentiation, and identify high-impact enhancements based on competitor analysis and the provided query.

            INPUT:
            Competitor Summary:
            {summary}

            Business Query:
            {query}

            ANALYSIS INSTRUCTIONS:
            1. Identify competitor strengths and positioning patterns.
            2. Detect feature gaps, market gaps, or unmet customer needs.
            3. Highlight differentiation opportunities.
            4. Suggest high-impact product enhancements.
            5. Recommend strategic positioning moves (pricing, features, UX, integrations, AI usage, etc.).
            6. Focus on practical, implementable actions — not generic advice.
            7. Be specific, strategic, and business-oriented.

            OUTPUT RULES:
            - Return STRICT JSON only.
            - No explanations outside JSON.
            - No markdown.
            - No extra commentary.
            - Each insight must be concise but action-oriented.
            - Each recommendation should start with a strategic verb (e.g., "Introduce", "Leverage", "Differentiate", "Optimize", "Expand", "Position", "Bundle").

            OUTPUT FORMAT:
            {{
                "market_summary": "High-level competitive landscape insight in 2-3 sentences",
                "key_gaps_identified": [
                    "Gap 1",
                    "Gap 2"
                ],
                "strategic_recommendations": [
                    "Introduce ...",
                    "Differentiate ...",
                    "Leverage ..."
                ],
                "quick_wins": [
                    "Short-term action 1",
                    "Short-term action 2"
                ],
                "long_term_moves": [
                    "Long-term strategic move 1",
                    "Long-term strategic move 2"
                ]
            }}
            """
        return prompt
    
    def generate_insights(self, payload):
        summary, query = payload.summary, payload.query
        prompt = self.prompt(summary, query)
        response = self.model.invoke(prompt)
        print(f"The response is {response.content}")
        return {"summary": summary, "query": query, "insights": str(response.content)}