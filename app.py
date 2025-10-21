import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu
from common import show_header, show_kpis, show_filters
from helper import state_abbrev
from sales import sales_view
from trends import trends_view
from locations import locations_view
from category import category_view
# --- PAGE CONFIG ---
st.set_page_config(page_title="Superstore Sales Dashboard", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
.stApp {background-color: #EFF1E6; color: #241341;}
[data-testid="stSidebar"] {background-color: #B6B7B2;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR MENU ---
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Sales", "Trends", "Category", "Product", "Location", "Shipping"],
        icons=["house", "cart-check", "graph-up", "grid", "box-seam", "geo-alt", "truck"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#B6B7B2"},
            "icon": {"color": "#241341", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "--hover-color": "#EFF1E6"},
            "nav-link-selected": {"background-color": "#999999"},
        }
    )

# --- LOAD DATA ---
data = pd.read_csv("data/Superstore.csv")

# --- COMMON COMPONENTS ---
show_header()
show_kpis()

# ✅ Show filters only once and capture returned values
selected_region, selected_state, selected_city, selected_start_date, selected_end_date = show_filters(data)

# --- APPLY FILTERS TO DATA ---
filtered_data = data.copy()

# Filter by region/state/city
if selected_region != "Choose an option":
    filtered_data = filtered_data[filtered_data["Region"] == selected_region]
if selected_state != "Choose an option":
    filtered_data = filtered_data[filtered_data["State"] == selected_state]
if selected_city != "Choose an option":
    filtered_data = filtered_data[filtered_data["City"] == selected_city]

# Convert dates safely using dayfirst=True
filtered_data["Order Date"] = pd.to_datetime(filtered_data["Order Date"], dayfirst=True, errors='coerce')
selected_start_date = pd.to_datetime(selected_start_date, dayfirst=True, errors='coerce')
selected_end_date = pd.to_datetime(selected_end_date, dayfirst=True, errors='coerce')

# Filter by date range
if not filtered_data["Order Date"].isnull().all():  # Ensure there are valid dates
    filtered_data = filtered_data[
        (filtered_data["Order Date"] >= selected_start_date) &
        (filtered_data["Order Date"] <= selected_end_date)
    ]

# --- PAGE CONTENT ---
if selected == "Home":
    st.subheader("🏠 Home Overview")
    st.write("you can see here order details through filter or without filter")
    st.dataframe(filtered_data)

elif selected == "Sales":
    #data come from sales.py
    sales_view(filtered_data)

elif selected == "Trends":
    trends_view(filtered_data)





elif selected == "Category":
    category_view(filtered_data)


elif selected == "Product":
    st.subheader("🛍️ Product Insights")
    st.write("Explore product-wise performance metrics here.")

elif selected == "Location":
    locations_view(filtered_data)


elif selected == "Shipping":
    st.subheader("🚚 Shipping Performance")
    st.write("Analyze shipping modes and delivery timelines here.")
