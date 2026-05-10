import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Dashboard Universitario", layout="centered")
st.title("Dashboard Universitario")

df = pd.read_csv("university_student_data.csv")

# Creamos los filtros 
col1, col2 = st.columns([2, 1])

with col1:
    term_seleccionado = st.selectbox("Seleccioná el período estudiantil", df["Term"].unique())

with col2:
    show_grid = st.checkbox("Mostrar cuadrícula", value=True)

df_filtrado = df[df["Term"] == term_seleccionado]

# KPI cards
col_a, col_b, col_c = st.columns(3)
col_a.metric("Promedio Retencion", f"{df_filtrado['Retention Rate (%)'].mean():.1f}%")
col_b.metric("Promedio Satisfaccion", f"{df_filtrado['Student Satisfaction (%)'].mean():.1f}%")
col_c.metric("Total Inscriptos", f"{df_filtrado['Enrolled'].sum()}")

# Grafico - Tasa de retencion de estudiantes
Tasa_retencion = df_filtrado.groupby("Year")["Retention Rate (%)"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
Tasa_retencion.plot(ax=ax, title="Tasa de Retencion a lo largo del tiempo", xlabel="Año", ylabel="Tasa de Retencion (%)")
ax.grid(show_grid)
st.pyplot(fig)

# Grafico  - Satisfaccion estudiantil
Satisfaccion_estudiantil = df_filtrado.groupby("Year")["Student Satisfaction (%)"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
Satisfaccion_estudiantil.plot(ax=ax, title="Satisfaccion estudiantil por año", xlabel="Año", ylabel="Satisfaccion (%)")
ax.grid(show_grid)
st.pyplot(fig)

# Spring y Fall - grafico (usa df completo para mostrar ambos periodos)
Analisis_term = df.groupby(["Year", "Term"])["Retention Rate (%)"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
Analisis_term.unstack().plot(ax=ax, kind="bar", title="Retencion por periodo", xlabel="Año", ylabel="Porcentaje de Retencion")
plt.legend(loc="best")
ax.grid(show_grid)
st.pyplot(fig)

# Distibucion de inscriptos por dpto - grafico torta
columnas_dpto = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
totales = df_filtrado[columnas_dpto].sum()
fig, ax = plt.subplots(figsize=(7, 7))
totales.plot(ax=ax, kind="pie", title="Distribucion de inscriptos por departamento", autopct="%1.1f%%")
st.pyplot(fig)

# Tabla de datos
tab1, tab2 = st.tabs(["Datos filtrados", "Datos completos"])
with tab1:
    st.dataframe(df_filtrado.reset_index(drop=True), use_container_width=True)
with tab2:
    st.dataframe(df, use_container_width=True)
