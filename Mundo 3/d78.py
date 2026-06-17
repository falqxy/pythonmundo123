maior = 0
menor = None
lista = list()

for c in range(0, 5):
    valores = int(input('Digite um valor: '))
    lista.append(valores)
    if valores > maior:
        maior = valores
    elif menor is None or valores < menor:
        menor = valores

pos_menor = []
pos_maior = []
for pos, valor in enumerate(lista):
    if valor == maior:
        pos_maior.append(pos)
    if valor == menor:
        pos_menor.append(pos)

print(f'Você digitou a lista {lista}')
if len(pos_menor) > 1:
    print(f'O menor número foi {menor} nas posições {pos_menor}')
else:
    print(f'O menor número foi {menor} na posição {pos_menor}')
if len(pos_maior) > 1:
    print(f'O maior valor foi {maior} nas posições {pos_maior}')
else:
    print(f'O maior valor foi {maior} na posição {pos_maior}')

#certo

'''for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if valores[-1] > maior:
        maior = valores[-1]
    elif menor is None or valores[-1] < menor:
        menor = valores[-1]

for pos, val in enumerate(valores):
    if val == maior:
        pos_maior = pos
    if val == menor:
        pos_menor = pos  # claude

print(
    f'O maior é {maior} na posição {pos_maior} e o menor {menor} na posição {pos_menor}')'''
