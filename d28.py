import random

lista = [0, 1, 2, 3, 4, 5]
r = random.choice(lista)
n = int(input('Adivinhe o número que o computador escolheu de 0 a 5: '))
if n > 5 or n < 0:
    print('Seu número é maior que 5 ou menor que 0')
    exit()
if n == r:
    print('Você Venceu!')
else:
    print('Você perdeu :(')
print('O computador escolheu o número: ', r)

#ta certo mas ele fez assim

'''```python
from random import randint

computador = randint(0, 5)  # Faz o computador "PENSAR"
print('=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=' * 20)
jogador = int(input('Em que número eu pensei? '))  # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))'''''