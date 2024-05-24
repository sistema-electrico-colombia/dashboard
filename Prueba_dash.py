import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Configuración inicial del layout de la página
st.set_page_config(
                   page_title="Sistema electrico Colombiano", #Titulo de la pagina
                 page_icon=":globe_with_meridians:", #Icono de la pagina
             layout="wide" ) #Diseño de la pagina

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("power_system.csv",low_memory=False)
df_plot = df.copy()
df_plot['Date'] = pd.to_datetime(df_plot['Date'])
df_plot['Year'] = df_plot['Date'].dt.year
df_plot['Month'] = df_plot['Date'].dt.month
fig, axes = plt.subplots(figsize=(12, 6))
sns.lineplot(ax=axes, data=df_plot, x='Date', y='daily_emision_CO2_eq')
axes.set_title('Emisiones CO2 Equivalente')
axes.set_ylabel('Toneladas CO2 eq')
axes.set_xlabel('Fecha')
from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y")
axes.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)
plt.show()

#Grafica 2

fig, axes = plt.subplots(figsize=(12, 6))
sns.lineplot(ax=axes, data=df_plot, x='Date', y='daily_aportes_energia')
axes.set_title('Aportes de energia')
axes.set_ylabel('Energía (GWh)')
axes.set_xlabel('Fecha')
from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y-%m")
axes.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)
plt.show()

# Grafica 3

fig, axes = plt.subplots(figsize=(12, 6))
sns.lineplot(ax=axes, data=df_plot, x='Date', y='daily_volumen_util_energia')
axes.set_title('Volumen Util de Energia')
axes.set_ylabel('Energía (GWh)')
axes.set_xlabel('Fecha')
from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y-%m")
axes.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)
plt.show()

#Grafica 4

fig, axes = plt.subplots(figsize=(12, 6))
sns.lineplot(ax=axes, data=df_plot, x='Date', y="daily_precio_bolsa")
axes.set_title('Volumen Util de Energia')
axes.set_ylabel('Energía (GWh)')
axes.set_xlabel('COP/kWh')
from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y-%m")
axes.xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)
plt.show()

df = pd.read_csv("power_system.csv",low_memory=False)

# Crear una aplicación de Streamlit
st.title("Sistema Electrico Colombiano")
st.subheader("Por: Julián Andrés Santos Méndez ,Juan Felipe Sepulveda Mantilla, Luz Edilsa Ortiz Lopez,Julian Obando Scarpetta")
st.divider()

default_years = [2020, 2019,2018]
default_months = [1, 2]
# Filtrar el DataFrame según el año y mes seleccionados por el usuario
selected_years = st.sidebar.multiselect("Seleccione los años", df_plot['Year'].unique(), default=default_years)
selected_months = st.sidebar.multiselect("Seleccione los meses", range(1, 13), default=default_months)
if not selected_months:
    selected_months = list(range(1, 13))

filtered_df = df_plot[(df_plot['Year'].isin(selected_years)) & (df_plot['Month'].isin(selected_months))]

# Crear columnas para la presentación de los gráficos
col1, col2, col3 = st.columns([2, 0.2, 2])

with st.container():
    col1, col2, col3 = st.columns([1, 0.1, 1])

    with col1:
        st.subheader("Emisiones CO2 EQUIVALENTE")
        fig, axes = plt.subplots()
        sns.lineplot(ax=axes, data=filtered_df, x='Date', y='daily_emision_CO2_eq')
        axes.set_title('Emisiones CO2 Equivalente')
        axes.set_ylabel('Toneladas CO2 eq')
        axes.set_xlabel("fecha")
        st.pyplot(fig)

    with col3:
        st.subheader("Aportes de Energia")
        fig2, axes2 = plt.subplots()
        sns.lineplot(ax=axes2, data=filtered_df, x='Date', y='daily_aportes_energia')
        axes2.set_title('Aportes de energia')
        axes2.set_ylabel('Energía (GWh)')
        axes2.set_xlabel("fecha")
        st.pyplot(fig2)

st.divider()
with st.container():
    col4, col5, col6 = st.columns([1, 0.1, 1])

    with col4:
        st.subheader("Energia Util")
        fig3, axes3 = plt.subplots()
        sns.lineplot(ax=axes3, data=filtered_df, x='Date', y='daily_volumen_util_energia')
        axes3.set_title('Energia Util')
        axes3.set_ylabel('Energía (GWh)')
        axes3.set_xlabel("fecha")
        st.pyplot(fig3)

    with col6:
        st.subheader("Precio Bolsa")
        fig4, axes4 = plt.subplots()
        sns.lineplot(ax=axes4, data=filtered_df, x='Date', y="daily_precio_bolsa")
        axes4.set_title('Precio Bolsa')
        axes4.set_ylabel('COP/kWh')
        axes4.set_xlabel("fecha")
        st.pyplot(fig4)

