#estoque-python

## Instalação das Dependências
Para instalar as bibliotecas necessárias, execute no terminal:

- python3 -m pip install -r requirements.txt

## O arquivo requirements.txt documenta todas as dependências utilizadas no projeto.

## Execução do Projeto

### Para abrir o dashboard do Streamlit:
- python3 -m streamlit run app.py

### Para executar os scripts de geração de dados:
- python3 -m scripts.celulares

## Processamento e Análise de Dados

### Conversão dos dados para DataFrame:
- df = pd.DataFrame(celulares)

### Geração de arquivos CSV:
- df.to_csv("celulares.csv", index=False)

### Ordenação dos preços (do menor para o maior):
- tabela_celulares = tabela_celulares.sort_values(by="preco")

### Geração do CSV com preços ordenados:
- tabela_celulares.to_csv("precos_ordenados.csv", index=False)

### Cálculo da média dos preços:
- media_precos = tabela_celulares["preco"].mean()

## Filtros Interativos no Streamlit

### Cabeçalho da sidebar:
- st.sidebar.header("Filtros")

## Filtro por sistema operacional:
sistema = st.sidebar.multiselect("Sistema Operacional", options=tabela_celulares["sistema"].unique())

## Filtro por faixa de preço:
preco_min, preco_max = st.sidebar.slider("Faixa de preço", min_value=int(col_preco.min()), max_value=int(col_preco.max()), value=(1000, int(col_preco.max())))

