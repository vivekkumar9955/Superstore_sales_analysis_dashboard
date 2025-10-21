import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def trends_view(filtered_data):
    # Convert Order Date to datetime if not already
    filtered_data['Order Date'] = pd.to_datetime(filtered_data['Order Date'])

    # Group by Month (Period)
    monthly_sales = (
        filtered_data.groupby(filtered_data['Order Date'].dt.to_period('M'))['Sales']
        .sum()
        .reset_index()
    )

    # Convert back to timestamp for plotting
    monthly_sales['Order Date'] = monthly_sales['Order Date'].dt.to_timestamp()

    # st.write(monthly_sales.head())  # Optional: to see result

    monthly_trends = (
        filtered_data.groupby(filtered_data['Order Date'].dt.to_period('M'))[['Sales', 'Profit']]
        .sum()
        .reset_index()
    )

    monthly_trends['Order Date'] = monthly_trends['Order Date'].dt.to_timestamp()

    plt.style.use('Solarize_Light2')
    filtered_data['Month'] = filtered_data['Order Date'].dt.strftime('%b')
    monthly_sales = filtered_data.groupby('Month')['Sales'].sum().reindex(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ).reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_trends['Order Date'], monthly_trends['Sales'], label='Sales', color='teal', linewidth=2)
    ax.plot(monthly_trends['Order Date'], monthly_trends['Profit'], label='Profit', color='orange', linewidth=2,
            linestyle='--')

    ax.set_title("📅 Monthly Sales & Profit Trends", fontsize=14, fontweight='bold')
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    ax.legend(loc ='upper center')
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)
