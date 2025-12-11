import plotly.express as px

def monthly_sales_chart(df):
    monthly = df.groupby(df["date"].dt.to_period("M"))["totalsales"].sum().reset_index()
    monthly["date"] = monthly["date"].dt.to_timestamp()
    return px.line(monthly, x="date", y="totalsales", title="Monthly Sales Trend", markers=True)

def city_sales_chart(df):
    if "city" in df.columns:
        city_df = df.groupby("city")["totalsales"].sum().reset_index()
        return px.pie(city_df, names="city", values="totalsales", title="City-wise Sales")
    return None

def category_sales_chart(df):
    if "category" in df.columns:
        cat_df = df.groupby("category")["totalsales"].sum().reset_index()
        return px.bar(cat_df, x="category", y="totalsales", title="Category-wise Sales", text_auto=True, color="totalsales", color_continuous_scale="Viridis")
    return None

def top_products_chart(df):
    if "subcategory" in df.columns:
        top_df = df.groupby("subcategory")["totalsales"].sum().sort_values(ascending=False).head(10).reset_index()
        return px.bar(top_df, x="subcategory", y="totalsales", title="Top 10 Products", text_auto=True, color="totalsales", color_continuous_scale="Plasma")
    return None

def profit_vs_sales_scatter(df):
    if "profit" in df.columns and "totalsales" in df.columns:
        return px.scatter(df, x="totalsales", y="profit", color="category" if "category" in df.columns else None,
                          title="Profit vs Sales", hover_data=["subcategory", "city"], size="totalsales")

def discount_vs_sales_bubble(df):
    if "discount" in df.columns:
        return px.scatter(df, x="discount", y="totalsales", size="totalsales", color="category" if "category" in df.columns else None,
                          title="Discount vs Sales", hover_data=["subcategory", "city"])
