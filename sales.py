import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", message="Glyph .* missing from font")
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message="Passing `palette` without assigning `hue` is deprecated"
)

# Set style and font globally
plt.style.use('Solarize_Light2')
plt.rcParams['font.family'] = 'Segoe UI Emoji'

def sales_view(filtered_data):
    col1, col2 = st.columns([1, 1])

    # --- Sales by Category ---
    with col1:
        st.subheader("💰 Sales by Category")

        category_by_sales = (
            filtered_data.groupby("Category")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=category_by_sales,
            x="Category",
            y="Sales",
            hue="Category",  # Added
            palette="pastel",
            dodge=False,
            ax=ax
        )

        ax.legend([], [], frameon=False)
        ax.set_title("Sales by Category", fontsize=14, fontweight='bold')
        ax.set_xlabel("Category", fontsize=12)
        ax.set_ylabel("Sales ($)", fontsize=12)

        for i, v in enumerate(category_by_sales["Sales"]):
            ax.text(i, v + 5000, f"${v:,.0f}", ha='center', fontweight='bold')

        st.pyplot(fig)

    # --- Sales by Region ---
    with col2:
        st.subheader("💰 Sales by Region")

        sales_by_region = (
            filtered_data.groupby("Region")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
        )

        fig, ax = plt.subplots(figsize=(6, 6))

        def autopct_format(pct):
            total = sales_by_region["Sales"].sum()
            value = int(round(pct * total / 100.0))
            return f"{pct:.1f}%\n(${value:,.0f})"

        wedges, texts, autotexts = ax.pie(
            sales_by_region["Sales"],
            labels=sales_by_region["Region"],
            autopct=autopct_format,
            startangle=90,
            colors=plt.cm.Pastel1.colors,
            wedgeprops={"edgecolor": "white"}
        )

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)

        ax.set_title("Sales by Region", fontsize=14, fontweight="bold")
        ax.axis('equal')

        st.pyplot(fig)
