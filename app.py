import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Carnes VIP | Premium Meat House",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# ESTILO PRO
# =========================
st.markdown("""
<style>

body {
    background-color: #0f0f0f;
}

.main {
    background-color: #f4f4f4;
}

/* HERO */
.hero {
    background: linear-gradient(90deg, #8B0000, #C62828);
    padding: 40px;
    border-radius: 20px;
    color: white;
    text-align: left;
    margin-bottom: 20px;
}

/* CARD PRODUCTO */
.card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    border-left: 6px solid #C62828;
}

/* BADGE */
.badge {
    background: #C62828;
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
}

/* BOTÓN CONTACTO */
.contact-box {
    background: #111;
    color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>🥩 Carnes VIP</h1>
    <h3>Calidad Premium en Peñalolén</h3>
    <p>Bolívar 6618 | Corte seleccionado | Atención personalizada | Parrilla & hogar</p>
</div>
""", unsafe_allow_html=True)

# =========================
# KPIs VISUALES
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("🔥 Cortes Premium", "25+")
col2.metric("🚚 Delivery", "30–60 min")
col3.metric("⭐ Satisfacción", "4.9/5")

st.divider()

# =========================
# BASE PRODUCTOS
# =========================
productos = pd.DataFrame([
    ["Lomo Vetado", "Vacuno", 12990, "🔥 Parrilla premium"],
    ["Filete", "Vacuno", 15990, "🥩 Corte suave y fino"],
    ["Asado Carnicero", "Vacuno", 8990, "🍖 Tradicional"],
    ["Costillar Cerdo", "Cerdo", 6990, "🍖 Jugoso"],
    ["Pechuga Pollo", "Pollo", 4990, "💪 Alta proteína"],
    ["Chorizos Artesanales", "Embutidos", 5990, "⭐ Especial parrilla"]
], columns=["Producto", "Categoria", "Precio", "Descripcion"])

# =========================
# FILTRO INTELIGENTE
# =========================
categoria = st.selectbox(
    "🔎 Explorar catálogo",
    ["Todos"] + list(productos["Categoria"].unique())
)

if categoria != "Todos":
    productos = productos[productos["Categoria"] == categoria]

# =========================
# CATÁLOGO CON ACORDEÓN (LOOK PRO)
# =========================
st.markdown("## 🥩 Catálogo Premium")

for cat in productos["Categoria"].unique():

    with st.expander(f"📦 {cat}"):
        sub = productos[productos["Categoria"] == cat]

        for _, row in sub.iterrows():
            st.markdown(f"""
            <div class="card">
                <h3>{row['Producto']} <span class="badge">{row['Categoria']}</span></h3>
                <p>{row['Descripcion']}</p>
                <h4 style="color:#C62828;">${row['Precio']:,} / kg</h4>
            </div>
            """, unsafe_allow_html=True)

# =========================
# PROMO ESTILO MARKETING
# =========================
st.divider()

st.markdown("## 🔥 Oferta del Día")

st.warning("""
🥩 PACK PARRILLERO VIP  
- 1kg Lomo Vetado  
- 1kg Asado Carnicero  
- 6 Chorizos Artesanales  

💥 25% DESCUENTO HOY
""")

# =========================
# CONTACTO PRO
# =========================
st.divider()

st.markdown("""
<div class="contact-box">
    <h2>📲 Contacto & Pedidos</h2>
    <p>📍 Bolívar 6618, Peñalolén</p>
    <p>📞 WhatsApp: +56 9 XXXX XXXX</p>
    <p>🚚 Delivery disponible</p>
</div>
""", unsafe_allow_html=True)

# BOTÓN WHATSAPP (SIMULADO)
st.link_button(
    "💬 Pedir por WhatsApp",
    "https://wa.me/569XXXXXXXX"
)
