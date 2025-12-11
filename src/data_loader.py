import pandas as pd

def load_data(path: str):
    """
    Load retail sales dataset and standardize column names for Streamlit dashboard.
    """
    try:
        df = pd.read_csv(path, encoding="latin1")
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="ISO-8859-1")

    df.columns = df.columns.str.strip().str.lower()

    rename_map = {
        "order id": "orderid",
        "order date": "date",
        "city": "city",
        "category": "category",
        "sub-category": "subcategory",
        "sales": "totalsales",
        "profit": "profit",
        "quantity": "quantity",
        "discount": "discount"
    }
    df = df.rename(columns=rename_map)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "totalsales" not in df.columns and "quantity" in df.columns and "unit price" in df.columns:
        df["totalsales"] = df["quantity"] * df["unit price"]

    if "profit" not in df.columns:
        df["profit"] = 0

    if "orderid" not in df.columns:
        df["orderid"] = range(1, len(df) + 1)

    if "discount" not in df.columns:
        df["discount"] = 0

    return df
