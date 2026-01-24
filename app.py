import streamlit as st
import pandas as pd
import matplotlib as plt

def main():
    st.set_page_config(page_title="Dashboard de Vendas de uma Loja de Celulares", layout="wide")
    st.title("Estoque")
    estoque = pd.read_csv("estoque.csv")
    st.table(estoque)
  
if __name__ == "__main__":
    main()