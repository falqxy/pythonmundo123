'''dado = []
lista = []
par = []
impar = []

for c in range(7):
    dado.append(int(input(f'Digite um {c+1} valor: ')))
    lista.append(dado.copy())
    dado.clear()
    if lista[c][0] % 2 == 0:  # logica pica ta
        par.append(lista[c][0])
    else:
        impar.append(lista[c][0])

print(lista)
print(f'Os pares sao {par}')
print(f'Os impares são {impar}')'''  # eu nao tinha visto o enunciado e fiz do meu jeito

lista = [[], []]
for c in range(7):
    n = int(input(f'Digite um {c+1} valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(lista)
lista[0].sort
lista[1].sort

print('Números em ordem crescente!')
print(f'Os números pares são {lista[0]}')
print(f'Os números ímpares são {lista[1]}')

#certo
