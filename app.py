# app.py (UPDATED FULL FILE)
# Replace your entire app.py with this content.

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import textwrap
from datetime import date, timedelta

# ---------------------------------
# Page config
# ---------------------------------
st.set_page_config(page_title="Business Overview", page_icon="🧠", layout="wide")

# ---------------------------------
# Blue/White theme + card styling
# ---------------------------------
CSS = """
<style>
/* overall background */
.stApp { background: #F6FAFF; }

/* sidebar */
section[data-testid="stSidebar"]{
  background: #FFFFFF;
  border-right: 1px solid rgba(31,95,191,0.18);
}

/* tighten padding */
.block-container { padding-top: 1.1rem; padding-bottom: 2rem; }

/* headings */
h1, h2, h3 { color: #0B2E5F; letter-spacing: 0.2px; }

/* section containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: #FFFFFF;
  border: 1px solid rgba(31,95,191,0.18);
  border-radius: 14px;
}

/* KPI cards */
.kpi-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
@media (max-width: 1100px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 700px)  { .kpi-grid { grid-template-columns: repeat(1, 1fr); } }

.kpi-card{
  background: #FFFFFF;
  border: 1px solid rgba(31,95,191,0.22);
  border-radius: 14px;
  padding: 12px 14px;
  box-shadow: 0 1px 0 rgba(11,46,95,0.03);
}

.kpi-label{
  color: rgba(11,46,95,0.75);
  font-size: 0.86rem;
  line-height: 1.1rem;
  margin-bottom: 6px;
}

.kpi-value{
  color: #0B2E5F;
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.6rem;
}

/* AI badges */
.badge-ai{
  display: inline-block;
  padding: 4px 9px;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  background: rgba(31,95,191,0.10);
  color: #1F5FBF;
  border: 1px solid rgba(31,95,191,0.22);
  margin-bottom: 8px;
}

.ai-tile{
  background: #FFFFFF;
  border: 1px solid rgba(31,95,191,0.22);
  border-radius: 14px;
  padding: 12px 14px;
}

.ai-title{
  font-weight: 700;
  color: #0B2E5F;
  margin-bottom: 6px;
}

.ai-body{
  color: rgba(11,46,95,0.85);
  line-height: 1.35rem;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------------------------------
# Backend hooks (mock placeholders)
# ---------------------------------
def backend_search_entity(search_text: str) -> dict:
    search_text = (search_text or "").strip()
    if not search_text:
        return {"status": "empty"}
    if search_text.upper().startswith("HH"):
        return {
            "status": "ok",
            "entity_type": "household",
            "household_id": search_text.upper(),
            "label": f"Household {search_text.upper()}",
        }
    return {
        "status": "ok",
        "entity_type": "customer",
        "customer_id": search_text.upper(),
        "household_id": "HH9001",
        "label": f"Customer {search_text.upper()} → Household HH9001",
    }

def get_portfolio_summary(filters: dict) -> dict:
    return {
        "Total # Households": (12842, "Count of unique households in the selected portfolio."),
        "Total Deposits (USD)": (2_345_000_000, "Sum of deposit balances across households."),
        "Total Loans / Liabilities (USD)": (1_876_000_000, "Sum of loan principals / liabilities across households."),
        "Total Spend (Cards) (USD)": (412_000_000, "Total credit/debit card spend across households."),
        "Average # Accounts": (3.6, "Average number of bank accounts/products per household."),
        "Avg Household 360 Score": (72, "Composite household score (relationship + product + risk + events)."),
        "Avg Household Wallet Share %": (28, "Estimated share of household financial wallet captured by the bank."),
        "Avg Household Risk Tier": ("Medium", "Portfolio-level risk tier based on aggregated household exposure signals."),
        "Avg Product Penetration": (46, "Average product coverage across key categories (HPPI proxy)."),
    }

def get_hrsi_metrics(filters: dict) -> dict:
    return {
        "Average HRSI": (68, "Household Relationship Strength Index (0–100). Higher = more interconnected."),
        "% High / Med / Low": ("22% / 54% / 24%", "Distribution of households by relationship strength bands."),
        "Avg # Joint Products": (1.4, "Average number of jointly-held products (joint a/c, co-borrower loans, etc.)."),
        "% HH w/ Multi-member Ties": ("61%", "Households showing multi-member financial relationships in the graph."),
    }

def get_hppi_metrics(filters: dict) -> dict:
    return {
        "Average HPPI": (46, "Household Product Penetration Index: coverage across product categories."),
        "White-space Opportunities": (38500, "Estimated count of missing product-category opportunities across households."),
        "Top Underpenetrated Categories": ("Wealth, Premium Cards, Insurance", "Categories with lowest penetration in target segments."),
        "Target Cluster": ("Mid-income, 2+ products", "Segment recommended for cross-sell due to existing engagement."),
    }

def get_hppi_chart_df(filters: dict) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Product Category": [
                "Insurance",
                "Wealth/Investments",
                "Credit Card (Premium)",
                "Mortgage",
                "Personal Loan",
                "Credit Card (Basic)",
                "Checking",
                "Savings",
            ],
            "Penetration %": [9, 12, 18, 21, 27, 52, 64, 78],
        }
    )

def get_risk_metrics(filters: dict) -> dict:
    return {
        "Avg Household Risk Index": (0.74, "Household risk proxy: (Loans + Card Usage) / Deposits (example)."),
        "% High-risk Tier": ("14%", "Share of households classified as high risk."),
        "90d Trend": ("Slightly rising", "Directional trend over recent period (mock)."),
        "Concentration": ("Younger households", "Where utilization/risk signals cluster (mock)."),
    }

def get_risk_trend_df(filters: dict) -> pd.DataFrame:
    days = 60
    start = date.today() - timedelta(days=days)
    dates = pd.date_range(start=start, periods=days, freq="D")
    trend = np.clip(np.cumsum(np.random.normal(0.0002, 0.01, size=days)) + 0.68, 0.4, 1.2)
    return pd.DataFrame({"date": dates, "risk_index": trend})

def get_life_event_metrics(filters: dict) -> dict:
    return {
        "% HH with Life-event Signals": ("19%", "Households showing detectable life-event signals (relocation, mortgage, education)."),
        "Most Common Life Events": ("Move, Education Spend Rise, New Mortgage", "Top life-event signals in portfolio."),
        "Event Clusters": ("Middle-income rising", "Segments where life-event signals are increasing (mock)."),
        "Recommended Focus": ("Education + home protection", "Suggested playbooks based on detected events."),
    }

def get_life_event_df(filters: dict) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Life Event": [
                "Address change / relocation",
                "Tuition / education spend rising",
                "New mortgage opened",
                "Marriage / joint account creation",
                "Student loan closure",
            ],
            "Households": [940, 780, 620, 530, 410],
        }
    )

def gen_ai_business_overview_tiles() -> list[dict]:
    return [
        {
            "title": "Relationship Strength",
            "text": "High-HRSI households correlate with higher wallet share and lower attrition. Prioritize top decile HRSI households for bundled relationship offers.",
        },
        {
            "title": "Product Penetration",
            "text": "Investment and card products are underpenetrated. Target mid-income households with 2+ existing products for cross-sell journeys.",
        },
        {
            "title": "Credit Utilization & Risk Posture",
            "text": "Utilization pressure is concentrated in younger households. Avoid promoting unsecured credit to high-risk clusters; focus on low-risk, mortgage-ready segments.",
        },
        {
            "title": "Life Events",
            "text": "Life-event driven needs are rising in middle-income segments. Target upcoming college transitions with education savings and protection playbooks.",
        },
    ]

# ---------------------------------
# UI helpers
# ---------------------------------
def fmt_value(v):
    if isinstance(v, (int, np.integer)):
        return f"{v:,}"
    if isinstance(v, (float, np.floating)):
        if abs(v) < 10:
            return f"{v:.2f}".rstrip("0").rstrip(".")
        return f"{v:,.2f}"
    return str(v)

def kpi_grid(kpis: dict):
    cards = []
    for label, (value, tip) in kpis.items():
        card = f"""
