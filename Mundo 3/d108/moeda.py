import funcoes

p = float(input('Digite o preço: R$ '))

print(f'A metade de {funcoes.moeda(p)} é {funcoes.moeda(funcoes.metade(p))}')
print(f'O dobro de {funcoes.moeda(p)} é {funcoes.moeda(funcoes.dobro(p))}')
print(f'Aumentando 10% de {funcoes.moeda(p)} temos, {funcoes.moeda(funcoes.aumentar(p))}')
print(f'Diminuindo 13% de {funcoes.moeda(p)} temos, {funcoes.moeda(funcoes.diminuir(p))}')

#certo