import math

n = int(input('Digite um número: '))
r = math.factorial(n)
print(f"O fatorial de {n} é {r}")

#certo
#fiz importando biblioteca, com laco de repeticao nao sei fazer nao

#o dele

'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''