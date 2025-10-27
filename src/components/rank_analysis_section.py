import streamlit as st
import plotly.express as px
from src.components.utils import load_games

def rank_analysis_section():
   
    st.title("Analysis: Top 10 More Played")

    df = load_games()
    st.dataframe(df)

    top = df.sort_values("hours_avg", ascending=False).head(10)

    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric("Total Hours Played", int(top["hours_avg"].sum()))
    kpi2.metric("Metascore", f"{top["metascore"].mean():.2f}")
    kpi3.metric("Average Price", f"R${top["price_brl"].mean():.2f}")

    fig = px.bar(top, x="title", y="hours_avg", color="genre", text="hours_avg")
    fig.update_traces(texttemplate="%{text}", textposition="outside")
    fig.update_layout(xaxis_title="", yaxis_title="Average Hours", legend_title_text="Genre")

    st.plotly_chart(fig, use_container_width=True)

