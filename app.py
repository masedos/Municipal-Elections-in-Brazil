import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px

DATE_TIME = "date/time"
DATA_URL = ("dataset/municipios.csv")

st.title("Eleições Municipais do Estado de Goiás")
st.markdown("Análise sobre as eleições municípais do Estado de Goiás no ano de 2020")

municipios = pd.read_csv(DATA_URL)
mu_go = municipios.loc[municipios['codigo_uf'] == 52]

go = mu_go[['nome',	'latitude',	'longitude']].reset_index(drop = True)

go.rename(columns={'nome': 'Municípios', 'latitude': 'latitude', 'longitude': 'longitude'}, inplace=True)

st.write('Quantidade de Municípios no Estado de Goiás',go.shape[0])
st.write(go.head(247))
st.map(go)