import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carnes VIP", layout="wide")

# =========================
# ESTILO
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f5f5;
}

.card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}

.title {
    font-size: 40px;
    font-weight: bold;
    color: #b71c1c;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<div class='title'>🥩 Carnes VIP</div>", unsafe_allow_html=True)
st.subheader("Calidad Premium en Peñalolén | Bolívar 6618")

st.markdown("📍 Delivery y retiro en tienda | 📲 WhatsApp pedidos")

st.divider()

# =========================
# DATA PRODUCTOS
# =========================
productos = pd.DataFrame([
    ["Lomo Vetado", "Vacuno", 12990, "Premium para parrilla 🔥"],
    ["Asado Carnicero", "Vacuno", 8990, "Ideal para fines de semana"],
    ["Costillar Cerdo", "Cerdo", 6990, "Jugoso y tierno"],
    ["Pechuga Pollo", "Pollo", 4990, "Alta proteína"],
    ["Chorizos Artesanales", "Embutidos", 5990, "Para parrilla ⭐"]
], columns=["Producto", "Categoria", "Precio", "Descripcion"])

# =========================
# FILTRO
# =========================
categoria = st.selectbox("Filtrar categoría", ["Todos"] + list(productos["Categoria"].unique()))

if categoria != "Todos":
    productos = productos[productos["Categoria"] == categoria]

# =========================
# CATALOGO
# =========================
st.markdown("## 🥩 Catálogo")

for _, row in productos.iterrows():
    st.markdown(f"""
    <div class="card">
        <h3>{row['Producto']}</h3>
        <p>{row['Descripcion']}</p>
        <h4 style="color:#b71c1c;">${row['Precio']:,} / kg</h4>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PROMO
# =========================
st.divider()
st.markdown("## 🔥 Promoción del día")
st.success("Pack Parrillero Familiar: 1kg Lomo Vetado + 1kg Costillar + 6 Chorizos = 25% OFF")

# =========================
# UBICACION
# =========================
st.divider()
st.markdown("## 📍 Ubicación")
st.info("Bolívar 6618, Peñalolén, Santiago")
