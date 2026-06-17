import random
jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(jogos):
    print(f'Jogo {c+1}: {random.sample(range(1, 60), k=6)}')

#fui la estudar a biblioteca e fiz sem lista