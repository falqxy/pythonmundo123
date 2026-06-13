'''while True:
    n = float(input('Deseja ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'{n:.0f} x 1 = {n * 1:.0f}')
    print(f'{n:.0f} x 2 = {n * 2:.0f}')
    print(f'{n:.0f} x 3 = {n * 3:.0f}')
    print(f'{n:.0f} x 4 = {n * 4:.0f}')
    print(f'{n:.0f} x 5 = {n * 5:.0f}')
    print(f'{n:.0f} x 6 = {n * 6:.0f}')
    print(f'{n:.0f} x 7 = {n * 7:.0f}')
    print(f'{n:.0f} x 8 = {n * 8:.0f}')
    print(f'{n:.0f} x 9 = {n * 9:.0f}')
    print(f'{n:.0f} x 10 = {n * 10:.0f}')  # fiz merda e to com preg de arrumar'''

# ta certo, mas com o looping for é muito mais facil

c = 0
while True:

    n = int(input('Deseja ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:  # se for negativo
        break
    for c in range(1, 11):  # sempre um a mais
        print(f'{n} x {c} = {n * c}')
print('Programa encerrado!')

#fiz sozinho