import streamlit as st
import plotly.express as px

def category_view(filtered_data):
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📦 Quantity Sold by Sub-Category within Each Category (Stacked Bar)")

        # --- Group Data ---
        quantity_by_cat = (
            filtered_data.groupby(['Category', 'Sub-Category'])['Quantity']
            .sum()
            .reset_index()
            .sort_values(by='Quantity', ascending=False)
        )

        # --- Create Vertical Stacked Bar Chart ---
        fig = px.bar(
            quantity_by_cat,
            x='Category',           # X-axis → Categories
            y='Quantity',           # Y-axis → Quantity sold
            color='Sub-Category',   # Stack by Sub-Category
            hover_name='Sub-Category',
            title='Quantity Sold by Sub-Category within Each Category',
            text='Quantity',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_layout(
            barmode='stack',
            template='plotly_white',
            title_font=dict(size=16, color='black', family='Arial Black'),
            xaxis_title="Category",
            yaxis_title="Total Quantity Sold",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend_title_text="Sub-Category",
            margin=dict(l=60, r=40, t=60, b=60)
        )

        fig.update_traces(textposition='inside', textfont_size=11)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Segment Analysis by Category and Sub-Category")

        # --- Group Data ---
        quantity_by_cat = (
            filtered_data.groupby(['Category', 'Sub-Category'])['Quantity']
            .sum()
            .reset_index()
        )

        # --- FIXED: Use transform instead of apply ---
        quantity_by_cat['Percentage'] = quantity_by_cat.groupby('Category')['Quantity'].transform(
            lambda x: x / x.sum() * 100
        )

        # --- Create 100% Stacked Bar Chart ---
        fig = px.bar(
            quantity_by_cat,
            x='Category',
            y='Percentage',
            color='Sub-Category',
            hover_name='Sub-Category',
            title='Segment Analysis: Sub-Category Contribution within Each Category',
            text=quantity_by_cat['Percentage'].apply(lambda x: f"{x:.1f}%"),
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_layout(
            barmode='stack',
            template='plotly_white',
            title_font=dict(size=16, color='black', family='Arial Black'),
            xaxis_title="Category",
            yaxis_title="Percentage Contribution (%)",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend_title_text="Sub-Category",
            yaxis=dict(ticksuffix="%"),
            margin=dict(l=60, r=40, t=60, b=60)
        )

        st.plotly_chart(fig, use_container_width=True)
