import streamlit as st
import plotly.express as px
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Lūr Cycle Investment Strategy", layout="wide")

# Title and introduction
st.title("Lūr Cycle Investment Strategy Visualization")
st.markdown(
    """
    This interactive dashboard illustrates a strategy for investing in **China**, **Russia**, and the **United States** markets using the Lūr Cycle methodology. 
    The methodology is broken into three phases:
    - **Phase 1: Foundation (First Principles Thinking)**
    - **Phase 2: Construction (Logic)**
    - **Phase 3: Clarification (Feynman Technique)**
    
    Plus, an **Investment Strategy** section details asset allocation and risk management.
    """
)

# Sidebar for phase selection
phase = st.sidebar.selectbox("Select Phase", ["Foundation", "Construction", "Clarification", "Investment Strategy"])

if phase == "Foundation":
    st.header("Phase 1: Foundation (First Principles Thinking)")
    st.markdown("### Identify the Basics")
    
    # Expandable details for each market
    with st.expander("China"):
        st.markdown("""
        **Facts:**
        - Rapid urbanization
        - Government control over markets
        - Push towards tech self-sufficiency
        - Large consumer base
        - Regulatory crackdowns
        
        **Essence:**
        Invest in sectors with strong government support, while staying alert to policy shifts.
        """)
        
    with st.expander("Russia"):
        st.markdown("""
        **Facts:**
        - Commodity-driven economy
        - Geopolitical tensions leading to market isolation
        - Domestic market resilience
        
        **Essence:**
        Focus on companies that benefit from commodity price swings and can adapt to changing trade routes.
        """)
        
    with st.expander("United States"):
        st.markdown("""
        **Facts:**
        - Diverse economy
        - Tech leadership and consumer market strength
        - High valuations and evolving policy landscape
        
        **Essence:**
        Diversify across sectors, targeting innovation and companies with global reach.
        """)

elif phase == "Construction":
    st.header("Phase 2: Construction (Logic)")
    st.markdown("### Logical Deduction and Verification")
    
    st.markdown("Select a country to explore its strategic sector focus and underlying hypothesis.")
    country = st.selectbox("Country", ["China", "Russia", "United States"])
    
    if country == "China":
        st.markdown("""
        **Sector Focus:**
        - Renewable energy
        - Electric vehicles (EVs)
        - Tech companies (semiconductors, AI)
        
        **Hypothesis:**
        Companies like **CATL** (battery tech) or **BYD** (EVs) might grow due to supportive government policies, though regulatory changes require vigilance.
        """)
    elif country == "Russia":
        st.markdown("""
        **Sector Focus:**
        - Oil and gas (e.g., Gazprom, Rosneft)
        - Mining exposure
        
        **Hypothesis:**
        Target companies that have successfully managed sanctions and maintain strong ties with domestic or Eastern markets.
        """)
    elif country == "United States":
        st.markdown("""
        **Sector Focus:**
        - Tech giants (e.g., Apple, Microsoft)
        - Healthcare (e.g., Johnson & Johnson)
        - Consumer discretionary (e.g., Nike, Starbucks)
        
        **Hypothesis:**
        A diversified approach can balance high-growth tech with the stability of healthcare and consumer trends.
        """)
    
    st.markdown("#### Logical Verification")
    st.markdown("""
    - **China:** Verify consistency of policy support with company performance.
    - **Russia:** Monitor commodity prices, geopolitical developments, and sanction impacts.
    - **United States:** Compare current valuations against historical data and economic indicators.
    """)

elif phase == "Clarification":
    st.header("Phase 3: Clarification (Feynman Technique)")
    st.markdown("### Simplify and Explain the Strategy")
    
    st.markdown("""
    - **China:** "Invest where the government signals growth (e.g., green tech), but be prepared to pivot with regulatory shifts."
    - **Russia:** "Bet on commodities when conditions are favorable, focusing on companies with flexible market exposure."
    - **United States:** "Spread investments across tech for growth, healthcare for stability, and consumer goods as economic barometers."
    """)
    
    st.markdown("### Identify Gaps & Continuous Iteration")
    st.markdown("""
    - **China:** How to predict or react to sudden policy changes.
    - **Russia:** Grasping nuances of new energy/trade partnerships.
    - **United States:** Distinguishing between a market bubble and genuine growth.
    
    **Iteration:** Regularly review global economic news, policy updates, and sector trends to refine your strategy.
    """)

elif phase == "Investment Strategy":
    st.header("Investment Strategy & Risk Management")
    st.markdown("### Asset Allocation")
    
    # Create a DataFrame for allocation
    allocation_data = {
        "Market": ["China", "Russia", "United States"],
        "Allocation (%)": [35, 15, 50]
    }
    df_alloc = pd.DataFrame(allocation_data)
    
    # Create a pie chart for allocation
    fig = px.pie(df_alloc, names='Market', values='Allocation (%)', title='Investment Allocation')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Risk Management & Investment Horizon")
    st.markdown("""
    **Risk Management:**
    - **China & Russia:** Use stop-loss orders or options to manage higher volatility.
    - **United States:** Rebalance quarterly or after significant economic or geopolitical shifts.
    
    **Investment Horizon:**
    - **United States:** Focus on long-term growth.
    - **China:** Aim for medium-term gains aligned with policy clarity.
    - **Russia:** Look for short-term opportunities driven by commodity cycles and geopolitical events.
    """)

st.markdown("---")
st.markdown("This dashboard follows first principles of good visualization by keeping the interface intuitive, using clear headings, interactive widgets, and visual representations (like the pie chart) to convey critical information.")