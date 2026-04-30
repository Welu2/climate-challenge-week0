import pandas as pd
import streamlit as st
import os

DRIVE_MAP = {
    "Sudan": "15dQYyV6hxkutF7--YQrqoRysS1d0ZjHF",
    "Ethiopia": "1uZ8h-3LGv9eB8opNvBoc_TA6Bcj29iT4",
    "Kenya": "17Dm3wyc9CBBzhSIPBYr8lV5_XSggPPN_",
    "Tanzania": "1TJzZwzRk_BZ4mNDnZZ7OA7pX-8lNJxzy",
    "Nigeria": "1yKJwdRf58HXA6fx561OF3QymY_fhWmI-"
}


def get_drive_url(file_id):
    return f"https://drive.google.com/uc?export=download&id={file_id}"


@st.cache_data
def load_from_drive():
    dfs = []
    for country, file_id in DRIVE_MAP.items():
        try:
            df = pd.read_csv(get_drive_url(file_id))
            df["Country"] = country
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.year
            dfs.append(df)
        except Exception as e:
            print(f"Error loading {country}: {e}")

    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def load_local_data():
    """Fallback for local dev (optional)"""
    path = "data/"
    if not os.path.exists(path):
        return pd.DataFrame()

    dfs = []
    for f in os.listdir(path):
        if f.endswith("_clean.csv"):
            df = pd.read_csv(os.path.join(path, f))
            df["Country"] = f.replace("_clean.csv", "").capitalize()
            df["Date"] = pd.to_datetime(df["Date"])
            df["Year"] = df["Date"].dt.year
            dfs.append(df)

    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def load_all_data():
    """Try Drive first, fallback to local"""
    df = load_from_drive()
    if df.empty:
        df = load_local_data()
    return df