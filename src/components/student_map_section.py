import streamlit as st
import pandas as pd

def display_map_generation_section_student():

    st.info("""
   Explore a localização dos alunos:
    1.  **Selecione** uma ou mais cidades (ou "Todos").
    2.  **Escolha** uma cor e o tamanho para os marcadores.
    """)

    df = pd.read_csv("data/alunos_upe.csv")
    st.subheader("Controles do Mapa")
    
    opcoes_locais = ["Todos"] + df['cidade'].unique().tolist()
    
    selecao_usuario = st.multiselect(
        "Selecione os locais para visualizar",
        options=opcoes_locais,
        default=["Todos"]
    )
    
    cor_selecionada = st.color_picker(
        "Escolha uma cor para os pontos", "#4C00FF"
    )

    tamanho_selecionado = st.slider(
        "Escolha o tamanho dos pontos (em metros)", 10, 200, 50
    )
    
    if not selecao_usuario: 
        df_filtrado = df.iloc[0:0] 
    elif "Todos" in selecao_usuario: 
        df_filtrado = df 
    else: 
        df_filtrado = df[df['cidade'].isin(selecao_usuario)]
        
    df_filtrado["cor_ponto"] = cor_selecionada
    df_filtrado["tamanho_circulo"] = tamanho_selecionado
        
    st.map(
        data=df_filtrado,
        latitude="lat", 
        longitude="lon",
        size="tamanho_circulo", 
        color="cor_ponto", 
    
    )
