# 🚗 RW Garage — Catálogo Digital de Estética Automotiva

Catálogo online de produtos para estética automotiva da **RW Garage**, desenvolvido para facilitar a visualização dos produtos e direcionar clientes para compra via **Mercado Livre** e **Shopify**.

Este projeto também faz parte do meu **portfólio pessoal**, demonstrando habilidades em Python, Streamlit, organização de dados e construção de aplicações web.

---

## 🎯 Objetivo do Projeto

Criar um **catálogo digital moderno**, simples e responsivo que:

- Organize os produtos por categoria
- Apresente imagens, descrição e preços
- Disponibilize links diretos para compra
- Funcione como um site público da RW Garage
- Possa ser facilmente mantido e expandido

---

## 🧠 Solução Desenvolvida

A aplicação foi construída utilizando:

- **Python** para manipulação de dados
- **Pandas** para organização do catálogo
- **Streamlit** para criação da interface web
- **HTML + CSS** para estilização customizada
- Estrutura modular para facilitar manutenção e evolução

Os produtos são carregados a partir de um arquivo CSV, permitindo atualização rápida sem necessidade de alterar o código.

---

## 🖥️ Demonstração

🔗 **Aplicação online (em breve):**  
> *(Link será adicionado após o deploy)*

---

## 📂 Estrutura do Projeto

```text
rw-garage-catalog/
│
├── app/
│   └── app.py                # Aplicação Streamlit
│
├── assets/
│   └── produtos/             # Imagens dos produtos
│
├── data/
│   └── catalogo_rw_garage.csv # Base de dados do catálogo
│
├── notebooks/
│   └── 01_catalog_structure.ipynb # Exploração e estruturação dos dados
│
├── venv/                     # Ambiente virtual (ignorado no Git)
│
├── .gitignore
└── README.md
