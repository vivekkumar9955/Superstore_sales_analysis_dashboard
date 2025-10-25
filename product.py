import streamlit as st
import matplotlib.pyplot as plt
import warnings
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# Suppress specific warnings
# -----------------------------
warnings.filterwarnings(
    "ignore",
    message="Passing `palette` without assigning `hue` is deprecated"
)
warnings.filterwarnings("ignore", message="Glyph .* missing from font")

# -----------------------------
# Dashboard Function
# -----------------------------
def product_view(filtered_data):
    st.markdown("### 📊 Product and Regional Sales Overview")
    st.markdown("---")

    col1, col2 = st.columns([1.3, 0.9])

    # ---------------------------
    # 🛍️ Top 10 Products by Sales
    # ---------------------------
    st.subheader("🛍️ Top 10 Products by Sales")

    # --- Calculate Top 10 Products ---
    top_products = (
        filtered_data.groupby('Product Name')['Sales']
        .sum()
        .reset_index()
        .sort_values(by='Sales', ascending=False)
        .head(10)
    )

    # --- Add Rank Column ---
    top_products.reset_index(drop=True, inplace=True)
    top_products.index += 1
    top_products.rename_axis('Rank', inplace=True)

    # --- Format Sales Values ---
    top_products['Sales'] = top_products['Sales'].map('${:,.2f}'.format)

    # --- Display as Table ---
    st.dataframe(
        top_products,
        use_container_width=True,
        height=400
    )


    # ---------------------------
    # 💰 Sales by Region (Donut)
    # ---------------------------
    st.subheader("💸 Top 5 Most Profitable Products")

    # --- Calculate Top 5 Profitable Products ---
    top_products = (
        filtered_data.groupby('Product Name')['Profit']
        .sum()
        .reset_index()
        .sort_values(by='Profit', ascending=False)
        .head(5)
    )
    # --- Assign color based on profit ---
    top_products['color'] = ['red' if p < 0 else 'green' for p in top_products['Profit']]

    # --- Create Vertical Bar Chart ---
    fig = px.bar(
        top_products,
        y='Product Name',
        x='Profit',
        text='Profit',
        color='Profit',
        color_discrete_map={'green': 'green', 'red': 'red'},
        title='Top 5 Most Profitable Products'
    )

    # --- Beautify Chart ---
    fig.update_traces(
        texttemplate='₹%{text:,.0f}',  # format as currency (₹)
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title='Product Name',
        yaxis_title='Total Profit',
        xaxis_tickangle=-30,
        showlegend=False,
        title_x=0.35,
        title_font=dict(size=16),
        margin=dict(l=40, r=20, t=60, b=80),
        height=450
    )

    # --- Display Chart ---
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💸 Top 10 Least Profitable Products")

    # --- Calculate Top 5 least profitable products ---
    top_products = (
        filtered_data.groupby('Product Name')['Profit']
        .sum()
        .reset_index()
        .sort_values(by='Profit', ascending=True)  # lowest profits first
        .head(10)
    )

    # --- Assign color based on profit ---
    top_products['color'] = ['red' if p < 0 else 'green' for p in top_products['Profit']]

    # --- Create Horizontal Bar Chart ---
    fig = px.bar(
        top_products,
        x='Profit',
        y='Product Name',
        text='Profit',
        color='color',
        color_discrete_map={'green': 'green', 'red': 'red'},
        title='Top 10 Least Profitable Products',
        orientation='h'  # horizontal bars for long names
    )

    # --- Beautify Chart ---
    fig.update_traces(
        texttemplate='₹%{text:,.0f}',
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title='Total Profit',
        yaxis_title='',  # hide axis label
        showlegend=False,
        title_x=0.35,
        title_font=dict(size=16),
        margin=dict(l=200, r=20, t=60, b=40),
        height=400
    )

    # --- Display Chart ---
    st.plotly_chart(fig, use_container_width=True)
