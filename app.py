import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carnes VIP", layout="wide")

# =========================
# ESTILO PREMIUM
# =========================
st.markdown("""
<style>

.main {
    background-color: #f4f4f4;
}

/* HEADER */
.hero {
    background: linear-gradient(90deg, #7f0000, #c62828);
    padding: 35px;
    border-radius: 18px;
    color: white;
}

/* PRODUCT CARD */
.card {
    background: white;
    border-radius: 16px;
    padding: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* BOTÓN */
.stButton>button {
    background-color: #c62828;
    color: white;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>🥩 Carnes VIP</h1>
    <p>Premium Meat House | Peñalolén - Bolívar 6618</p>
    <p>🥩 Cortes seleccionados | 🚚 Delivery | 🔥 Parrilla & hogar</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# CATALOGO REAL CON IMAGENES
# =========================
productos = [
    {
        "nombre": "Lomo Vetado",
        "precio": 12990,
        "categoria": "Vacuno",
        "img": "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"
    },
    {
        "nombre": "Filete Premium",
        "precio": 15990,
        "categoria": "Vacuno",
        "img": "https://images.unsplash.com/photo-1603360946369-dc9bb6258143"
    },
    {
        "nombre": "Asado Carnicero",
        "precio": 8990,
        "categoria": "Vacuno",
        "img": "https://images.unsplash.com/photo-1551028150-64b9f398f678"
    },
    {
        "nombre": "Costillar de Cerdo",
        "precio": 6990,
        "categoria": "Cerdo",
        "img": "https://images.unsplash.com/photo-1604908176997-125f25cc500f"
    },
    {
        "nombre": "Chorizos Artesanales",
        "precio": 5990,
        "categoria": "Embutidos",
        "img": "https://images.unsplash.com/photo-1607623814075-e51df1bdc82f"
    }
]

# =========================
# CARRITO
# =========================
if "cart" not in st.session_state:
    st.session_state.cart = []

# =========================
# FUNCION AGREGAR
# =========================
def add_to_cart(producto):
    st.session_state.cart.append(producto)

# =========================
# FILTRO
# =========================
categorias = ["Todos"] + list(set([p["categoria"] for p in productos]))
cat = st.selectbox("🔎 Filtrar catálogo", categorias)

# =========================
# GRID DE PRODUCTOS
# =========================
st.markdown("## 🥩 Catálogo Premium")

for p in productos:
    if cat != "Todos" and p["categoria"] != cat:
        continue

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(p["img"], use_container_width=True)

    with col2:
        st.markdown(f"### {p['nombre']}")
        st.write(f"Categoria: {p['categoria']}")
        st.markdown(f"## 💰 ${p['precio']:,} / kg")

        if st.button(f"Agregar {p['nombre']} 🛒"):
            add_to_cart(p)
            st.success("Agregado al carrito")

st.divider()

# =========================
# CARRITO REAL
# =========================
st.markdown("## 🛒 Carrito de compras")

if len(st.session_state.cart) == 0:
    st.info("Tu carrito está vacío")
else:
    total = 0

    for i, item in enumerate(st.session_state.cart):
        st.write(f"- {item['nombre']} | ${item['precio']:,}")
        total += item["precio"]

    st.markdown(f"### 💰 Total: ${total:,}")

    # =========================
    # WHATSAPP ORDER
    # =========================
    mensaje = "Pedido Carnes VIP:%0A"

    for item in st.session_state.cart:
        mensaje += f"- {item['nombre']} ${item['precio']}%0A"

    mensaje += f"%0ATotal: ${total}"

    whatsapp_url = f"https://wa.me/569XXXXXXXX?text={mensaje}"

    st.link_button("📲 Enviar pedido por WhatsApp", whatsapp_url)

    if st.button("🗑️ Vaciar carrito"):
        st.session_state.cart = []
        st.rerun()

# =========================
# CONTACTO
# =========================
st.divider()

st.markdown("""
### 📍 Carnes VIP
📌 Bolívar 6618, Peñalolén  
📲 WhatsApp pedidos directos  
🚚 Delivery rápido  
🔥 Especialistas en parrilla
""")