<div class="kpi-card" title="{tip}">
  <div class="kpi-label">{label}</div>
  <div class="kpi-value">{fmt_value(value)}</div>
</div>
"""
        cards.append(textwrap.dedent(card).strip())

    html = f"""
<div class="kpi-grid">
  {''.join(cards)}
</div>
"""
    st.markdown(textwrap.dedent(html).strip(), unsafe_allow_html=True)

def ai_tiles(tiles: list[dict]):
    cols = st.columns(2)
    for i, t in enumerate(tiles):
        tile_html = f"""
<div class="ai-tile">
  <div class="badge-ai">🤖 AI-generated</div>
  <div class="ai-title">{t["title"]}</div>
  <div class="ai-body">{t["text"]}</div>
</div>
"""
        with cols[i % 2]:
            st.markdown(textwrap.dedent(tile_html).strip(), unsafe_allow_html=True)

def small_bar_chart(df: pd.DataFrame, x: str, y: str, title: str):
    chart = (
        alt.Chart(df)
        .mark_bar(color="#1F5FBF")
        .encode(
            x=alt.X(x, sort=None),
            y=alt.Y(y),
            tooltip=[y, x],
        )
        .properties(height=220, title=title)
    )
    st.altair_chart(chart, use_container_width=True)

def small_line_chart(df: pd.DataFrame, x: str, y: str, title: str):
    chart = (
        alt.Chart(df)
        .mark_line(color="#1F5FBF")
        .encode(
            x=alt.X(x, title=None),
            y=alt.Y(y, title=None),
            tooltip=[x, y],
        )
        .properties(height=220, title=title)
    )
    st.altair_chart(chart, use_container_width=True)

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.markdown("### 🔎 Search")
    search_text = st.text_input("Customer ID / Household ID", placeholder="e.g., C101 or HH9001")
    if "entity_ctx" not in st.session_state:
        st.session_state.entity_ctx = {"status": "empty"}
    if st.button("Search", use_container_width=True):
        st.session_state.entity_ctx = backend_search_entity(search_text)

    st.markdown("---")
    st.markdown("### 🎛 Filters")
    region = st.selectbox("Region", ["All", "North", "South", "East", "West"], index=0)
    segment = st.selectbox("Income Segment", ["All", "Mass", "Mid-income", "Affluent", "HNW"], index=0)
    risk_tier = st.selectbox("Risk Tier", ["All", "Low", "Medium", "High"], index=0)
    life_event_flag = st.selectbox("Life-event Flag", ["All", "Yes", "No"], index=0)

    st.markdown("---")
    with st.expander("📘 Glossary"):
        st.write("Hover over KPIs on the page to see definitions. This can be expanded later.")

filters = {"region": region, "segment": segment, "risk_tier": risk_tier, "life_event_flag": life_event_flag}

# ---------------------------------
# Header
# ---------------------------------
st.title("Business Overview")
st.caption("Household-level intelligence view (prototype UI). Hover on any KPI tile for definitions.")

entity_ctx = st.session_state.entity_ctx
if entity_ctx.get("status") == "ok":
    st.success(f"Selected: {entity_ctx.get('label')}")
else:
    st.info("Use the left search to load a Customer ID or Household ID context (mock).")

st.markdown("")

# ---------------------------------
# Portfolio Summary
# ---------------------------------
with st.container(border=True):
    st.subheader("Portfolio Summary")
    st.caption("A clean KPI strip summarizing the portfolio. (Hover to see definitions)")
    kpi_grid(get_portfolio_summary(filters))

st.markdown("")

# ---------------------------------
# Business Overview (AI tiles)
# ---------------------------------
with st.container(border=True):
    st.subheader("Business Overview (AI Suggestions)")
    st.caption("Narrative insights shown as AI-generated tiles (prototype placeholder).")
    ai_tiles(gen_ai_business_overview_tiles())

st.markdown("")

# ---------------------------------
# Relationship Strength (no graph)
# ---------------------------------
with st.container(border=True):
    st.subheader("Relationship Strength (HRSI)")
    st.caption("Hover over metrics for definitions.")

    st.markdown(
        textwrap.dedent("""
