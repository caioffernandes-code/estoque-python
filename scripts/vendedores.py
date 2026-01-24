from data import vendas
def vendas_vendedor(vendedor = ""):
    contador_vendas = 0
    for i in vendas:
        cf = i['vendedor']
        if cf == vendedor:
            contador_vendas = contador_vendas + 1

    return contador_vendas

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
