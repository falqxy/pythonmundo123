import random

x = ''
n = 999  # numero jogado
c = 0  # contador
r = 0  # resultado do jogador + computador  # computador escolhe de um a 10
print('----------- JOGO DO PAR OU IMPAR -----------')

while True:
    comp = random.randint(1, 10)

    esc = str(input('Deseja ser par ou impar? ')).strip().lower()
    while esc != 'par' and esc != 'impar':
        print('Entrada inválida!')
        esc = str(input('Deseja ser par ou impar? ')).strip().lower()

    n = int(input('Agora digite um número de 1 a 10: '))
    while n < 1 or n > 10:
        print('Entrada inválida!')
        n = int(input('Digite um número de 1 a 10: '))

    r = comp + n  # soma dos 2 numeros
    if r % 2 == 0:
        x = 'Par'
    else:
        x = 'Impar'  # verifica se a soma é par ou impar

    print('=-' * 10)
    print(
        f'Você jogou {n} e a máquina {comp}, o resultado é {r} que é um número {x}')

    if esc == 'par' and r % 2 == 0:
        c += 1
        print(f'Partida vencida! Você agora tem {c} vitórias!')
        print('Vamos jogar novamente...')
    elif esc == 'impar' and r % 2 != 0:
        c += 1
        print(f'Partida vencida! Você agora tem {c} vitórias!')
        print('Vamos jogar novamente...')
    else:
        break
print(f'Partida perdida! Você conquistou {c} vitórias durante a jogatina!')

#fiz diferente mas foi certo 