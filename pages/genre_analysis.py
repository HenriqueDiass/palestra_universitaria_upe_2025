# pages/genre_analysis.py

import streamlit as st
from src.components.genre_analysis_section import genre_analysis_section
from src.components.utils import load_games  


st.title("Top rank")

df = load_games()
genre_analysis_section(df)