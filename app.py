import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Carnes VIP",
    page_icon="🥩",
    layout="wide"
)

WHATSAPP = "56981919691"

# =========================
# ESTILO REAL ECOMMERCE
# =========================

st.markdown("""
<style>

.main {
    background:#0b0b0b;
}

.block-container {
    padding-top: 1rem;
}

/* HEADER REAL NEGOCIO */
.hero {
    background: linear-gradient(135deg, #000000, #1a1a1a);
    border-bottom: 1px solid #c9a227;
    padding: 45px;
    text-align: center;
    color: #f5f0e6;
}

.hero h1 {
    font-size: 46px;
    letter-spacing: 4px;
    margin: 0;
}

.hero p {
    color:#c9a227;
    margin: 5px;
}

/* GRID PRODUCTOS */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

/* CARD REAL */
.card {
    background:#141414;
    border:1px solid #2a2a2a;
    border-radius:14px;
    overflow:hidden;
    transition:0.2s;
}

.card:hover {
    transform: scale(1.02);
}

/* IMAGEN PRO REAL (IMPORTANTE) */
.card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}

/* TEXTO */
.card-body {
    padding: 12px;
}

.title {
    color:#f5f0e6;
    font-size:18px;
    font-weight:600;
}

.price {
    color:#c9a227;
    font-size:20px;
    font-weight:700;
    margin-top:5px;
}

/* BOTONES */
.stButton > button {
    width:100%;
    background:#c9a227;
    color:black;
    font-weight:bold;
    border-radius:10px;
    border:none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">
    <h1>🥩 CARNES VIP</h1>
    <p>Premium Butchery • Cortes Seleccionados</p>
    <p>📍 Peñalolén • Santiago</p>
    <p>🔥 Parrilla · 🚚 Delivery · 🥩 Calidad Premium</p>
</div>
""", unsafe_allow_html=True)

# =========================
# PRODUCTOS (IMAGENES FIXED REAL LOOK)
# =========================

productos = [
    {
        "nombre": "Lomo Vetado",
        "precio": 12990,
        "img": "https://images.unsplash.com/photo-1604908176997-125f25cc500f?auto=format&fit=crop&w=900&q=80"
    },
    {
        "nombre": "Asado Carnicero",
        "precio": 8990,
        "img": "https://images.unsplash.com/photo-1603048297172-c92544798d5a?auto=format&fit=crop&w=900&q=80"
    },
    {
        "nombre": "Filete Premium",
        "precio": 15990,
        "img": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143?auto=format&fit=crop&w=900&q=80"
    },
    {
        "nombre": "Costillar de Cerdo",
        "precio": 6990,
        "img": "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?auto=format&fit=crop&w=900&q=80"
    },
]

# =========================
# CART
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = []

def add(p, qty):
    for i in st.session_state.cart:
        if i["nombre"] == p["nombre"]:
            i["qty"] += qty
            return
    st.session_state.cart.append({
        "nombre": p["nombre"],
        "precio": p["precio"],
        "qty": qty
    })

# =========================
# TITLE
# =========================

st.markdown("## 🥩 Productos")

# =========================
# GRID REAL (STREAMLIT SAFE)
# =========================

cols = st.columns(3)

for i, p in enumerate(productos):

    with cols[i % 3]:

        st.markdown(f"""
        <div class="card">

            <img src="{p['img']}">

            <div class="card-body">

                <div class="title">{p['nombre']}</div>

                <div class="price">${p['precio']:,}/kg</div>

            </div>

        </div>
        """, unsafe_allow_html=True)

        qty = st.number_input(
            "Kg",
            1, 20, 1,
            key=f"q{i}"
        )

        if st.button("Agregar", key=f"b{i}"):
            add(p, qty)
            st.toast("Agregado")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("🛒 Pedido VIP")

nombre = st.sidebar.text_input("Nombre")
telefono = st.sidebar.text_input("Teléfono")
direccion = st.sidebar.text_input("Dirección")

total = 0
msg = "🥩 CARNES VIP\n\n"

for item in st.session_state.cart:

    sub = item["precio"] * item["qty"]
    total += sub

    st.sidebar.write(f"{item['nombre']} x{item['qty']} = ${sub:,}")

    msg += f"{item['nombre']} x{item['qty']} = ${sub}\n"

msg += f"\nTOTAL: ${total}"

st.sidebar.markdown(f"## TOTAL: ${total:,}")

if st.session_state.cart:

    url = f"https://wa.me/{WHATSAPP}?text={quote(msg)}"

    st.sidebar.link_button(
        "📲 Enviar pedido",
        url
    )
