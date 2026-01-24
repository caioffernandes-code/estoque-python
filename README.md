DOCUMENTAÇÃO E COMANDOS USADOS NO PROJETO DE ANÁLISE DE DADOS DE VENDAS DE CELULARES (FICTÍCIO)

python3 -m pip install -r requirements.txt

Comando responsável por instalar a biblioteca de análise de dados no terminal VS code.
É preciso estar com um arquivo requirements.txt para documentas o nome das bibliotecas
que deseja instalar.



Comando responsável por abrir o dashboard do streamlit na página web
streamlit run app.py


Usado para abrir a aplicação da base de dados dos celulares
python3 -m scripts.celulares.py


Usado no terminal do VS code, para abrir o dashboard do streamlit com os comandos desejados
python3 -m streamlit run app.py


Comando utilizada para converter o dicionário contendo os celulares em DataFrame (tabelas)
df = pd.DataFrame(celulares)


Utilizado para criar gerar arquivos em CSV ou XLSX
df.to_csv("celulares.csv", index=False)


Ordenandos os preços dos menores preços até os maiores
tabela_celulares= tabela_celulares.sort_values(by='preco')


Gera um arquivo csv com os preços ordenados
tabela_celulares.to_csv("precos_ordenados.csv", index=False)


Gera a média dos preços dos celulares
media_precos = tabela_celulares[].mean()

Comando do streamlit para colocar os filtros desejados
st.sidebar.header

Comando do streamlit para colocar múltiplos filtros
sistema = st.sidebar.multiselect


Comando usado para filtrar o preco
preco_min, preco_max = st.sidebar.slider
"Faixa de preço",
min_value=int(col_preco.min()),
max_value=int(col_preco.max()),
value=(1000, int(col_preco.max()))