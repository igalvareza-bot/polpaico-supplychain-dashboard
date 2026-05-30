import streamlit as st
from urllib.parse import quote

# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="Carnes VIP",
    page_icon="🥩",
    layout="wide"
)

WHATSAPP_NUMBER = "56981919691"

# =========================
# ESTILO PROFESIONAL
# =========================

st.markdown("""
<style>

.main {
    background-color:#0f0f0f;
}

.block-container {
    padding-top: 1rem;
}

/* HEADER PREMIUM */
.hero {
    background: linear-gradient(135deg, #000000, #2b1b0f);
    border: 1px solid #c9a227;
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    color: #f5f0e6;
}

.hero h1 {
    font-size: 44px;
    letter-spacing: 3px;
    margin: 0;
}

.hero p {
    color: #d6c7a1;
    margin: 4px;
}

/* CARDS */
.card {
    background: #161616;
    border: 1px solid #2a2a2a;
    border-radius: 14px;
    overflow: hidden;
}

/* PRECIO */
.price {
    color: #c9a227;
    font-size: 20px;
    font-weight: bold;
}

/* BOTONES */
.stButton > button {
    background-color: #c9a227;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
}

/* WHATSAPP FLOTANTE */
.wsp {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #25D366;
    width: 65px;
    height: 65px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    text-decoration: none;
    z-index: 999;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">
    <h1>🥩 CARNES VIP</h1>
    <p>Premium Butchery</p>
    <p>📍 Peñalolén · Santiago</p>
    <p>🔥 Parrilla · 🚚 Delivery · 🥩 Cortes Premium</p>
</div>
""", unsafe_allow_html=True)

# =========================
# PRODUCTOS
# =========================

productos = [
    {
        "nombre": "Lomo Vetado",
        "precio": 12990,
        "img": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"
    },
    {
        "nombre": "Filete Premium",
        "precio": 15990,
        "img": "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=600&q=80"
    },
    {
        "nombre": "Costillar de Cerdo",
        "precio": 6990,
        "img": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?auto=format&fit=crop&w=600&q=80"
    },
    {
        "nombre": "Asado Carnicero",
        "precio": 8990,
        "img": "https://images.unsplash.com/photo-1603048297172-c92544798d5a?auto=format&fit=crop&w=600&q=80"
    },
]

# =========================
# SESSION
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = []

def add_item(p, qty):
    for i in st.session_state.cart:
        if i["nombre"] == p["nombre"]:
            i["cantidad"] += qty
            return
    st.session_state.cart.append({
        "nombre": p["nombre"],
        "precio": p["precio"],
        "cantidad": qty
    })

# =========================
# CATÁLOGO
# =========================

st.markdown("## 🥩 Catálogo Premium")

cols = st.columns(3)

for i, p in enumerate(productos):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="card">

            <img src="{p['img']}" width="100%">

            <div style="padding:12px">

                <h3 style="color:#f5f0e6">{p['nombre']}</h3>

                <div class="price">${p['precio']:,}/kg</div>

            </div>

        </div>
        """, unsafe_allow_html=True)

        qty = st.number_input(
            "Kg",
            min_value=1,
            max_value=20,
            value=1,
            key=f"q{i}"
        )

        if st.button("🛒 Agregar", key=f"b{i}"):
            add_item(p, qty)
            st.toast("Agregado al carrito")

# =========================
# SIDEBAR CARRITO
# =========================

st.sidebar.title("🛒 Pedido")

nombre = st.sidebar.text_input("Nombre")
telefono = st.sidebar.text_input("Teléfono")
direccion = st.sidebar.text_input("Dirección")
comuna = st.sidebar.text_input("Comuna")

total = 0

mensaje = f"""
🥩 CARNES VIP

Cliente: {nombre}
Tel: {telefono}
Dirección: {direccion}
Comuna: {comuna}

-----------------------
"""

if not st.session_state.cart:
    st.sidebar.info("Carrito vacío")

else:

    for item in st.session_state.cart:

        subtotal = item["precio"] * item["cantidad"]
        total += subtotal

        st.sidebar.write(
            f"{item['nombre']} x{item['cantidad']} = ${subtotal:,}"
        )

        mensaje += f"""
{item['nombre']} x{item['cantidad']} = ${subtotal:,}
"""

    mensaje += f"""

💰 TOTAL: ${total:,}
"""

st.sidebar.markdown(f"## TOTAL: ${total:,}")

# =========================
# WHATSAPP
# =========================

if st.session_state.cart:

    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(mensaje)}"

    st.sidebar.link_button(
        "📲 Enviar pedido por WhatsApp",
        url
    )

# =========================
# FLOTANTE
# =========================

st.markdown(f"""
<a class="wsp" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">💬</a>
""", unsafe_allow_html=True)

