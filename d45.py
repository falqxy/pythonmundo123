import random

#pedra = 1, papel = 2, tesoura = 3
lista = [1, 2, 3]
r = random.choice(lista)
jogador = input('Qual você vai jogar? Pedra, Papel ou Tesoura? ').strip().lower()

if jogador == 'pedra' and r == 1:
    print('Escolhi PEDRA, Empate!')
elif jogador == 'pedra' and r == 2:
    print('Escolhi PAPEL! Você Perdeu!')
elif jogador == 'pedra' and r == 3:
    print('Escolhi TESOURA! Você Perdeu!')


elif jogador == 'papel' and r == 1:
    print('Escolhi PEDRA! Você Ganhou!')
elif jogador == 'papel' and r == 2:
    print('Escolhi PAPEL, Empate!')
elif jogador == 'papel' and r == 3:
    print('Escolhi TESOURA! Você Perdeu!')


elif jogador == 'tesoura' and r == 1:
    print('Escolhi PEDRA! Você Perdeu!')
elif jogador == 'tesoura' and r == 2:
    print('Escolhi PAPEL! Você Ganhou!')
elif jogador == 'tesoura' and r == 3:
    print('Escolhi TESOURA! Empate!')
else:
    print('Opção inválida! Digite Pedra, Papel ou Tesoura!')

#certo

#ele fez assim

'''from random import randint
from time import sleep
itens = ('Pedra', Papel, 'Tesoura')
computador = randint(0, 2)
print('O Computador escolheu {}' .format(itens[computador])) #isso aq e tipo o computador escolhe em itens posicao 0 é pedra e assim vai
print([ 0 ] PEDRA\n [ 1 ] PAPEL\n [ 2 ] TESOURA)
jogador = int(input('Qual a sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-' * 11)
print('Computador jogou {}' .format(itens[computador])
print('Jogador jogou {}' .format(itens[computador])
print('=-' * 11)


if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')'''