from data.celulares import celulares
from data.vendas import vendas
import pandas as pd

df_vendas = pd.DataFrame(vendas)
df_celulares = pd.DataFrame(celulares)

df_celulares.to_csv("celulares.csv", index=False)
df_vendas.to_csv("vendas.csv", index=False)

def criar_estoque ():
    arquivo_celulares = pd.read_csv("celulares.csv")
    arquivo_vendas = pd.read_csv("vendas.csv")
    
    copia_celulares = arquivo_celulares
    for index, celular in copia_celulares.iterrows():        
        for index_1, venda in arquivo_vendas.iterrows():
            if celular["id"]== venda["produto_id"]:
                #print(celular)
                copia_celulares.drop(index, inplace=True)
                break
    copia_celulares.to_csv("estoque.csv", index=False)
    return copia_celulares



#resultado = criar_estoque()




    





