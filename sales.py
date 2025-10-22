import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress non-critical warnings
warnings.filterwarnings("ignore")

def sales_view(filtered_data):
    col1, col2 = st.columns([1, 1])

    # ---- SALES BY CATEGORY ----
    with col1:
        st.subheader("Sales by Category")

        plt.style.use('Solarize_Light2')

        # Group data by Category (Sum of Sales)
        category_by_sales = (
            filtered_data.groupby("Category")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

        # Create figure
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=category_by_sales,
            x="Category",
            y="Sales",
            hue="Category",          # ✅ Fix: avoid palette warning
            palette="pastel",
            legend=False,            # ✅ Suppress legend duplication
            ax=ax
        )

        ax.set_title("Sales by Category", fontsize=14, fontweight='bold')
        ax.set_xlabel("Category", fontsize=12)
        ax.set_ylabel("Sales ($)", fontsize=12)

        # Add values on bars
        for i, v in enumerate(category_by_sales["Sales"]):
            ax.text(i, v + 5000, f"${v:,.0f}", ha='center', fontweight='bold', fontsize=10)

        plt.tight_layout()
        st.pyplot(fig)

    # ---- SALES BY REGION ----
    with col2:
        st.subheader("Sales by Region")

        plt.style.use('Solarize_Light2')

        # Group data by Region
        sales_by_region = (
            filtered_data.groupby("Region")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

        # Create donut chart
        fig, ax = plt.subplots(figsize=(6, 6))

        # Custom autopct function to show % and actual value
        def autopct_format(pct):
            total = sales_by_region["Sales"].sum()
            value = int(round(pct * total / 100.0))
            return f"{pct:.1f}%\n(${value:,.0f})"

        wedges, texts, autotexts = ax.pie(
            sales_by_region["Sales"],
            labels=sales_by_region["Region"],
            autopct=autopct_format,
            startangle=90,
            colors=plt.cm.Pastel1.colors,  # soft pastel colors
            wedgeprops={"edgecolor": "white"}
        )

        # Donut hole
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)

        # Aesthetics
        ax.set_title("Sales by Region", fontsize=14, fontweight="bold")
        ax.axis('equal')  # Ensures circular shape
        plt.tight_layout()

        st.pyplot(fig)
