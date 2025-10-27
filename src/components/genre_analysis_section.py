import streamlit as st
import plotly.express as px


def genre_analysis_section(df):
    
    st.title("Analysis Game Map Gender")

    st.dataframe(df)

    type = st.radio("Choose The Graph:", ["Pie-chart", "Treemap", "Donut"], horizontal=True)

    if type == "Pie-chart":
        data_pie = df.groupby("genre")["hours_avg"].sum().reset_index()
        fig = px.pie(data_pie, names="genre", values="hours_avg")
    elif type == "Treemap":
        fig = px.treemap(df, path=["genre", "title"], values="hours_avg", color="genre")
    else:
        data_donut = df.groupby("genre")["hours_avg"].sum().reset_index()
        fig = px.pie(data_donut, names="genre", values="hours_avg", hole=0.50)

    st.plotly_chart(fig, use_container_width=True)

