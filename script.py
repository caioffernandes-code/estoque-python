from data import vendas
import pandas as pd

def soma_vendas():
    soma = 0
    for i in vendas:
        v = i['valor_unitario']
        soma = soma + v
    return soma


def soma_pagamento(forma_pagamento):
    soma_p = 0
    for i in vendas:
        p = i['forma_pagamento']
        if p == forma_pagamento:
            soma_p = soma_p + i['valor_unitario']
    return soma_p


def soma_canal_venda(escolha):
    soma_ecommerce = 0
    for i in vendas:
        c = i['canal_venda']
        if c == escolha:
            soma_ecommerce = soma_ecommerce + i['valor_unitario']
    
    return soma_ecommerce

def soma_qtd_canal_venda (canal):
    soma_canal = 0
    for i in vendas:
        ca = i['canal_venda']
        if ca == canal:
            soma_canal = soma_canal + i['valor_unitario']

    return soma_canal


def vendas_vendedor(vendedor = ""):
    contador_vendas = 0
    for i in vendas:
        cf = i['vendedor']
        if cf == vendedor:
            contador_vendas = contador_vendas + 1

    return contador_vendas

def produto_mais_vendido():
    maior_produto = 0
    for i in vendas:
        produto_vendido = i['quantidade']
        if produto_vendido > maior_produto:
            maior_produto = produto_vendido
        
    return maior_produto

def produto_menos_vendido():
    menor_produto = vendas[0]['quantidade']
    for i in vendas:
        produto_menos = i['quantidade']
        if produto_menos < menor_produto:
            menor_produto = produto_menos

    return menor_produto

def vendedor_mais_vendeu():
    total_por_vendedor = {}

    for i in vendas:
        vendedor = i['vendedor']
        quantidade = i['quantidade']

        if vendedor in total_por_vendedor:
            total_por_vendedor[vendedor] += quantidade
        else:
            total_por_vendedor[vendedor] = quantidade

    maior_vendedor = None
    maior_quantidade = 0

    for vendedor, total in total_por_vendedor.items():
        if total > maior_quantidade:
            maior_quantidade = total
            maior_vendedor = vendedor

    return maior_vendedor, maior_quantidade

def vendedor_menos_vendeu():
    total_vendedor = {}
    for i in vendas:
        vendedor = i['vendedor']
        quantidade = i['quantidade']

        if vendedor in total_vendedor:
            total_vendedor[vendedor] += quantidade
        else:
            total_vendedor[vendedor] = quantidade

    menor_vendedor = None
    menor_quantidade = float('inf')

    for vendedor, total in total_vendedor.items():
        if total < menor_quantidade:
            menor_quantidade = total
            menor_vendedor = vendedor

    return menor_vendedor, menor_quantidade

def produto_mais_barato():
    menor_valor = float('inf')

    for i in vendas:
        valor = i['valor_unitario']
        if valor < menor_valor:
            menor_valor = valor

    return menor_valor

def produto_mais_caro():
    maior_valor = 0

    for i in vendas:
        valor = i['valor_unitario']
        if valor > maior_valor:
            maior_valor = valor
    
    return maior_valor


print("\n----------- ANÁLISE DAS VENDAS DE CELULARES ---------\n")

resultado_vendedor = vendas_vendedor("Ana")
print(f"O vendedor escolhido teve um total de vendas de: {resultado_vendedor:.0f} vendas")

resultado = soma_vendas()
print(f"As somas de todas as vendas foi de: {resultado:.2f} reais")

resultado_soma = soma_pagamento("PIX")
print(f"O total de vendas com a forma de pagamento escolhida foi de: {resultado_soma:.2f} reais")

resultado_ecommerce = soma_canal_venda("Loja Física")
print(f"A soma das vendas do canal de venda escolhido foi de: {resultado_ecommerce:.2f} reais")

resultado_qtd = soma_qtd_canal_venda("E-commerce")
print(f"A quantidade de venda por canal de venda escolhido foi de: {resultado_qtd:.2f} reais")

resultado_maior_produto = produto_mais_vendido()
print(f"O produto mais vendido foi o produto id {resultado_maior_produto}")

resultado_menor_produto = produto_menos_vendido()
print(f"O produto menos vendido foi o produto id {resultado_menor_produto}")

resultado_mais_vendeu = vendedor_mais_vendeu()
print(f"O vendedor que mais vendeu foi: {resultado_mais_vendeu}")

resultado_menos_vendeu = vendedor_menos_vendeu()
print(f"O vendedor que menos vendeu foi: {resultado_menos_vendeu}")

resultado_produto_mais_barato = produto_mais_barato()
print(f"O produto mais barato em estoque é o produto que custou: R$ {resultado_produto_mais_barato}")

resultado_produto_mais_caro = produto_mais_caro()
print(f"O produto mais caro é o produto que custou: R$ {resultado_produto_mais_caro}")


