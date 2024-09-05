import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.title('Análisis de Vehículos Usados en EE.UU.')

# Texto introductorio
st.markdown("""
### Bienvenido a la aplicación de análisis de vehículos usados.
Esta aplicación te permite explorar un conjunto de datos de anuncios de venta de coches en EE.UU. Utiliza los filtros en la barra lateral para ajustar el análisis a tus necesidades.
""")

# Barra lateral con filtros
st.sidebar.header('Filtros')
price_range = st.sidebar.slider('Selecciona el rango de precios', 0, int(df['price'].max()), (5000, 30000))
selected_model = st.sidebar.selectbox('Selecciona el modelo de vehículo', df['model'].unique())

# Texto sobre la funcionalidad de los filtros
st.write(f"Mostrando resultados para el modelo seleccionado: **{selected_model}** en el rango de precios: **{price_range[0]} - {price_range[1]}**")

# Mostrar los datos filtrados
filtered_data = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) & (df['model'] == selected_model)]
st.write("A continuación se muestran los primeros 5 registros de los datos filtrados:")
st.write(filtered_data.head())

# Descripción del histograma
st.markdown("""
### Distribución de Precios de Vehículos
Selecciona la casilla de verificación para ver el histograma de la distribución de precios de los vehículos filtrados.
""")
if st.sidebar.checkbox('Mostrar distribución de precios'):
    fig = px.histogram(filtered_data, x='price', title=f'Distribución de Precios para {selected_model}')
    st.plotly_chart(fig)

# Descripción del gráfico de dispersión
st.markdown("""
### Relación entre Año y Precio
Selecciona la casilla de verificación para ver la relación entre el año del vehículo y su precio.
""")
if st.sidebar.checkbox('Mostrar relación Año - Precio'):
    fig2 = px.scatter(filtered_data, x='model_year', y='price', title=f'Relación Año - Precio para {selected_model}')
    st.plotly_chart(fig2)




