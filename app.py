import streamlit as st
from dados_api import previsao_temperatura

cidades ={
    "Jundiaí":[-23.18580483986627, -46.886722066321035],
    "Santana de Parnaíba":[-23.436788523098716, -46.92167252836605],
    "Orlando":[28.546898430844173, -81.39705316429564],
    "Roma":[41.900754657478195, 12.471441187795431]
}

st.sidebar.title("Previsão do tempo")
st.sidebar.image('logo.png')

cidade = st.sidebar.selectbox("Escolha a cidade:", cidades.keys())
latitude,  longitude = cidades[cidade]

st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

dados, temeperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temeperatura_media.iterrows():
    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

    with col2:
        st.metric("Temperatura média", f"{d['temperatura_media']:2f}º")

    with col3:
        if d['temperatura_media'] <10:
            temp = "cold.png"

        elif d['temperatura_media'] <18:
            temp = "cool.png" 

        elif d['temperatura_media'] <25:
            temp = "comfort.png"

        else:
            temp = "warm.png"

        st.image(temp, width=40)                          