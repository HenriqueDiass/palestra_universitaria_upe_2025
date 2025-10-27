# Home.py
import streamlit as st

# --- Configuração da Página ---
# (Isso deve ser o primeiro comando Streamlit em sua Home.py)
st.set_page_config(
    page_title="Home | Análise de Alunos UPE",
    page_icon="🎓",
    layout="wide"
)
col_titulo, col_logo = st.columns([0.6, 0.3])

with col_titulo:
    st.title("🎓 Análise de Distribuição de Alunos")
    st.subheader("Bem-vindo ao painel de análise geográfica dos estudantes!")
    st.markdown("""
Esta aplicação foi desenvolvida para a palestra universitária, com o objetivo de
demonstrar o poder do Streamlit e PyDeck na criação de visualizações de dados interativas.
""")
    st.markdown("""
Explore as diferentes análises usando o menu na barra lateral.
""")

with col_logo:
        st.image("data/logo_upe.png", width=450) 


st.divider() 

st.header("O que você encontrará aqui?")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True): # Cria um container com borda
        st.subheader("🗺️ Mapa de Densidade 3D")
        st.write("""
        Explore a concentração de alunos em um mapa 3D interativo. 
        Esta visualização usa 'HexagonLayer' do PyDeck para agrupar
        alunos por região, mostrando "prédios" 3D onde há maior densidade.
        """)
        # Botão que leva diretamente para a página
        st.link_button("Ir para o Mapa 3D", url="mapa-3d")

# Cartão 2: Mapa de Estudantes
with col2:
    with st.container(border=True): # Cria um container com borda
        st.subheader("📍 Mapa de Localização Individual")
        st.write("""
        Veja a localização individual de cada estudante. Esta visualização
        usa 'ScatterplotLayer' para plotar um ponto para cada aluno,
        permitindo ver a distribuição exata e filtrar por campus.
        """)
        # Botão que leva diretamente para a página
        st.link_button("Ir para o Mapa de Estudantes", url="mapa-estudantes")


col3, col4 = st.columns(2)

# Cartão 3: Análise de Gênero (Pie/Treemap/Donut)
with col3:
    with st.container(border=True):
        st.subheader("📊 Análise por Gênero de Jogo")
        st.write("""
        Analise a distribuição de horas jogadas por gênero.
        Escolha entre gráficos de Pizza (Pie-chart), Mapa de Árvore (Treemap)
        ou Rosca (Donut) para ver quais categorias são mais jogadas.
        """)
        # URL baseada no arquivo: pages/grafico_one.py (ou o novo nome que você deu)
        st.link_button("Ir para Análise de Gênero", url="grafico_one")

# Cartão 4: Top 10 Jogos (Barras + KPIs)
with col4:
    with st.container(border=True):
        st.subheader("🏆 Top 10 Jogos Mais Jogados")
        st.write("""
        Descubra os 10 jogos com as maiores médias de horas jogadas.
        Este painel inclui um gráfico de barras e KPIs (Metascore,
        Preço Médio e Total de Horas) para uma análise rápida.
        """)
        # URL baseada no arquivo: pages/grafico_ois.py (ou o novo nome que você deu)
        st.link_button("Ir para o Top 10", url="grafico_ois")