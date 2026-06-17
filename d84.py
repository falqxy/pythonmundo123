'''lista = []
contador = 0
peso = 0
maior = 0
menor = None
nome_maior = ''
nome_menor =  ''
while True:

    if peso > maior:
        maior = peso
        nome_maior = nome
    if menor is None or peso < menor:
        menor = peso
        nome_menor = nome
    sn = str(input('Deseja continuar [S/N]? '))
    print(lista)
    if sn[0] in 'Ss':
        continue
    if sn[0] in 'Nn':
        print('Programa finalizado!')
        break
    else:
        print('Entrada inválida, digite novamente')
        sn = str(input('Deseja continuar? '))
print(f'Você cadastrou {contador} pessoas')
print(f'O maior peso foi {maior}. Peso de {nome_maior}')
print(f'O menor peso foi {menor}. Peso de {nome_menor}')'''  # meio certo


lista = []
dado = []
contador = 0
maior = menor = None
while True:

    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    lista.append(dado.copy())
    dado.clear()
    contador += 1
    sn = str(input('Deseja continuar [S/N]? '))
    if sn[0] in 'Ss':
        continue
    if sn[0] in 'Nn':
        print('Programa finalizado!')
        break
    else:
        print('Entrada inválida, digite novamente')
        sn = str(input('Deseja continuar? '))

for p in lista:
    if maior is None or p[1] > maior:
        maior = p[1]
    if menor is None or p[1] < menor:
        menor = p[1]

print(f'Você cadastrou {contador} pessoas')
print(f'O maior peso foi {maior}. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

#certo