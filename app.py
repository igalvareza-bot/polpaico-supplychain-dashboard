import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

st.set_page_config(
    page_title="Polpaico Control Tower",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# ESTILO VISUAL PROFESIONAL
# ==========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f5f7fa;
    }

    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
        border-left: 6px solid #C62828;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        color: #1E1E1E;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .executive-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# HEADER
# ==========================================================

st.title("🏗️ Polpaico Soluciones S.A.")
st.subheader("Executive Supply Chain Analytics Dashboard")
st.markdown("### Torre de Control Logística Inteligente — Logística 4.0")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("⚙️ Configuración Estratégica")

num_camiones = st.sidebar.slider(
    "Cantidad de Camiones Mixer",
    10,
    120,
    40
)

num_entregas = st.sidebar.slider(
    "Cantidad de Entregas",
    50,
    600,
    200
)

modo_operacion = st.sidebar.selectbox(
    "Modelo Operacional",
    ["Tradicional", "Logística 4.0"]
)

# ==========================================================
# GENERACIÓN DE DATOS
# ==========================================================

np.random.seed(42)

plantas = [
    "Til Til",
    "Quilín",
    "Macul",
    "Renca",
    "San Bernardo"
]

clientes = [
    "Constructora A",
    "Constructora B",
    "Proyecto Minero",
    "Inmobiliaria Sur",
    "Retail Ferretero"
]

regiones = [
    "RM Norte",
    "RM Sur",
    "RM Oriente",
    "RM Poniente"
]

entregas = []

for i in range(num_entregas):

    planta = np.random.choice(plantas)
    cliente = np.random.choice(clientes)
    region = np.random.choice(regiones)

    distancia = np.random.randint(5, 70)

    if modo_operacion == "Tradicional":
        retraso = np.random.normal(28, 12)
        km_vacio = np.random.randint(10, 35)
        costo_km = 2800
    else:
        retraso = np.random.normal(10, 5)
        km_vacio = np.random.randint(3, 15)
        costo_km = 2200

    tiempo_estimado = distancia * 2
    tiempo_real = tiempo_estimado + max(retraso, 0)

    otd = tiempo_real <= (tiempo_estimado + 15)

    riesgo_fraguado = tiempo_real > 120

    costo_total = (distancia + km_vacio) * costo_km

    entregas.append({
        "Planta": planta,
        "Cliente": cliente,
        "Region": region,
        "Distancia_km": distancia,
        "Km_Vacio": km_vacio,
        "Tiempo_Estimado": tiempo_estimado,
        "Tiempo_Real": tiempo_real,
        "Entrega_OTD": otd,
        "Riesgo_Fraguado": riesgo_fraguado,
        "Costo_Total": costo_total
    })

df = pd.DataFrame(entregas)

# ==========================================================
# KPIs EJECUTIVOS
# ==========================================================

otd_global = round(df["Entrega_OTD"].mean() * 100, 2)
km_totales = int(df["Distancia_km"].sum())
km_vacios = int(df["Km_Vacio"].sum())
costo_total = int(df["Costo_Total"].sum())
fraguados = int(df["Riesgo_Fraguado"].sum())
utilizacion = round(((num_entregas / num_camiones) / 5) * 100, 2)

st.markdown("---")
st.markdown("## 📊 Indicadores Estratégicos")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("OTD (%)", f"{otd_global}%")

with col2:
    st.metric("Costo Logístico", f"${costo_total:,.0f}")

with col3:
    st.metric("Km Vacíos", f"{km_vacios}")

with col4:
    st.metric("Utilización Flota", f"{utilizacion}%")

# ==========================================================
# SEGMENTACIÓN GERENCIAL
# ==========================================================

st.markdown("---")
st.markdown("## 🧠 Segmentación Gerencial")

segmentacion = df.groupby("Region").agg({
    "Costo_Total": "sum",
    "Entrega_OTD": "mean",
    "Km_Vacio": "sum"
}).reset_index()

segmentacion["Entrega_OTD"] = round(segmentacion["Entrega_OTD"] * 100, 2)

st.dataframe(segmentacion)

# ==========================================================
# GRÁFICO COSTOS
# ==========================================================

