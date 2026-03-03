import streamlit as st
import pandas as pd
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

# =====================================================
# PAGE 1 — DATA UPLOAD
# =====================================================
if page == "Data Upload":

    st.markdown('<div class="main-title">GenAI Activated Customer & Household Intelligence</div>', unsafe_allow_html=True)

    st.markdown("### Select Data Source")

    source = st.selectbox("Choose Source",
                          ["Core Banking", "Credit Card System",
                           "CRM", "Upload Excel"])

    if source == "Upload Excel":
        uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "csv"])
        if uploaded_file:
            st.success("File uploaded successfully!")

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

    G = nx.Graph()
    G.add_edges_from([
        ("Jennifer Lopez", "Karen Lopez"),
        ("Jennifer Lopez", "Joint Mortgage"),
        ("Karen Lopez", "Savings Account"),
        ("Jennifer Lopez", "Credit Card 1")
    ])

    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []

    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    fig = go.Figure()

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