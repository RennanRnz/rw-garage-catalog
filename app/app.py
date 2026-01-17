import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="RW Garage | Catálogo Automotivo",
    page_icon="🚗",
    layout="wide"
)

# =========================
# CSS GLOBAL (CARDS)
# =========================
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
    margin-bottom: 25px;
}

.preco {
    font-size: 18px;
    font-weight: bold;
    color: #2e7d32;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.title("🚗 RW Garage — Catálogo de Produtos Automotivos")
st.markdown(
    "Produtos selecionados para **estética automotiva**, com links diretos para compra."
)

# =========================
# CARREGAMENTO DOS DADOS
# =========================
DATA_PATH = Path("data/catalogo_rw_garage.csv")
IMG_PATH = Path("assets/produtos")

df = pd.read_csv(DATA_PATH)

# Agrupando por categoria
catalogo_por_categoria = {
    categoria: dados.reset_index(drop=True)
    for categoria, dados in df.groupby("categoria")
}

# =========================
# RENDERIZAÇÃO DO CATÁLOGO
# =========================
for categoria, produtos_categoria in catalogo_por_categoria.items():

    st.subheader(f"🧽 {categoria}")

    for _, produto in produtos_categoria.iterrows():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])

        # -------- IMAGEM --------
        with col1:
            img_file = IMG_PATH / produto["imagem"]
            if img_file.exists():
                image = Image.open(img_file)
                st.image(image, width="stretch")
            else:
                st.info("Imagem não disponível")

        # -------- INFORMAÇÕES --------
        with col2:
            st.markdown(f"### {produto['produto']}")
            st.write(produto["descricao"])

            st.markdown(
                f'<div class="preco">💰 R$ {produto["preco"]:.2f}</div>',
                unsafe_allow_html=True
            )

            col_btn1, col_btn2 = st.columns(2)

            with col_btn1:
                if pd.notna(produto["link_mercado_livre"]):
                    st.link_button(
                        "🛒 Mercado Livre",
                        produto["link_mercado_livre"]
                    )

            with col_btn2:
                if pd.notna(produto["link_shopify"]):
                    st.link_button(
                        "🛍️ Shopify",
                        produto["link_shopify"]
                    )

        st.markdown("</div>", unsafe_allow_html=True)