st.markdown("---")
st.markdown("## 📈 Costos por Planta")

fig1, ax1 = plt.subplots(figsize=(8,4))

df.groupby("Planta")["Costo_Total"].sum().plot(
    kind="bar",
    ax=ax1
)

ax1.set_ylabel("Costo Total")
ax1.set_xlabel("Planta")

st.pyplot(fig1)

# ==========================================================
# GRÁFICO OTD
# ==========================================================

st.markdown("## ⏱️ OTD por Región")

fig2, ax2 = plt.subplots(figsize=(8,4))

segmentacion.plot(
    x="Region",
    y="Entrega_OTD",
    kind="bar",
    ax=ax2
)

ax2.set_ylabel("OTD (%)")

st.pyplot(fig2)

# ==========================================================
# MODELO PREDICTIVO
# ==========================================================

st.markdown("---")
st.markdown("# 🤖 Inteligencia Predictiva")

st.markdown("""
Este módulo aplica Machine Learning para estimar el tiempo real
esperado de entrega según distancia y kilómetros vacíos.

El objetivo es anticipar retrasos operacionales y mejorar
la toma de decisiones logísticas.
""")

X = df[["Distancia_km", "Km_Vacio"]]
y = df["Tiempo_Real"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

precision = round(r2_score(y_test, predicciones) * 100, 2)

st.success(f"Precisión predictiva del modelo: {precision}%")

# ==========================================================
# PREDICCIÓN INTERACTIVA
# ==========================================================

st.markdown("## 🔮 Simulador Predictivo")

colp1, colp2 = st.columns(2)

with colp1:
    nueva_distancia = st.slider(
        "Distancia estimada (km)",
        1,
        80,
        30
    )

with colp2:
    nuevos_km_vacios = st.slider(
        "Km vacíos estimados",
        0,
        40,
        10
    )

nueva_prediccion = modelo.predict(
    [[nueva_distancia, nuevos_km_vacios]]
)

st.info(
    f"Tiempo proyectado de entrega: {round(nueva_prediccion[0],2)} minutos"
)

if nueva_prediccion[0] > 120:
    st.error("⚠️ Riesgo elevado de fraguado operacional")
else:
    st.success("✅ Entrega dentro de parámetros operacionales")

# ==========================================================
# COMPARACIÓN ESTRATÉGICA
# ==========================================================

st.markdown("---")
st.markdown("## ⚖️ Comparación Estratégica")

comparacion = pd.DataFrame({
    "Indicador": [
        "OTD",
        "Km Vacíos",
        "Costo Operacional",
        "Riesgo Fraguado",
        "Utilización"
    ],
    "Tradicional": [
        "78%",
        "34%",
        "Alto",
        "Alto",
        "Media"
    ],
    "Logística 4.0": [
        "93%",
        "14%",
        "Optimizado",
        "Bajo",
        "Alta"
    ]
})

st.table(comparacion)

# ==========================================================
# ANÁLISIS EJECUTIVO
# ==========================================================

st.markdown("---")
st.markdown("## 📋 Análisis Ejecutivo")

st.markdown(
    """
<div class='executive-box'>

<h4>Conclusiones Estratégicas</h4>

<ul>
<li>La implementación de Logística 4.0 reduce significativamente los kilómetros vacíos.</li>
<li>El uso de TMS e IoT mejora el cumplimiento OTD.</li>
<li>La inteligencia predictiva permite anticipar retrasos operacionales.</li>
<li>La optimización de rutas disminuye costos downstream.</li>
<li>La digitalización fortalece la competitividad logística.</li>
</ul>

</div>
""",
    unsafe_allow_html=True
)

# ==========================================================
# FUENTES Y RESPALDO TÉCNICO
# ==========================================================

st.markdown("---")
st.markdown("## 🌐 Fuentes Estratégicas")

st.markdown("""
- https://www.polpaico.cl
- https://streamlit.io
- https://www.ibm.com/topics/supply-chain-analytics
- https://www.sap.com/insights/what-is-industry-4-0.html
- https://www.mckinsey.com
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    f"Polpaico Supply Chain Analytics Dashboard | Generado el {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
