matriz = [[0, 0, 0], #indice 0 matriz[0] linha 1
          [0, 0, 0], #indice 1 matriz[1] linha 2
          [0, 0, 0]] #indice 2 matriz[2] linha 3
par = somapar = tercolsom = maior = 0
tercol = []
for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            par.append(n)
            somapar += n
        if c == 2:
            tercol.append(n)
            tercolsom += n
maior = max(matriz[1]) #if l == 1: nao precisa desse if, troca o maior = max(matriz[l]) por maior = max(matriz[1]) ele pega o indice 1 segunda linha
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares {par} é {somapar}')
print(f'A soma dos números da terceira coluna {tercol} é {tercolsom}')
print(f'O maior número é da segunda coluna é {maior}')

#certo
#ele fez assim
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:'''