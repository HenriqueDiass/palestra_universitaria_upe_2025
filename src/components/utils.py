import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_games(path: str = "data/steam_games.json") -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File Not Found: {path}")
    df = pd.read_json(p)

    return df