import streamlit as st
from datetime import datetime
from helper import kpi_total_sales ,kpi_tatal_profit ,kpi_top_category
import pandas as pd

data = pd.read_csv('data/Superstore.csv')
# --- HEADER ---
def show_header():
    st.markdown("""
        <div style="
            background-color:#999999;
            padding:15px;
            border-radius:10px;
            text-align:center;
            color:#EFF1E6;
            margin-bottom:20px;
        ">
            <h2>📊 Superstore Sales Dashboard</h2>
            <p style="font-size:14px;">Interactive Insights for Business Growth</p>
        </div>
    """, unsafe_allow_html=True)


# --- KPI SECTION ---
def show_kpis():

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        total_sales = kpi_total_sales(data)
        st.metric("Total Sales", total_sales)
    with col2:
        top_city = data.groupby("City")["Sales"].sum().idxmax()
        st.metric("Top City ", top_city)
    with col3:
        total_profit = kpi_tatal_profit(data)
        st.metric("Total Profit", total_profit)
    with col4:
        top_category = kpi_top_category(data)
        st.metric("Top Category", top_category)

from datetime import datetime


from datetime import datetime
import streamlit as st
from datetime import datetime
import pandas as pd

def show_filters(df):
    st.subheader("Filters")

    region_col, state_col, city_col, start_date_col, end_date_col = st.columns(5)

    # Get unique values from dataframe
    regions = ["Choose an option"] + sorted(df["Region"].dropna().unique().tolist())
    states = ["Choose an option"] + sorted(df["State"].dropna().unique().tolist())
    cities = ["Choose an option"] + sorted(df["City"].dropna().unique().tolist())

    # Region filter
    with region_col:
        selected_region = st.selectbox("Select Region", regions, key="region")

    # State filter
    with state_col:
        selected_state = st.selectbox("Select State", states, key="state")

    # City filter
    with city_col:
        selected_city = st.selectbox("Pick the City", cities, key="city")

    # Start date filter
    with start_date_col:
        selected_start_date = st.date_input(
            "Start Date",
            value=datetime(2014, 1, 3),
            key="start_date"
        )

    # End date filter
    with end_date_col:
        selected_end_date = st.date_input(
            "End Date",
            value=datetime(2017, 12, 30),
            key="end_date"
        )

    st.markdown("<hr/>", unsafe_allow_html=True)

    # Return only the selected filter values
    return selected_region, selected_state, selected_city, selected_start_date, selected_end_date
