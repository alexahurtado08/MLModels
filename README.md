# MLModels
Ejemplo de modelos de ML- Modelos supervisados
# Modelos Supervisados de Machine Learning con Python y Streamlit

Este proyecto implementa diferentes **modelos supervisados de Machine Learning** utilizando **Python**.  
La aplicación permite **entrenar, evaluar y visualizar** modelos directamente desde una interfaz web desarrollada en **Streamlit** y desplegada con **GitHub Pages/Streamlit Cloud**.

---

## 📌 Descripción

Los modelos incluidos abarcan algoritmos clásicos de clasificación y regresión, como:

- **Regresión Logística**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machines (SVM)**
- **Árboles de Decisión**
- **Random Forest**
- **Regresión Lineal**

La aplicación permite:

✅ Cargar datasets (CSV).  
✅ Seleccionar un modelo supervisado.  
✅ Dividir el dataset en entrenamiento y prueba.  
✅ Entrenar el modelo y visualizar métricas.  
✅ Mostrar gráficas de desempeño (matriz de confusión, curvas ROC, etc.).  
✅ Descargar resultados y predicciones.  

---

## 🛠️ Requisitos

Antes de ejecutar la aplicación, asegúrate de instalar las dependencias:

```bash
pip install -r requirements.txt

Para ejecutar la aplicación en tu entorno local
streamlit run app.py
