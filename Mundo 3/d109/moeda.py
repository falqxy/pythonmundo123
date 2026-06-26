import funcoes

p = float(input('Digite o preço: R$ '))

print(f'A metade de {funcoes.moeda(p)} é {funcoes.metade(p, show=False)}')
print(f'O dobro de {funcoes.moeda(p)} é {funcoes.dobro(p, show=False)}')
print(f'Aumentando 10% de {funcoes.moeda(p)} temos, {funcoes.aumentar(p, show=True)}')
print(f'Diminuindo 13% de {funcoes.moeda(p)} temos, {funcoes.diminuir(p, show=True)}')

#certo