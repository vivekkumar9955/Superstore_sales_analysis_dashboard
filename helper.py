def kpi_total_sales(data):
    return round(data['Sales'].sum(),1)

def kpi_tatal_profit(data):
    return round(data['Profit'].sum(),1)

def kpi_top_category(data):
    top_category = (
        data.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )
    return top_category