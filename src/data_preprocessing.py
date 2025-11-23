"""
Data preprocessing:
- Load raw CSV
- Clean and validate fields
- Prepare processed dataset for analysis
"""

import pandas as pd


def load_raw_data(path):
    return pd.read_csv(path)


def clean_data(df):
    df = df.copy()
    df.dropna(subset=["variant", "converted"], inplace=True)
    df["variant"] = df["variant"].astype(str).str.upper()
    df["converted"] = df["converted"].astype(int)
    return df


def split_by_variant(df):
    a = df[df["variant"] == "A"]
    b = df[df["variant"] == "B"]
    return a, b
