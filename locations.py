import streamlit as st
import plotly.express as px
from helper import state_abbrev


def locations_view(filtered_data):
    # Group by Sales State
    st.subheader("🗺️ Sales by State")

    # --- Group data by State ---
    sales_by_State = (
        filtered_data.groupby("State")[["Sales", "Profit","Discount"]]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    # Make sure State column has **state codes** for choropleth
    # Example mapping function (state_abbrev) should return dict: {'California': 'CA', ...}
    state_abbrev_dict = state_abbrev()
    sales_by_State['State_Code'] = sales_by_State['State'].map(state_abbrev_dict)

    # --- Create choropleth ---
    fig = px.choropleth(
        sales_by_State,
        locations='State_Code',  # use state codes for mapping
        locationmode='USA-states',
        color='Sales',
        hover_name='State',  # shows full state name on hover
        hover_data={'Sales': True, 'Profit': True, 'Discount':True,'State_Code': False},  # shows only sales, hides code
        color_continuous_scale='Viridis',
        scope='usa'
    )

    # --- Display in Streamlit ---
    st.plotly_chart(fig, use_container_width=True)


