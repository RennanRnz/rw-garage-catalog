import streamlit as st
import pandas as pd
from pathlib import Path

# ========================
# CONFIGURAÇÕES GERAIS
# ========================
st.set_page_config(
    page_title="RW Garage | Catálogo Automotivo",
    page_icon="assets/icons/rw_garage_logo.png",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "produtos"
ICONS_DIR = ASSETS_DIR / "icons"

# ========================
# CSS CUSTOM
# ========================
st.markdown(
    """
    <style>
        .card {
            background-color: #111;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.35);
            margin-bottom: 20px;
        }
        .price {
            color: #25d366;
            font-size: 20px;
            font-weight: bold;
        }
        .btn {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin-right: 6px;
            color: white;
        }
        .btn-ml {
            background-color: #ffe600;
            color: black;
        }
        .btn-shop {
            background-color: #5c6ac4;
        }
        .header {
            padding: 30px;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            border-radius: 20px;
            margin-bottom: 40px;
        }
        .wpp-float {
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 9999;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ========================
# BOTÃO WHATSAPP FLUTUANTE
# ========================
st.markdown(
    """
    <div class="wpp-float">
        <a href="https://wa.me/554396607482" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="55">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ========================
# HEADER
# ========================
col_logo, col_title, col_links = st.columns([1, 6, 2])

with col_logo:
    st.image(str(ICONS_DIR / "rw_garage_logo.png"), width=90)

with col_title:
    st.markdown(
        """
        <div class="header">
            <h1>RW Garage</h1>
            <h3>Catálogo Automotivo</h3>
            <p>Produtos profissionais para estética automotiva</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_links:
    st.markdown(
        """
        <a href="https://www.instagram.com/rwgarage0/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="32">
        </a>
        """,
        unsafe_allow_html=True
    )

# ========================
# LOAD DATA
# ========================
df = pd.read_csv(DATA_DIR / "catalogo_rw_garage.csv")

# ========================
# FILTROS
# ========================
st.sidebar.header("🔍 Filtros")

busca = st.sidebar.text_input("Buscar produto")

categorias = ["Todas"] + sorted(df["categoria"].unique())
categoria = st.sidebar.selectbox("Categoria", categorias)

if busca:
    df = df[df["produto"].str.contains(busca, case=False)]

if categoria != "Todas":
    df = df[df["categoria"] == categoria]

# ========================
# CATÁLOGO
# ========================
for categoria in df["categoria"].unique():
    st.subheader(f"🧴 {categoria}")
    produtos = df[df["categoria"] == categoria]
    cols = st.columns(3)

    for i, (_, row) in enumerate(produtos.iterrows()):
        with cols[i % 3]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            img = IMAGES_DIR / row["imagem"]
            if img.exists():
                st.image(str(img), width=200)

            st.markdown(f"### {row['produto']}")
            st.markdown(row["descricao"])

            if row["preco"] > 0:
                st.markdown(
                    f"<div class='price'>💰 R$ {row['preco']:.2f}</div>",
                    unsafe_allow_html=True
                )

            if pd.notna(row["link_mercado_livre"]):
                st.markdown(
                    f"<a class='btn btn-ml' href='{row['link_mercado_livre']}' target='_blank'>Mercado Livre</a>",
                    unsafe_allow_html=True
                )

            if pd.notna(row["link_shopify"]):
                st.markdown(
                    f"<a class='btn btn-shop' href='{row['link_shopify']}' target='_blank'>Shopify</a>",
                    unsafe_allow_html=True
                )

            st.markdown("</div>", unsafe_allow_html=True)