# dataFrame da lista de celulares
df = pd.DataFrame(celulares)
print(df)

#Geração de arquivo csv dos celulares
df.to_csv("celulares.csv", index=False)

#dataFrame da lista de vendas
df = pd.DataFrame(vendas)
print(df)

#Geração de arquivo csv das vendas
df.to_csv("vendas.csv", index=False)

#dataFrame da lista de vendedores
df = pd.DataFrame(vendedores)
print(df)

#Geração de arquivo csv dos vendedores
df.to_csv("vendedores.csv", index=False)

#dataFrame da lista de parcelas
df = pd.DataFrame(parcelas)
print(df)

#Geração de arquivo csv das parcelas
df.to_csv("parcelas.csv", index=False)

#leitura dos dados para filtragem
tabela_celulares = pd.read_csv("celulares.csv")

col_preco = tabela_celulares['preco']

print(

    tabela_celulares[col_preco > 1000]
)
#armazena
maior_que_1000 = tabela_celulares[col_preco > 1000]
#arquivo filtrado com os preços maiores que 1000
maior_que_1000.to_csv("preco_maior_que_1000.csv", index=False)

col_sistema = tabela_celulares['sistema']

###########Filtro para gerar planilha apenas com celulares Androids#########

print(

    tabela_celulares[col_sistema == 'Android']
)

apenas_Android = tabela_celulares[col_sistema == 'Android']
apenas_Android.to_csv("apenas_Android.csv", index=False)

###########Filtro para gerar planilha apenas com celulares iOS#########

col_sistema_ios = tabela_celulares['sistema']

print(

    tabela_celulares[col_sistema == 'iOS']
)

apenas_iOs = tabela_celulares[col_sistema == 'iOS']
apenas_iOs.to_csv("apenas_iOs.csv", index=False)

#####################################################################

#Ordenandos os preços dos menores preços até os maiores
tabela_celulares= tabela_celulares.sort_values(by='preco')

# Mostra a tabela ordenada
print("\nLista dos menores e maiores preços dos celulares:")
print(tabela_celulares)

tabela_celulares.to_csv("precos_ordenados.csv", index=False)

#Média dos preços dos celulares
media_precos = tabela_celulares['preco'].mean()
print(f"\nMédia dos Preços dos Celulares: {media_precos:.2f}")


media_precos = pd.DataFrame(

    {
        "media_preço" : [media_precos]
    }
)
media_precos.to_csv("media_preços.csv", index=False)


#leitura dos dados para filtragem
tabela_vendas = pd.read_csv("vendas.csv")

###########Filtro para gerar planilha apenas com venda de celulares na Loja Física#########

col_canal_de_Venda_lojafisica = tabela_vendas['canal_venda']

print(

    tabela_vendas[col_canal_de_Venda_lojafisica == 'Loja Física']
)
vendas_loja_fisica = tabela_vendas[col_canal_de_Venda_lojafisica == 'Loja Física']
vendas_loja_fisica.to_csv("vendas_loja_fisica.csv")

###########Filtro para gerar planilha apenas com venda de celulares no E-Commerce#########

col_canal_de_Venda_ecommerce = tabela_vendas['canal_venda']

print (
    tabela_vendas[col_canal_de_Venda_ecommerce == 'E-commerce']
)
vendas_ecommerce = tabela_vendas[col_canal_de_Venda_ecommerce == 'E-commerce']
vendas_ecommerce.to_csv("vendas_ecommerce.csv",index=False)

###########Filtro para gerar planilha apenas com venda de celulares no Cartão#########

col_forma_De_pagamento_cartao = tabela_vendas['forma_pagamento']

print (
    tabela_vendas[col_forma_De_pagamento_cartao == 'Cartão de Crédito']
)
vendas_cartao_de_Credito = tabela_vendas[col_forma_De_pagamento_cartao == 'Cartão de Crédito']
vendas_cartao_de_Credito.to_csv("vendas_Cartao.csv",index=False)

###########Filtro para gerar planilha apenas com venda de celulares no PIX##########

col_forma_De_pagamento_pix = tabela_vendas['forma_pagamento']

print(
    
    tabela_vendas[col_forma_De_pagamento_pix == 'PIX']
)
vendas_pix = tabela_vendas[col_forma_De_pagamento_pix == 'PIX']
vendas_pix.to_csv("vendas_pix.csv", index=False)

col_forma_De_pagamento_dinheiro = tabela_vendas['forma_pagamento']

###########Filtro para gerar planilha apenas com venda de celulares no Dinheiro#########

print (

    tabela_vendas[col_forma_De_pagamento_dinheiro == 'Dinheiro']
)
vendas_dinheiro = tabela_vendas[col_forma_De_pagamento_dinheiro == 'Dinheiro']
vendas_dinheiro.to_csv("vendas_dinheiro.csv", index=False)