def metade(n):
    return n / 2
def dobro(n):
    return n * 2
def aumentar(n, aum):
    return n * (1 + aum/100)
def diminuir(n, red):
    return n * (1 - red/100)
def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')
def resumo(n, aum, red):
    print(f'A metade de {moeda(n)} é {moeda(metade(n))}')
    print(f'O dobro de {moeda(n)} é {moeda(dobro(n))}')
    print(f'Aumentando {aum}% de {moeda(n)} temos, {moeda(aumentar(n, aum))}')
    print(f'Diminuindo {red}% de {moeda(n)} temos, {moeda(diminuir(n, red))}')