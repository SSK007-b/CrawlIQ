import streamlit as st
import requests
import json
from datetime import datetime

# ---------- CONFIG ----------
API_URL = "http://localhost:8000/api/orchestrator/post"

st.set_page_config(
    page_title="AI Market Intelligence Engine",
    page_icon="🚀",
    layout="wide"
)

# ---------- HEADER ----------
st.title("🚀 AI Market Intelligence Engine")
st.markdown("Turn any product website into AI-powered strategic insights.")

# ---------- INPUT SECTION ----------
with st.container():
    col1, col2 = st.columns([2, 3])

    with col1:
        url = st.text_input("🔗 Product URL", placeholder="https://www.notion.com/")
    
    with col2:
        query = st.text_area(
            "💡 Your Business Query",
            placeholder="What AI features should we build to compete?"
        )

    submit = st.button("Generate AI Insights")

# ---------- API CALL ----------
if submit:
    if not url or not query:
        st.warning("Please enter both URL and Query")
    else:
        with st.spinner("Analyzing product & generating strategic insights..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "url": url,
                        "query": query
                    },
                    timeout=120
                )

                if response.status_code == 200:
                    data = response.json()

                    summary = data.get("summary", {})
                    insights_raw = data.get("insights", "{}")
                    insights = json.loads(insights_raw)

                    st.success("Analysis Completed Successfully ✅")

                    # ---------- PRODUCT INFO ----------
                    st.markdown("---")
                    st.header("📌 Product Overview")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("Product Name", summary.get("product_name", "N/A"))
                        st.write("🌐 URL:", summary.get("url"))

                    with col2:
                        scraped_at = summary.get("scraped_at")
                        if scraped_at:
                            dt = datetime.fromisoformat(scraped_at)
                            st.metric("Scraped At", dt.strftime("%d %b %Y %H:%M"))

                    st.markdown("### 📝 Cleaned Summary")
                    st.info(summary.get("cleaned_text", "No summary available"))

                    # ---------- MARKET SUMMARY ----------
                    st.markdown("---")
                    st.header("📊 Market Summary")
                    st.success(insights.get("market_summary", "No summary available"))

                    # ---------- KEY GAPS ----------
                    st.markdown("---")
                    st.header("🔍 Key Gaps Identified")

                    for gap in insights.get("key_gaps_identified", []):
                        st.warning(f"• {gap}")

                    # ---------- STRATEGIC RECOMMENDATIONS ----------
                    st.markdown("---")
                    st.header("🎯 Strategic Recommendations")

                    for rec in insights.get("strategic_recommendations", []):
                        st.success(f"• {rec}")

                    # ---------- QUICK WINS ----------
                    st.markdown("---")
                    st.header("⚡ Quick Wins")

                    for win in insights.get("quick_wins", []):
                        st.info(f"• {win}")

                    # ---------- LONG TERM MOVES ----------
                    st.markdown("---")
                    st.header("🚀 Long Term Moves")

                    for move in insights.get("long_term_moves", []):
                        st.markdown(f"• {move}")

                else:
                    st.error(f"API Error: {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")