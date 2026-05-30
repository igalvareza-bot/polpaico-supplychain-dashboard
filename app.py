```python
import streamlit as st
from urllib.parse import quote

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Carnes VIP",
    page_icon="🥩",
    layout="wide"
)

WHATSAPP_NUMBER = "56971791270"

# =====================================================
# CSS PREMIUM
# =====================================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.main{
    background:#f5f5f5;
}

.hero{
    background:linear-gradient(135deg,#111111,#7f0000);
    color:white;
    padding:35px;
    border-radius:20px;
    text-align:center;
    margin-bottom:20px;
}

.card{
    background:white;
    border-radius:18px;
    overflow:hidden;
    box-shadow:0px 4px 14px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.card-title{
    font-size:22px;
    font-weight:700;
    margin-bottom:5px;
}

.card-category{
    color:gray;
    font-size:14px;
}

.card-price{
    color:#c62828;
    font-size:28px;
    font-weight:bold;
}

.whatsapp-float{
    position:fixed;
    width:70px;
    height:70px;
    bottom:20px;
    right:20px;
    background:#25D366;
    color:white;
    border-radius:50%;
    text-align:center;
    font-size:35px;
    line-height:70px;
    text-decoration:none;
    z-index:9999;
    box-shadow:0 5px 15px rgba(0,0,0,.3);
}

.stButton > button{
    width:100%;
    border-radius:10px;
    background:#c62828;
    color:white;
    border:none;
}

.stButton > button:hover{
    background:#8b0000;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# PRODUCTOS
# =====================================================

productos = [

    {
        "nombre":"Lomo Vetado",
        "precio":12990,
        "categoria":"Vacuno",
        "img":"https://images.unsplash.com/photo-1544025162-d76694265947"
    },

    {
        "nombre":"Filete Premium",
        "precio":15990,
        "categoria":"Vacuno",
        "img":"https://images.unsplash.com/photo-1558030006-450675393462"
    },

    {
        "nombre":"Asado Carnicero",
        "precio":8990,
        "categoria":"Vacuno",
        "img":"https://images.unsplash.com/photo-1603048297172-c92544798d5a"
    },

    {
        "nombre":"Costillar de Cerdo",
        "precio":6990,
        "categoria":"Cerdo",
        "img":"https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba"
    },

    {
        "nombre":"Chorizos Artesanales",
        "precio":5990,
        "categoria":"Embutidos",
        "img":"https://images.unsplash.com/photo-1594041680534-e8c8cdebd659"
    }

]

# =====================================================
# SESSION
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# =====================================================
# FUNCIONES
# =====================================================

def agregar_producto(producto, cantidad):

    existe = False

    for item in st.session_state.cart:

        if item["nombre"] == producto["nombre"]:

            item["cantidad"] += cantidad
            existe = True
            break

    if not existe:

        st.session_state.cart.append({
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad
        })

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">

<h1>🥩 CARNES VIP</h1>

<h3>Premium Meat House</h3>

<p>
📍 Bolívar 6618 · Peñalolén
</p>

<p>
🚚 Delivery • 🔥 Parrilla • 🥩 Cortes Premium
</p>

</div>
""", unsafe_allow_html=True)

st.success(
    "🔥 DELIVERY GRATIS SOBRE $50.000 | "
    "🥩 CORTES PREMIUM SELECCIONADOS"
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🛒 Pedido")

    cliente = st.text_input(
        "Nombre Cliente"
    )

    telefono = st.text_input(
        "Teléfono"
    )

    direccion = st.text_input(
        "Dirección"
    )

    comuna = st.text_input(
        "Comuna"
    )

# =====================================================
# FILTROS
# =====================================================

c1, c2 = st.columns([2,1])

with c1:

    busqueda = st.text_input(
        "🔎 Buscar producto"
    )

with c2:

    categorias = ["Todos"] + sorted(
        list(
            set(
                p["categoria"]
                for p in productos
            )
        )
    )

    categoria = st.selectbox(
        "Categoría",
        categorias
    )

# =====================================================
# CATALOGO
# =====================================================

st.markdown("## 🥩 Catálogo Premium")

filtrados = []

for p in productos:

    if categoria != "Todos":

        if p["categoria"] != categoria:
            continue

    if busqueda:

        if busqueda.lower() not in p["nombre"].lower():
            continue

    filtrados.append(p)

cols = st.columns(3)

for i, p in enumerate(filtrados):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="card">

                <img src="{p['img']}"
                style="
                width:100%;
                height:220px;
                object-fit:cover;
                ">

                <div style="padding:15px">

                    <div class="card-title">
                    {p['nombre']}
                    </div>

                    <div class="card-category">
                    {p['categoria']}
                    </div>

                    <div class="card-price">
                    ${p['precio']:,}/kg
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        cantidad = st.number_input(
            "Cantidad (kg)",
            min_value=1,
            value=1,
            key=f"cant_{i}"
        )

        if st.button(
            "🛒 Agregar al pedido",
            key=f"btn_{i}"
        ):

            agregar_producto(
                p,
                cantidad
            )

            st.success(
                f"{p['nombre']} agregado"
            )

# =====================================================
# CARRITO
# =====================================================

with st.sidebar:

    st.divider()

    st.subheader("Detalle")

    total = 0

    if len(st.session_state.cart) == 0:

        st.info(
            "No hay productos"
        )

    else:

        mensaje = f"""
🥩 PEDIDO CARNES VIP

Cliente: {cliente}
Teléfono: {telefono}
Dirección: {direccion}
Comuna: {comuna}

=========================
"""

        for idx, item in enumerate(
            st.session_state.cart
        ):

            subtotal = (
                item["precio"]
                * item["cantidad"]
            )

            total += subtotal

            c1, c2 = st.columns([4,1])

            with c1:

                st.write(
                    f"**{item['nombre']}**"
                )

                st.caption(
                    f"{item['cantidad']} kg"
                )

            with c2:

                if st.button(
                    "❌",
                    key=f"del_{idx}"
                ):
                    st.session_state.cart.pop(idx)
                    st.rerun()

            st.write(
                f"${subtotal:,}"
            )

            st.divider()

            mensaje += f"""
• {item['nombre']}
Cantidad: {item['cantidad']} kg
Subtotal: ${subtotal:,}

"""

        mensaje += f"""

💰 TOTAL: ${total:,}
"""

        st.success(
            f"TOTAL: ${total:,}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(mensaje)}"
        )

        st.link_button(
            "📲 Enviar Pedido",
            whatsapp_url
        )

        if st.button(
            "🗑️ Vaciar Carrito"
        ):

            st.session_state.cart = []
            st.rerun()

# =====================================================
# BOTON FLOTANTE
# =====================================================

st.markdown(
    f"""
<a
href="https://wa.me/{WHATSAPP_NUMBER}"
target="_blank"
class="whatsapp-float">
💬
</a>
""",
    unsafe_allow_html=True
)

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
### 📍 Carnes VIP

📌 Bolívar 6618, Peñalolén

📲 WhatsApp Directo

🚚 Delivery Rápido

🔥 Especialistas en Parrilla
""")
```
