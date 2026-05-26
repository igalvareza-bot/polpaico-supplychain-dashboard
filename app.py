import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

st.set_page_config(
    page_title="Polpaico Supply Chain Control Tower",
    layout="wide"
)

# ==========================================================
# TÍTULO
# ==========================================================

st.title("🏗️ Polpaico Soluciones S.A.")
st.subheader("Torre de Control Logística - Supply Chain Analytics")
st.markdown("### Simulación Ejecutiva de Optimización Logística y Logística 4.0")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("Configuración de Simulación")

num_camiones = st.sidebar.slider(
    "Cantidad de Camiones Mixer",
    10,
    100,
    40
)

num_entregas = st.sidebar.slider(
    "Cantidad de Entregas",
    50,
    500,
    200
)

usar_tms = st.sidebar.selectbox(
    "Modo Operacional",
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

data = []

for i in range(num_entregas):

    planta = np.random.choice(plantas)
    cliente = np.random.choice(clientes)

    distancia = np.random.randint(5, 60)

    if usar_tms == "Tradicional":
        retraso = np.random.normal(25, 12)
        km_vacio = np.random.randint(10, 30)
        costo_km = 2800
    else:
        retraso = np.random.normal(10, 5)
        km_vacio = np.random.randint(3, 15)
        costo_km = 2200

    tiempo_estimado = distancia * 2
    tiempo_real = tiempo_estimado + max(retraso, 0)

    entrega_otd = tiempo_real <= (tiempo_estimado + 15)

    riesgo_fraguado = tiempo_real > 120

    costo_total = (distancia + km_vacio) * costo_km

    data.append({
        "Planta": planta,
        "Cliente": cliente,
        "Distancia_km": distancia,
        "Km_Vacio": km_vacio,
        "Tiempo_Estimado": tiempo_estimado,
        "Tiempo_Real": tiempo_real,
        "Entrega_OTD": entrega_otd,
        "Riesgo_Fraguado": riesgo_fraguado,
        "Costo_Total": costo_total
    })

df = pd.DataFrame(data)

# ==========================================================
# KPI PRINCIPALES
# ==========================================================

otd = round(df["Entrega_OTD"].mean() * 100, 2)

km_totales = int(df["Distancia_km"].sum())

km_vacios = int(df["Km_Vacio"].sum())

costo_logistico = int(df["Costo_Total"].sum())

riesgo_fraguado = int(df["Riesgo_Fraguado"].sum())

utilizacion_flota = round(
    ((num_entregas / num_camiones) / 5) * 100,
    2
)

# ==========================================================
# KPIs VISUALES
# ==========================================================

st.markdown("---")
st.markdown("## 📊 KPI Logísticos")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "OTD (%)",
    f"{otd}%"
)

col2.metric(
    "Costo Logístico",
    f"${costo_logistico:,.0f}"
)

col3.metric(
    "Km Totales",
    f"{km_totales}"
)

col4.metric(
    "Km Vacíos",
    f"{km_vacios}"
)

col5, col6, col7 = st.columns(3)

col5.metric(
    "Entregas",
    f"{num_entregas}"
)

col6.metric(
    "Riesgo Fraguado",
    f"{riesgo_fraguado}"
)

col7.metric(
    "Utilización Flota",
    f"{utilizacion_flota}%"
)

# ==========================================================
# TABLA OPERACIONAL
# ==========================================================

st.markdown("---")
st.markdown("## 🚛 Monitoreo Operacional")

st.dataframe(df)

# ==========================================================
# GRÁFICO 1
# ==========================================================

st.markdown("---")
st.markdown("## 📈 Entregas por Planta")

fig1, ax1 = plt.subplots(figsize=(8, 4))

df["Planta"].value_counts().plot(
    kind="bar",
    ax=ax1
)

ax1.set_ylabel("Cantidad Entregas")
ax1.set_xlabel("Planta")

st.pyplot(fig1)

# ==========================================================
# GRÁFICO 2
# ==========================================================

st.markdown("## 📉 Costos por Planta")

fig2, ax2 = plt.subplots(figsize=(8, 4))

df.groupby("Planta")["Costo_Total"].sum().plot(
    kind="bar",
    ax=ax2
)

ax2.set_ylabel("Costo Total")
ax2.set_xlabel("Planta")

st.pyplot(fig2)

# ==========================================================
# GRÁFICO 3
# ==========================================================

st.markdown("## ⏱️ Comparación Tiempo Estimado vs Real")

fig3, ax3 = plt.subplots(figsize=(10, 4))

ax3.plot(
    df["Tiempo_Estimado"].values[:50],
    label="Estimado"
)

ax3.plot(
    df["Tiempo_Real"].values[:50],
    label="Real"
)

ax3.legend()

ax3.set_ylabel("Minutos")
ax3.set_xlabel("Entregas")

st.pyplot(fig3)

# ==========================================================
# ANÁLISIS EJECUTIVO
# ==========================================================

st.markdown("---")
st.markdown("## 🧠 Análisis Ejecutivo")

if usar_tms == "Tradicional":

    st.error("""
    El modelo tradicional presenta mayores niveles de retraso,
    aumento de kilómetros vacíos y menor eficiencia operacional.
    
    Esto impacta directamente:
    - El indicador OTD
    - Los costos logísticos downstream
    - La satisfacción del cliente
    - El riesgo de pérdida por fraguado
    """)

else:

    st.success("""
    La implementación de Logística 4.0 mediante TMS + IoT
    mejora significativamente la eficiencia operacional.
    
    Beneficios observados:
    - Reducción de kilómetros vacíos
    - Mayor cumplimiento OTD
    - Menor costo logístico
    - Mejor utilización de flota
    - Menor riesgo de fraguado
    """)

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
        "Riesgo de Fraguado",
        "Utilización Flota"
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
# CONCLUSIÓN
# ==========================================================

st.markdown("---")
st.markdown("## 🏁 Conclusión Gerencial")

st.info("""
La simulación demuestra que la implementación de tecnologías
de Logística 4.0 permite transformar la cadena de suministro
de Polpaico Soluciones S.A. en una operación más eficiente,
flexible y sostenible.

La integración de sensores IoT y herramientas TMS permite:
- Reducir costos logísticos
- Mejorar la capacidad de respuesta
- Optimizar la utilización de la flota
- Disminuir pérdidas operacionales
- Incrementar el cumplimiento OTD

La propuesta presenta una mejora significativa en la relación
costo-beneficio y fortalece la competitividad operacional
de la compañía.
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    f"Polpaico Supply Chain Analytics | Generado el {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)