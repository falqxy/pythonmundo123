'''import random
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(jogos):
    print(f'Jogo {c+1}: {random.sample(range(1, 61), k=6)}') #isso é um k'''

# fui la estudar a biblioteca e fiz sem lista


from random import randint
lista = []
cont2 = 0
jogos = int(input('Quantos jogos voce quer que eu sorteie: '))
while cont2 < jogos:
    cont2 += 1
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    print(lista)
    lista.clear() #eu fiz esse dps q vi o enunciado


'''from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)'''