<div class="ai-tile">
  <div class="badge-ai">🤖 AI Recommendation</div>
  <div class="ai-title">Suggested Plays</div>
  <div class="ai-body">
    High HRSI → Offer family wealth planning •
    Medium → Offer joint savings upgrade •
    Low → Offer household consolidation products
  </div>
</div>
""").strip(),
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    kpi_grid(get_hrsi_metrics(filters))

st.markdown("")

# ---------------------------------
# Product Penetration
# ---------------------------------
with st.container(border=True):
    st.subheader("Product Penetration (HPPI)")
    st.caption("Hover over metrics for definitions.")

    left, right = st.columns([1.25, 1])

    with left:
        st.markdown(
            textwrap.dedent("""
<div class="ai-tile">
  <div class="badge-ai">🤖 AI Recommendation</div>
  <div class="ai-title">Strategy by HPPI</div>
  <div class="ai-body">
    HPPI < 40 → Cross-sell campaigns •
    40–70 → Upsell premium versions •
    >70 → Retention-focused strategy
  </div>
</div>
""").strip(),
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        kpi_grid(get_hppi_metrics(filters))

    with right:
        small_bar_chart(get_hppi_chart_df(filters), x="Penetration %", y="Product Category", title="Penetration by Category (Mock)")

st.markdown("")

# ---------------------------------
# Risk
# ---------------------------------
with st.container(border=True):
    st.subheader("Credit Utilization & Risk Posture")
    st.caption("Hover over metrics for definitions.")

    left, right = st.columns([1.25, 1])

    with left:
        st.markdown(
            textwrap.dedent("""
<div class="ai-tile">
  <div class="badge-ai">🤖 AI Guidance</div>
  <div class="ai-title">Risk-aware Activation</div>
  <div class="ai-body">
    Avoid promoting unsecured personal loans to high-risk clusters.
    Focus on low-risk, mortgage-ready households. Trigger early warnings for sudden utilization spikes.
  </div>
</div>
""").strip(),
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        kpi_grid(get_risk_metrics(filters))

    with right:
        small_line_chart(get_risk_trend_df(filters), x="date", y="risk_index", title="Risk Trend (Mock)")

st.markdown("")

# ---------------------------------
# Life Events
# ---------------------------------
with st.container(border=True):
    st.subheader("Life Events & Mobility")
    st.caption("Hover over metrics for definitions.")

    left, right = st.columns([1.25, 1])

    with left:
        st.markdown(
            textwrap.dedent("""
<div class="ai-tile">
  <div class="badge-ai">🤖 AI Recommendation</div>
  <div class="ai-title">Life-event Playbooks</div>
  <div class="ai-body">
    New mortgage → Home insurance •
    Address change → Utility bill offers •
    Student loan closure → Wealth planning
  </div>
</div>
""").strip(),
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        kpi_grid(get_life_event_metrics(filters))

    with right:
        small_bar_chart(get_life_event_df(filters), x="Households", y="Life Event", title="Life Events (Mock)")

st.caption("Prototype UI only — backend calls can replace mock functions without changing the layout.")