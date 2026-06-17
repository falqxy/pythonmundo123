matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
par = []

for l in range(3):
    for c in range(3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            par.append(n)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(par)
