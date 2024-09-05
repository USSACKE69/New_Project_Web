import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el archivo CSV del conjunto de datos en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Vehículos Usados en EE.UU.')

# Mostrar el dataframe de forma opcional
st.write("Vista previa de los datos:")
st.write(df.head())

# Casilla de verificación para el histograma de precios
if st.checkbox('Mostrar distribución de precios'):
    fig = px.histogram(df, x='price', title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig)

# Casilla de verificación para el gráfico de dispersión (relación entre año y precio)
if st.checkbox('Mostrar relación Año - Precio'):
    fig2 = px.scatter(df, x='model_year', y='price', title='Relación entre Año del Vehículo y Precio')
    st.plotly_chart(fig2)


