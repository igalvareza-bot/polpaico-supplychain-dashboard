import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Carnes VIP",
    page_icon="🥩",
    layout="wide"
)

WHATSAPP = "56981919691"

# =========================
# DATA (MEJOR IMAGEN CONSISTENTE)
# =========================

productos = [
    ("Lomo Vetado", 12990, "https://images.unsplash.com/photo-1604908176997-125f25cc500f?auto=format&fit=crop&w=800&q=80"),
    ("Filete Premium", 15990, "https://images.unsplash.com/photo-1603360946369-dc9bb6258143?auto=format&fit=crop&w=800&q=80"),
    ("Asado Carnicero", 8990, "https://images.unsplash.com/photo-1603048297172-c92544798d5a?auto=format&fit=crop&w=800&q=80"),
    ("Costillar Cerdo", 6990, "https://images.unsplash.com/photo-1529692236671-f1f6cf9683ba?auto=format&fit=crop&w=800&q=80"),
]

# =========================
# CART
# =========================

if "cart" not in st.session_state:
    st.session_state.cart = []

def add(name, price, qty):
    for i in st.session_state.cart:
        if i["name"] == name:
            i["qty"] += qty
            return
    st.session_state.cart.append({
        "name": name,
        "price": price,
        "qty": qty
    })

# =========================
# HEADER REAL (SIN LOOK DEMO)
# =========================

st.title("🥩 Carnes VIP")
st.caption("Premium Butchery · Cortes seleccionados en Santiago")

st.divider()

# =========================
# GRID LIMPIO (SIN HTML)
# =========================

cols = st.columns(4)

for i, (name, price, img) in enumerate(productos):

    with cols[i % 4]:

        st.image(img, use_container_width=True)

        st.subheader(name)
        st.write(f"💰 ${price:,}/kg")

        qty = st.number_input(
            "Kg",
            1, 20, 1,
            key=f"q{i}"
        )

        if st.button("Agregar", key=f"b{i}"):
            add(name, price, qty)
            st.toast("Agregado")

# =========================
# SIDEBAR (PRO REAL)
# =========================

st.sidebar.title("🛒 Pedido")

name = st.sidebar.text_input("Nombre")
phone = st.sidebar.text_input("Teléfono")
address = st.sidebar.text_input("Dirección")

total = 0
msg = "🥩 CARNES VIP\n\n"

if st.session_state.cart:

    for item in st.session_state.cart:

        sub = item["price"] * item["qty"]
        total += sub

        st.sidebar.write(f"{item['name']} x{item['qty']} = ${sub:,}")

        msg += f"{item['name']} x{item['qty']} = ${sub}\n"

msg += f"\nTOTAL: ${total:,}"

st.sidebar.divider()
st.sidebar.markdown(f"## TOTAL: ${total:,}")

if st.session_state.cart:

    url = f"https://wa.me/{WHATSAPP}?text={quote(msg)}"

    st.sidebar.link_button("📲 Enviar pedido", url)