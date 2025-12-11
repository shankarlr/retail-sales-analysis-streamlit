def calculate_kpis(df):
    """
    Calculate professional KPIs:
    Total Sales, Total Profit, Avg Order Value, Total Orders, Profit Margin (%)
    """
    total_sales = float(df["totalsales"].sum())
    total_profit = float(df["profit"].sum())
    avg_order_value = float(df["totalsales"].mean())
    total_orders = df["orderid"].nunique()
    profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

    return total_sales, total_profit, avg_order_value, total_orders, profit_margin
