import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de anuncios de autos - Streamlit")

car_data = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.write('Gráfico de dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
    