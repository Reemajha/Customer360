import streamlit as st
import pandas as pd
<<<<<<< HEAD
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx

st.set_page_config(layout="wide")

# =====================================================
# ENTERPRISE STYLING
# =====================================================
st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:38px;
    font-weight:700;
    color:#123B63;
}
.section-title {
    font-size:22px;
    font-weight:600;
    color:#123B63;
    margin-top:20px;
}
.insight-box {
    background-color:#f0f6ff;
    padding:15px;
    border-radius:12px;
    border-left:6px solid #f37021;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================
#st.sidebar.image("exl_logo.png", width=120)

page = st.sidebar.radio(
    "Navigation",
    ["Data Upload", "Business Overview",
     "Household Overview", "Identity Graph"]
)
=======
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import textwrap

st.set_page_config(layout="wide", page_title="Customer360 | Business Overview")

# =====================================================
# PROFESSIONAL DASHBOARD STYLE (Blue/White + better hierarchy)
# =====================================================
CSS = """
<style>
/* Fix top-cut + improve spacing */
.block-container{
  padding-top: 2.25rem;
  padding-bottom: 2rem;
  max-width: 1450px;
}
.stApp{ background: #F6FAFF; }

/* Sidebar */
section[data-testid="stSidebar"]{
  background: #FFFFFF;
  border-right: 1px solid rgba(31,95,191,0.16);
}

/* Typography */
.h1{
  font-size: 28px;
  font-weight: 800;
  color: #0B2E5F;
  margin: 0 0 4px 0;
}
.sub{
  color: rgba(11,46,95,0.72);
  font-size: 0.92rem;
  margin: 0 0 14px 0;
}
.h2{
  font-size: 16px;
  font-weight: 800;
  color: #0B2E5F;
  margin: 0 0 10px 0;
}
.h2-divider{
  display:flex;
  align-items:center;
  gap:10px;
  margin: 10px 0 10px 0;
}
.h2-divider .line{
  height: 1px;
  background: rgba(31,95,191,0.18);
  flex: 1;
}

/* Card shell */
.card{
  background: #FFFFFF;
  border: 1px solid rgba(31,95,191,0.16);
  border-radius: 14px;
  padding: 14px;
  box-shadow: 0 1px 0 rgba(11,46,95,0.03);
  margin-bottom: 14px;
}

/* KPI grid */
.kpi-grid{
  display:grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
@media (max-width: 1200px){ .kpi-grid{ grid-template-columns: repeat(3, 1fr);} }
@media (max-width: 900px){ .kpi-grid{ grid-template-columns: repeat(2, 1fr);} }
@media (max-width: 560px){ .kpi-grid{ grid-template-columns: repeat(1, 1fr);} }

.kpi-card{
  background:#FFFFFF;
  border: 1px solid rgba(31,95,191,0.18);
  border-radius: 12px;
  padding: 10px 12px;
}
.kpi-label{
  color:#111827; /* black label per your feedback */
  font-size: 0.80rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.kpi-value{
  color:#1F5FBF; /* blue value */
  font-size: 1.15rem;
  font-weight: 900;
  line-height: 1.2rem;
}

/* AI Suggestions grid (more engaging) */
.ai-grid{
  display:grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}
@media (max-width: 900px){ .ai-grid{ grid-template-columns: repeat(1, 1fr);} }

.ai-card{
  border-radius: 14px;
  padding: 12px 14px;
  border: 1px solid rgba(31,95,191,0.18);
  background: linear-gradient(180deg, rgba(31,95,191,0.06), rgba(255,255,255,1));
  position: relative;
  overflow: hidden;
}
.ai-accent{
  position:absolute;
  left:0; top:0; bottom:0;
  width: 6px;
  background: #1F5FBF;
  opacity: 0.9;
}
.ai-badge{
  display:inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  color: #1F5FBF;
  background: rgba(31,95,191,0.10);
  border: 1px solid rgba(31,95,191,0.18);
  padding: 4px 9px;
  border-radius: 999px;
  margin-bottom: 8px;
}
.ai-title{
  font-size: 0.95rem;
  font-weight: 900;
  color: #0B2E5F;
  margin-bottom: 6px;
  display:flex;
  gap: 8px;
  align-items:center;
}
.ai-body{
  color: rgba(11,46,95,0.84);
  font-size: 0.90rem;
  line-height: 1.35rem;
}

/* KPI Section tiles (2x2) */
.kpi-section-grid{
  display:grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}
@media (max-width: 950px){ .kpi-section-grid{ grid-template-columns: repeat(1, 1fr);} }

.kpi-section{
  background:#FFFFFF;
  border: 1px solid rgba(31,95,191,0.16);
  border-radius: 14px;
  padding: 14px;
  box-shadow: 0 1px 0 rgba(11,46,95,0.03);
}
.kpi-section-header{
  display:flex;
  align-items:center;
  justify-content:space-between;
  margin-bottom: 8px;
}
.kpi-section-title{
  display:flex;
  gap: 8px;
  align-items:center;
  font-weight: 900;
  color:#0B2E5F;
  font-size: 1.0rem;
}
.kpi-section-sub{
  color: rgba(11,46,95,0.70);
  font-size: 0.85rem;
  margin-bottom: 10px;
}

.reco{
  border-radius: 12px;
  padding: 10px 12px;
  border: 1px solid rgba(243,112,33,0.28);
  background: rgba(243,112,33,0.08);
  margin: 10px 0 10px 0;
}
.reco-title{
  font-weight: 900;
  color:#8A3B12;
  font-size: 0.82rem;
  margin-bottom: 4px;
}
.reco-body{
  color: rgba(53,18,8,0.86);
  font-size: 0.90rem;
  line-height: 1.25rem;
}

/* Small tooltip icon */
.tip{ color: rgba(11,46,95,0.55); font-weight: 900; margin-left: 6px; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def _dedent(s: str) -> str:
    return textwrap.dedent(s).strip()


def kpi_grid(kpis: dict):
    # kpis: {label: (value, tooltip)}
    items = []
    for label, (value, tip) in kpis.items():
        items.append(_dedent(f"""
        <div class="kpi-card" title="{tip}">
          <div class="kpi-label">{label}</div>
          <div class="kpi-value">{value}</div>
        </div>
        """))
    st.markdown(_dedent(f"""<div class="kpi-grid">{''.join(items)}</div>"""), unsafe_allow_html=True)


def ai_suggestions_grid(tiles: list[dict]):
    blocks = []
    for t in tiles:
        blocks.append(_dedent(f"""
        <div class="ai-card">
          <div class="ai-accent"></div>
          <div class="ai-badge">🤖 AI-generated insight</div>
          <div class="ai-title">{t["icon"]} {t["title"]}</div>
          <div class="ai-body">{t["text"]}</div>
        </div>
        """))
    st.markdown(_dedent(f"""<div class="ai-grid">{''.join(blocks)}</div>"""), unsafe_allow_html=True)


def section_title(text: str):
    st.markdown(f"<div class='h2'>{text}</div>", unsafe_allow_html=True)


def divider_title(text: str):
    st.markdown(_dedent(f"""
    <div class="h2-divider">
      <div class="h2">{text}</div>
      <div class="line"></div>
    </div>
    """), unsafe_allow_html=True)


# =====================================================
# SIDEBAR NAVIGATION (kept from colleague's file)
# =====================================================
page = st.sidebar.radio("Navigation", ["Data Upload", "Business Overview", "Household Overview", "Identity Graph"])

>>>>>>> 4280cea (Improve Business Overview UI: styling, tooltips, KPI tiles)

# =====================================================
# PAGE 1 — DATA UPLOAD
# =====================================================
if page == "Data Upload":
<<<<<<< HEAD

    st.markdown('<div class="main-title">GenAI Activated Customer & Household Intelligence</div>', unsafe_allow_html=True)

    st.markdown("### Select Data Source")

    source = st.selectbox("Choose Source",
                          ["Core Banking", "Credit Card System",
                           "CRM", "Upload Excel"])

=======
    st.markdown("<div class='h1'>GenAI Activated Customer & Household Intelligence</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Prototype UI — select a source or upload a file to simulate ingestion.</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    section_title("Select Data Source")
    source = st.selectbox("Choose Source", ["Core Banking", "Credit Card System", "CRM", "Upload Excel"])
>>>>>>> 4280cea (Improve Business Overview UI: styling, tooltips, KPI tiles)
    if source == "Upload Excel":
        uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "csv"])
        if uploaded_file:
            st.success("File uploaded successfully!")
<<<<<<< HEAD

# =====================================================
# PAGE 2 — BUSINESS OVERVIEW
# =====================================================
if page == "Business Overview":

    # ---------------- Portfolio Summary ----------------
    st.markdown('<div class="section-title" style="text-align:center;">Portfolio Summary</div>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Total Households", "48,250")
    col2.metric("Total Deposits", "$3.2B")
    col3.metric("Total Loans", "$1.8B")
    col4.metric("Total Spend (Cards)", "$920M")
    col5.metric("Avg # Accounts", "3.4")
    col6.metric("Avg Household 360 Score", "74")

    # ---------------- Relationship & Product ----------------
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown('<div class="section-title">Relationship Strength</div>', unsafe_allow_html=True)

        st.metric("Average HRSI", "81")
        st.metric("% High Strength", "42%")
        st.metric("Avg Joint Products", "1.8")

        df_rel = pd.DataFrame({
            "Category": ["High", "Medium", "Low"],
            "Households": [20000, 18000, 10250]
        })

        fig_rel = px.pie(df_rel, names="Category", values="Households")
        st.plotly_chart(fig_rel, use_container_width=True)

        st.markdown('<div class="insight-box">'
                    'High-HRSI households correlate with higher wallet share and lower attrition.<br>'
                    'Prioritize top decile HRSI households for bundled relationship offers.'
                    '</div>', unsafe_allow_html=True)

    with col_right:
        st.markdown('<div class="section-title">Product Penetration</div>', unsafe_allow_html=True)

        st.metric("Average HPPI", "67")
        st.metric("White-space Opportunities", "18,420")

        df_prod = pd.DataFrame({
            "Product": ["Investments", "Cards", "Mortgage"],
            "Penetration": [35, 42, 58]
        })

        fig_prod = px.bar(df_prod, x="Product", y="Penetration")
        st.plotly_chart(fig_prod, use_container_width=True)

        st.markdown('<div class="insight-box">'
                    'Investment and card products appear significantly underpenetrated.<br>'
                    'Target mid-income households with 2+ existing products for cross-sell.'
                    '</div>', unsafe_allow_html=True)

    # ---------------- Risk & Life Event ----------------
    col_bottom_left, col_bottom_right = st.columns(2)

    with col_bottom_left:
        st.markdown('<div class="section-title">Risk Posture</div>', unsafe_allow_html=True)

        st.metric("Average HCRAS", "58")
        st.metric("% High Risk", "14%")
        st.metric("Credit Utilization", "63%")

        df_risk = pd.DataFrame({
            "Days": ["Day 1", "Day 30", "Day 60", "Day 90"],
            "Risk Score": [55, 56, 57, 58]
        })

        fig_risk = px.line(df_risk, x="Days", y="Risk Score")
        st.plotly_chart(fig_risk, use_container_width=True)

        st.markdown('<div class="insight-box">'
                    'Rising utilization is concentrated in younger households.<br>'
                    'Avoid promoting personal loans to high-risk clusters.'
                    '</div>', unsafe_allow_html=True)

    with col_bottom_right:
        st.markdown('<div class="section-title">Life Event Intelligence</div>', unsafe_allow_html=True)

        st.metric("% Households w/ Life Events", "28%")

        df_life = pd.DataFrame({
            "Event": ["Relocation", "Education", "Job Change"],
            "Count": [4200, 3800, 5100]
        })

        fig_life = px.bar(df_life, x="Event", y="Count")
        st.plotly_chart(fig_life, use_container_width=True)

        st.markdown('<div class="insight-box">'
                    'Life-event-driven needs are rising in middle-income segments.<br>'
                    'Target households with upcoming college transitions with 529 plans.'
                    '</div>', unsafe_allow_html=True)

# =====================================================
# PAGE 3 — HOUSEHOLD OVERVIEW
# =====================================================
if page == "Household Overview":

    st.markdown('<div class="section-title">Search Household</div>', unsafe_allow_html=True)

    hh_id = st.text_input("Enter Household ID")

    col_main, col_ai = st.columns([2,1])

    with col_main:
        st.markdown('<div class="section-title">Financial Snapshot</div>', unsafe_allow_html=True)

        st.metric("Total Deposits", "$420,000")
        st.metric("Total Loans", "$280,000 (Mortgage + Auto)")
        st.metric("Credit Card Utilization", "71% (3 Cards)")
        st.metric("Net Worth Estimate", "$650,000")

        st.markdown("### Members in Household")
        st.write(["Jennifer Lopez", "Karen Lopez"])

    with col_ai:
        st.markdown('<div class="section-title">AI Recommendations</div>', unsafe_allow_html=True)

        st.info("""
        Household shows strong relationship index but low investment penetration.
        Recommend Premium Card Upgrade + Investment Advisory outreach.
        """)

        st.markdown("### Copilot Insight")
        st.success("Primary financial influencer: Jennifer Lopez")

# =====================================================
# PAGE 4 — IDENTITY GRAPH
# =====================================================
if page == "Identity Graph":

    st.markdown('<div class="section-title">Household Financial Identity Mapping</div>', unsafe_allow_html=True)
=======
    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================
# PAGE 2 — BUSINESS OVERVIEW (Slide 15 aligned + improved UI)
# =====================================================
if page == "Business Overview":
    st.markdown("<div class='h1'>Business Overview</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Slide 15: Portfolio Summary → AI Suggestions → Key KPI tiles (Household-level).</div>", unsafe_allow_html=True)

    # -------- Portfolio Summary
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    divider_title("Portfolio Summary")
    st.caption("Hover over any tile to see a definition.")

    portfolio_kpis = {
        "Total Number of Households": ("48,250", "Count of unique households in the selected portfolio."),
        "Total Deposits": ("$3.2B", "Sum of deposit balances across households."),
        "Total Loans / Liabilities": ("$1.8B", "Sum of loan principals / liabilities across households."),
        "Total Spend (Cards)": ("$920M", "Aggregate card spend across households."),
        "Avg # Accounts": ("3.4", "Average number of accounts/products per household."),
        "Avg Household 360 Score": ("74", "Composite score (relationship + product + risk + events)."),
        "Avg Household Wallet Share %": ("28%", "Estimated bank share of household wallet."),
        "Avg Household Risk Tier": ("Medium", "Portfolio risk tier based on household exposure signals."),
        "Avg Product Penetration": ("46", "Average product coverage across key categories (HPPI proxy)."),
    }
    kpi_grid(portfolio_kpis)
    st.markdown("</div>", unsafe_allow_html=True)

    # -------- Business Overview AI Suggestions (more engaging)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    divider_title("Business Overview AI Suggestions")
    st.caption("These are narrative insights generated by AI (prototype placeholders).")

    ai_tiles = [
        {
            "icon": "🧩",
            "title": "Relationship Strength",
            "text": "High-HRSI households correlate with higher wallet share and lower attrition. Prioritize top decile households for bundled relationship offers.",
        },
        {
            "icon": "🎯",
            "title": "Product Penetration",
            "text": "Investment and card products appear underpenetrated. Target mid-income households with 2+ existing products for cross-sell journeys.",
        },
        {
            "icon": "🛡️",
            "title": "Credit Utilization & Risk",
            "text": "Utilization pressure is higher in younger households. Avoid pushing unsecured credit to high-risk clusters; focus on low-risk mortgage-ready segments.",
        },
        {
            "icon": "📍",
            "title": "Life Events",
            "text": "Life-event-driven needs are rising in middle-income segments. Target college transitions with education savings and protection playbooks.",
        },
    ]
    ai_suggestions_grid(ai_tiles)
    st.markdown("</div>", unsafe_allow_html=True)

    # -------- Clear separation into 4 KPI tiles
    divider_title("Key KPIs (Household-Level)")

    st.caption("Each KPI tile includes an AI recommendation, key metrics (with tooltips), and a compact chart (mock).")

    # Build 4 KPI tiles (2x2)
    tiles_html = []

    # 1) Relationship Strength (remove pie; cleaner)
    rel_kpis = {
        "Average HRSI": ("81", "Household Relationship Strength Index (0–100). Higher = more interconnected."),
        "% High Strength": ("42%", "Share of households classified as High relationship strength."),
        "Avg Joint Products": ("1.8", "Average number of jointly-held products."),
        "% Multi-member Ties": ("61%", "Households showing multi-member ties in household graph."),
    }
    df_rel = pd.DataFrame({"Band": ["High", "Medium", "Low"], "Households": [20000, 18000, 10250]})

    # 2) Product Penetration
    prod_kpis = {
        "Average HPPI": ("67", "Household Product Penetration Index (0–100)."),
        "White-space Opportunities": ("18,420", "Estimated missing product opportunities across households."),
        "Lowest Penetration": ("Wealth / Premium Cards", "Categories with most whitespace."),
        "Target Cluster": ("Mid-income, 2+ products", "Segment recommended for cross-sell."),
    }
    df_prod = pd.DataFrame({"Product": ["Investments", "Cards", "Mortgage"], "Penetration": [35, 42, 58]})

    # 3) Risk Posture
    risk_kpis = {
        "Average HCRAS": ("58", "Household Credit Risk Aggregation Score (portfolio proxy)."),
        "% High Risk": ("14%", "Share of households in high-risk tier."),
        "Credit Utilization": ("63%", "Utilization across credit products (proxy)."),
        "Trend Window": ("Last 90 days", "Time window used for monitoring (prototype)."),
    }
    df_risk = pd.DataFrame({"Days": ["Day 1", "Day 30", "Day 60", "Day 90"], "Risk Score": [55, 56, 57, 58]})

    # 4) Life Events
    life_kpis = {
        "% HH w/ Life Events": ("28%", "Households with detected life event indicators."),
        "Top Events": ("Relocation, Education", "Most common life events detected."),
        "Rising Segment": ("Middle-income", "Segment where signals are increasing."),
        "Recommended Focus": ("Education savings", "Suggested playbook category."),
    }
    df_life = pd.DataFrame({"Event": ["Relocation", "Education", "Job Change"], "Count": [4200, 3800, 5100]})

    # Render KPI tiles (Streamlit layout)
    st.markdown("<div class='kpi-section-grid'>", unsafe_allow_html=True)

    # Tile helper
    def render_kpi_tile(icon, title, title_tip, reco_title, reco_body, kpis, chart_fig):
        st.markdown("<div class='kpi-section'>", unsafe_allow_html=True)

        st.markdown(_dedent(f"""
        <div class="kpi-section-header" title="{title_tip}">
          <div class="kpi-section-title">{icon} {title}<span class="tip">ⓘ</span></div>
        </div>
        """), unsafe_allow_html=True)

        st.markdown(_dedent(f"""
        <div class="reco">
          <div class="reco-title">🤖 AI Recommendation — {reco_title}</div>
          <div class="reco-body">{reco_body}</div>
        </div>
        """), unsafe_allow_html=True)

        # KPIs (compact grid 2x2 inside tile)
        inner = []
        for lbl, (val, tip) in kpis.items():
            inner.append(_dedent(f"""
            <div class="kpi-card" title="{tip}">
              <div class="kpi-label">{lbl}</div>
              <div class="kpi-value">{val}</div>
            </div>
            """))
        st.markdown(_dedent(f"""
        <div class="kpi-grid" style="grid-template-columns: repeat(2, 1fr);">
          {''.join(inner)}
        </div>
        """), unsafe_allow_html=True)

        st.plotly_chart(chart_fig, use_container_width=True, config={"displayModeBar": False})
        st.markdown("</div>", unsafe_allow_html=True)

    # 2x2: Relationship + Product
    colA, colB = st.columns(2)
    with colA:
        fig_rel = px.bar(df_rel, x="Band", y="Households", height=250, title="Relationship Strength Distribution (Mock)")
        fig_rel.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        render_kpi_tile(
            "🧩",
            "Relationship Strength (HRSI)",
            "Measures financial interconnectedness in household (joint a/c, co-borrowing, internal transfers).",
            "Plays by HRSI",
            "High → Wealth planning • Medium → Joint savings upgrade • Low → Consolidation offers",
            rel_kpis,
            fig_rel,
        )

    with colB:
        fig_prod = px.bar(df_prod, x="Product", y="Penetration", height=250, title="Product Penetration (Mock)")
        fig_prod.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        render_kpi_tile(
            "🎯",
            "Product Penetration (HPPI)",
            "Measures how embedded the bank is across household product categories.",
            "Strategy by HPPI",
            "HPPI < 40 → Cross-sell • 40–70 → Upsell premium • >70 → Retention focus",
            prod_kpis,
            fig_prod,
        )

    # 2x2: Risk + Life events
    colC, colD = st.columns(2)
    with colC:
        fig_risk = px.line(df_risk, x="Days", y="Risk Score", height=250, title="Risk Trend (Mock)")
        fig_risk.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        render_kpi_tile(
            "🛡️",
            "Credit Utilization & Risk Posture",
            "Aggregated household exposure & leverage signals (portfolio view).",
            "Risk-aware targeting",
            "Avoid unsecured credit to high-risk clusters. Focus on low-risk mortgage-ready households.",
            risk_kpis,
            fig_risk,
        )

    with colD:
        fig_life = px.bar(df_life, x="Event", y="Count", height=250, title="Life Events (Mock)")
        fig_life.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        render_kpi_tile(
            "📍",
            "Life Events & Mobility",
            "Signals like relocation, mortgage, education spend changes, life-stage transitions.",
            "Life-event playbooks",
            "New mortgage → Home insurance • Address change → Utility offers • Education → Savings plans",
            life_kpis,
            fig_life,
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =====================================================
# PAGE 3 — HOUSEHOLD OVERVIEW (kept; light polish)
# =====================================================
if page == "Household Overview":
    st.markdown("<div class='h1'>Household Overview</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Search a household and view snapshot + AI guidance.</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    section_title("Search Household")
    hh_id = st.text_input("Enter Household ID", placeholder="e.g., HH9001")
    st.markdown("</div>", unsafe_allow_html=True)

    col_main, col_ai = st.columns([2, 1])

    with col_main:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        divider_title("Financial Snapshot")
        snap = {
            "Total Deposits": ("$420,000", "Sum of deposits across household members."),
            "Total Loans": ("$280,000", "Sum of loan principals (mortgage/auto/personal)."),
            "Credit Card Utilization": ("71%", "Total balance / total credit limit across cards."),
            "Net Worth Estimate": ("$650,000", "Deposits + investments - liabilities (prototype)."),
        }
        kpi_grid(snap)
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='h2'>Members in Household</div>", unsafe_allow_html=True)
        st.write(["Jennifer Lopez", "Karen Lopez"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col_ai:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        divider_title("AI Recommendations")
        st.info("Household shows strong relationship index but low investment penetration. Recommend Premium Card Upgrade + Investment Advisory outreach.")
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        divider_title("Copilot Insight")
        st.success("Primary financial influencer: Jennifer Lopez")
        st.markdown("</div>", unsafe_allow_html=True)


# =====================================================
# PAGE 4 — IDENTITY GRAPH (kept; light polish)
# =====================================================
if page == "Identity Graph":
    st.markdown("<div class='h1'>Identity Graph</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Household financial identity mapping (prototype graph view).</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    divider_title("Household Financial Identity Mapping")
>>>>>>> 4280cea (Improve Business Overview UI: styling, tooltips, KPI tiles)

    G = nx.Graph()
    G.add_edges_from([
        ("Jennifer Lopez", "Karen Lopez"),
        ("Jennifer Lopez", "Joint Mortgage"),
        ("Karen Lopez", "Savings Account"),
        ("Jennifer Lopez", "Credit Card 1")
    ])

<<<<<<< HEAD
    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
=======
    pos = nx.spring_layout(G, seed=7)

    edge_x, edge_y = [], []
    for e in G.edges():
        x0, y0 = pos[e[0]]
        x1, y1 = pos[e[1]]
>>>>>>> 4280cea (Improve Business Overview UI: styling, tooltips, KPI tiles)
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    fig = go.Figure()
<<<<<<< HEAD

    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        mode='lines',
        line=dict(width=1),
        hoverinfo='none'
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="insight-box">'
                'Primary financial influencer: Jennifer Lopez.<br>'
                'Joint loan exposure within acceptable threshold.'
                '</div>', unsafe_allow_html=True)
=======
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        mode="lines",
        line=dict(width=1, color="rgba(31,95,191,0.55)"),
        hoverinfo="none"
    ))

    node_x, node_y, node_text = [], [], []
    for n in G.nodes():
        x, y = pos[n]
        node_x.append(x); node_y.append(y); node_text.append(n)

    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        marker=dict(size=14, color="#1F5FBF"),
        hoverinfo="text"
    ))

    fig.update_layout(
        height=520,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown(_dedent("""
    <div class="reco">
      <div class="reco-title">🤖 AI-generated graph insight</div>
      <div class="reco-body">
        Primary financial influencer: Jennifer Lopez. Joint loan exposure within acceptable threshold.
      </div>
    </div>
    """), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
>>>>>>> 4280cea (Improve Business Overview UI: styling, tooltips, KPI tiles)
