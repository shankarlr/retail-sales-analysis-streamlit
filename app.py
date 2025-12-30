import pandas as pd
from src.data_loader import load_data
from src.eda import calculate_kpis
from src.charts import (monthly_sales_chart, city_sales_chart, category_sales_chart,
                        top_products_chart, profit_vs_sales_scatter, discount_vs_sales_bubble)

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")
st.title("📊 Professional Retail Sales Analytics Dashboard")

df = load_data("data/retail_sales.csv")

# ---------------- Sidebar Filters ----------------
st.sidebar.header("Filters")

# Date Range
min_date = df["date"].min()
max_date = df["date"].max()
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])
filtered_df = df[(df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))]

# City Filter
if "city" in df.columns:
    cities = st.sidebar.multiselect("Select City", df["city"].unique(), df["city"].unique())
    filtered_df = filtered_df[filtered_df["city"].isin(cities)]

# Category Filter
if "category" in df.columns:
    categories = st.sidebar.multiselect("Select Category", df["category"].unique(), df["category"].unique())
    filtered_df = filtered_df[filtered_df["category"].isin(categories)]

# Subcategory Filter
if "subcategory" in df.columns:
    subcats = st.sidebar.multiselect("Select Sub-Category", df["subcategory"].unique(), df["subcategory"].unique())
    filtered_df = filtered_df[filtered_df["subcategory"].isin(subcats)]

# ---------------- KPIs ----------------
total_sales, total_profit, avg_order_value, total_orders, profit_margin = calculate_kpis(filtered_df)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Sales", f"₹{total_sales:,.0f}")
col2.metric("Total Profit", f"₹{total_profit:,.0f}")
col3.metric("Avg Order Value", f"₹{avg_order_value:,.0f}")
col4.metric("Total Orders", total_orders)
col5.metric("Profit Margin", f"{profit_margin:.2f}%")

st.markdown("---")

# ---------------- Tabs for Charts ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Monthly Sales", "City Sales", "Category Sales",
                                              "Top Products", "Profit vs Sales", "Discount vs Sales"])

with tab1:
    st.plotly_chart(monthly_sales_chart(filtered_df), use_container_width=True)
with tab2:
    chart = city_sales_chart(filtered_df)
    if chart: st.plotly_chart(chart, use_container_width=True)
with tab3:
    chart = category_sales_chart(filtered_df)
    if chart: st.plotly_chart(chart, use_container_width=True)
with tab4:
    chart = top_products_chart(filtered_df)
    if chart: st.plotly_chart(chart, use_container_width=True)
with tab5:
    st.plotly_chart(profit_vs_sales_scatter(filtered_df), use_container_width=True)
with tab6:
    st.plotly_chart(discount_vs_sales_bubble(filtered_df), use_container_width=True)

# ---------------- Raw Data ----------------
with st.expander("View Raw Data"):
    st.dataframe(filtered_df)
