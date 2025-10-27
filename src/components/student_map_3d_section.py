# /map_functions.py

import streamlit as st
import pandas as pd
import pydeck as pdk

def display_map_generation_section_3d():

    st.info("""
    🗺️ **Explore a Distribuição Geográfica dos Alunos**
    
    Use os controles nesta seção para interagir com o mapa:
    
    * **Selecionar locais:** Escolha uma ou mais cidades. Selecione "Todos" para ver a base completa.
    * **Escolher cor:** Defina a cor dos pontos.
    * **Escolher tamanho:** Ajuste o raio (em metros) dos círculos no mapa.
    """)
    
    df = pd.read_csv("data/alunos_upe.csv")
    centro_lat = df['lat'].mean()
    centro_lon = df['lon'].mean()

    tamanho_selecionado = st.slider(
        "Escolha o tamanho dos pontos (em metros)", 10000, 20000, 5000
    )
    formato_plotagem = st.selectbox(
        "Qual a forma que voce quer plotar a vizualização?",
    ("HexagonLayer", "GridLayer"),
)

    view_state = pdk.ViewState(
        latitude=centro_lat,
        longitude=centro_lon,
        zoom=7,
        pitch=45  
    )
    if formato_plotagem == "HexagonLayer":

        layer = pdk.Layer(
           formato_plotagem,
           data=df,
           get_position='[lon, lat]',
           radius=tamanho_selecionado,  
            elevation_scale=50,
            extruded=True,
           pickable=True,
        )
    else:
        
        layer = pdk.Layer(
            "GridLayer",
            data=df,
            get_position='[lon, lat]',
            cell_size=tamanho_selecionado, 
            elevation_scale=50,
            extruded=True,
            pickable=True,
        )
    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style=None,
        tooltip={"text": "Contagem de Alunos: {elevationValue}"}
    )

    
    st.pydeck_chart(deck, use_container_width=True)