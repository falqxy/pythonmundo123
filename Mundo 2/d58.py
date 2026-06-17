from random import randint
from time import sleep

'''lista = [0, 1, 2, 3, 4, 5]
r = random.choice(lista)
n = int(input('Adivinhe o número que o computador escolheu de 0 a 5: '))
if n > 5 or n < 0:
    print('Seu número é maior que 5 ou menor que 0')
    exit()
if n == r:
    print('Você Venceu!')
else:
    print('Você perdeu :(')
print('O computador escolheu o número: ', r)''' #refazer desafio 28

c = 1 #pra caso o usuario acerte de primeira nao coloco 0 mas sim 1
print(5 *'=-' + 'INICIANDO JOGO DA ADIVINHACAO' + 5 * '=-')
sleep(3)
print(20 * '=-')
print('O COMPUTADOR ESTÁ PENSANDO...')
print(20 * '=-')
sleep(2)
print('Computador: PENSEI EM UM NÚMERO, CONSEGUE ADIVINHAR?')
r = randint(0, 10)
#print (r)
n = int(input('Digite um número de 0 a 10: '))
while r != n:
    n = int(input(f'Você errou, digite outro número: '))
    c += 1
print(f'Você adivinhou! Em {c} palpites, o número era {r}, PARABÉNS!')

#certo