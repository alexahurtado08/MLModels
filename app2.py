import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA Automático", layout="wide")

st.title("📊 Exploratory Data Analysis (EDA) Automático")

# --- Subida del dataset ---
st.sidebar.header("Carga de Dataset")
archivo_csv = st.sidebar.file_uploader("Sube tu archivo CSV", type=["csv"])

if archivo_csv is not None:
    # Leer dataset
    df = pd.read_csv(archivo_csv)

    st.subheader("📋 Vista previa de los datos originales")
    st.dataframe(df.head())

    # --- Limpieza básica ---
    st.subheader("🧹 Limpieza de datos")

    # Mostrar valores faltantes
    st.write("Valores faltantes por columna:")
    st.write(df.isnull().sum())

    # Selección de método para tratar los NaN
    metodo_faltantes = st.radio(
        "Cómo manejar los valores faltantes?",
        ("Eliminar filas con NaN", "Rellenar con media", "Rellenar con moda", "Mantener"),
        horizontal=True
    )

    if metodo_faltantes == "Eliminar filas con NaN":
        df = df.dropna()
    elif metodo_faltantes == "Rellenar con media":
        df = df.fillna(df.mean(numeric_only=True))
    elif metodo_faltantes == "Rellenar con moda":
        for col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])
    # Si elige "Mantener", no se hace nada

    # Outliers con IQR
    if st.checkbox("Eliminar valores atípicos (IQR)"):
        Q1 = df.quantile(0.25, numeric_only=True)
        Q3 = df.quantile(0.75, numeric_only=True)
        IQR = Q3 - Q1
        mask = ~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
        df = df[mask]

    st.success("✅ Datos limpios listos para el análisis")

    # Mostrar tabla después de limpieza
    st.subheader("📋 Datos después de limpieza")
    st.dataframe(df.head())

    # --- Estadísticas ---
    st.subheader("📊 Estadísticas descriptivas")
    st.write(df.describe(include="all"))

    # --- Visualizaciones ---
    st.sidebar.header("Visualizaciones")
    tipo_grafico = st.sidebar.selectbox(
        "Selecciona el tipo de gráfico",
        ["Histograma", "Gráfico de barras", "Gráfico de dispersión", "Gráfico de pastel", "Tendencia (línea)"]
    )

    st.subheader(f"📈 {tipo_grafico}")

    if tipo_grafico == "Histograma":
        columnas_num = df.select_dtypes(include=np.number).columns
        if len(columnas_num) > 0:
            columna = st.selectbox("Selecciona columna numérica", columnas_num)
            fig, ax = plt.subplots()
            sns.histplot(df[columna], kde=True, ax=ax)
            st.pyplot(fig)
        else:
            st.warning("No hay columnas numéricas disponibles.")

    elif tipo_grafico == "Gráfico de barras":
        columnas_cat = df.select_dtypes(exclude=np.number).columns
        if len(columnas_cat) > 0:
            columna = st.selectbox("Selecciona columna categórica", columnas_cat)
            fig, ax = plt.subplots()
            df[columna].value_counts().plot(kind="bar", ax=ax, color="skyblue")
            st.pyplot(fig)
        else:
            st.warning("No hay columnas categóricas disponibles.")

    elif tipo_grafico == "Gráfico de dispersión":
        columnas_num = df.select_dtypes(include=np.number).columns
        if len(columnas_num) >= 2:
            x = st.selectbox("Eje X", columnas_num, index=0)
            y = st.selectbox("Eje Y", columnas_num, index=1)
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x], y=df[y], ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Se necesitan al menos 2 columnas numéricas.")

    elif tipo_grafico == "Gráfico de pastel":
        columnas_cat = df.select_dtypes(exclude=np.number).columns
        if len(columnas_cat) > 0:
            columna = st.selectbox("Selecciona columna categórica", columnas_cat)
            fig, ax = plt.subplots()
            df[columna].value_counts().plot(kind="pie", autopct='%1.1f%%', ax=ax)
            st.pyplot(fig)
        else:
            st.warning("No hay columnas categóricas disponibles.")

    elif tipo_grafico == "Tendencia (línea)":
        columnas_num = df.select_dtypes(include=np.number).columns
        if len(columnas_num) > 0:
            columna = st.selectbox("Selecciona columna numérica", columnas_num)
            fig, ax = plt.subplots()
            df[columna].plot(kind="line", ax=ax, color="orange")
            st.pyplot(fig)
        else:
            st.warning("No hay columnas numéricas disponibles.")

else:
    st.warning("⚠️ Sube un archivo CSV desde la barra lateral para comenzar el análisis")

