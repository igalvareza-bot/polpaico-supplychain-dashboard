import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Carnes VIP",
    page_icon="🥩",
    layout="wide"
)

# ==========================================
# ESTILOS
# ==========================================

st.markdown("""
<style>

.main {
    background-color: #f7f7f7;
}

.hero {
    background: linear-gradient(135deg,#111,#8B0000);
    color:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
    margin-bottom:20px;
}

.product-card {
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.1);
    margin-bottom:15px;
}

.stButton > button {
    width:100%;
    background:#c62828;
    color:white;
    border:none;
    border-radius:10px;
}

.stButton > button:hover {
    background:#8B0000;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# DATOS
# ==========================================

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

# ==========================================
# SESSION
# ==========================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# ==========================================
# FUNCIONES
# ==========================================

def agregar_carrito(producto, cantidad):
    st.session_state.cart.append({
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })

# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero">
    <h1>🥩 Carnes VIP</h1>
    <h4>Premium Meat House</h4>
    <p>📍 Bolívar 6618, Peñalolén</p>
    <p>🚚 Delivery • 🔥 Parrilla • 🥩 Cortes Premium</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# OFERTAS
# ==========================================

st.info(
    "🔥 PROMOCIÓN: Delivery gratis sobre $50.000 | "
    "🥩 Cortes Premium seleccionados"
)

# ==========================================
# FILTROS
# ==========================================

col1, col2 = st.columns([1,1])

with col1:
    busqueda = st.text_input("🔎 Buscar producto")

with col2:
    categorias = ["Todos"] + list(set(
        [p["categoria"] for p in productos]
    ))

    categoria = st.selectbox(
        "Filtrar categoría",
        categorias
    )

# ==========================================
# CATÁLOGO
# ==========================================

st.subheader("🥩 Catálogo")

cols = st.columns(3)

indice = 0

for producto in productos:

    if categoria != "Todos":
        if producto["categoria"] != categoria:
            continue

    if busqueda:
        if busqueda.lower() not in producto["nombre"].lower():
            continue

    with cols[indice % 3]:

        with st.container(border=True):

            st.image(
                producto["img"],
                width=250
            )

            st.markdown(
                f"### {producto['nombre']}"
            )

            st.caption(producto["categoria"])

            st.metric(
                "Precio por Kg",
                f"${producto['precio']:,}"
            )

            cantidad = st.number_input(
                "Cantidad (Kg)",
                min_value=1,
                value=1,
                key=f"cantidad_{indice}"
            )

            if st.button(
                "🛒 Agregar",
                key=f"agregar_{indice}"
            ):
                agregar_carrito(producto, cantidad)
                st.success("Producto agregado")

    indice += 1

# ==========================================
# SIDEBAR CARRITO
# ==========================================

with st.sidebar:

    st.header("🛒 Carrito")

    total = 0

    if len(st.session_state.cart) == 0:

        st.info("No hay productos")

    else:

        mensaje = "🥩 PEDIDO CARNES VIP\n\n"

        for item in st.session_state.cart:

            subtotal = (
                item["precio"] *
                item["cantidad"]
            )

            total += subtotal

            st.write(
                f"**{item['nombre']}**"
            )

            st.write(
                f"{item['cantidad']} Kg"
            )

            st.write(
                f"${subtotal:,}"
            )

            st.divider()

            mensaje += (
                f"• {item['nombre']}\n"
                f"Cantidad: {item['cantidad']} Kg\n"
                f"Subtotal: ${subtotal:,}\n\n"
            )

        mensaje += f"💰 TOTAL: ${total:,}"

        st.markdown(
            f"## Total: ${total:,}"
        )

        whatsapp = (
            "https://wa.me/56971791270"
            f"?text={quote(mensaje)}"
        )

        st.link_button(
            "📲 Enviar pedido por WhatsApp",
            whatsapp
        )

        if st.button("🗑️ Vaciar carrito"):
            st.session_state.cart = []
            st.rerun()

# ==========================================
# BOTON FLOTANTE WHATSAPP
# ==========================================

st.markdown("""
<a href="https://wa.me/56971791270"
target="_blank"
style="
position:fixed;
bottom:20px;
right:20px;
background:#25D366;
color:white;
width:65px;
height:65px;
display:flex;
align-items:center;
justify-content:center;
border-radius:50%;
font-size:30px;
text-decoration:none;
z-index:9999;
box-shadow:0 4px 15px rgba(0,0,0,0.3);
">
💬
</a>
""", unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
### 📍 Carnes VIP

📌 Bolívar 6618, Peñalolén

📲 Pedidos por WhatsApp

🚚 Delivery rápido

🔥 Especialistas en parrilla
""")