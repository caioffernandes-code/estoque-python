from data import vendas
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

