import random

par = []
sorteados = random.sample(range(1, 10), k=6)

def sorteio():
    print('Valores sorteados:', sorteados)
def somapar():
    s = 0
    for n in sorteados:
        if n % 2 == 0:
            par.append(n)
            s += n

    print(f'Somandos os valores pares {par} da lista, temos a soma {s}!')
sorteio()
somapar()

#fruto de estudar a biblioteca, eu consegui fazer sem me esforcar muito
#vendo a resolucao vi que o enunciado pedia lista dos numeros e confundi com o dos pares kk
#mesmo assim deu certihno

#solucao do professor

'''from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)'''