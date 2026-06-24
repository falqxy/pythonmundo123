from random import randint
from time import sleep

dado = {'jogador1': None, 'jogador2': None, 'jogador3': None, 'jogador4': None}

print('Valores sorteados:')
for c in range(4):
    dado[f'jogador{c+1}'] = randint(1, 6)
    print(f'O jogador {c+1} tirou: {dado[f"jogador{c+1}"]}')
    sleep(1)
print(dado)
print('Ranking dos Jogadores')
rank = dado.copy()
for c in range(4):
    maiorv = 0
    maiorj = None
    for jogador, valor in rank.items():
        if valor > maiorv:
            maiorv = valor
            maiorj = jogador
    print(f'{c+1}º lugar: {maiorj} com {maiorv}')
    del rank[maiorj]

#gambiarrudo mas foi

#ele nao ensinou como usar o sorted nas listas, eu pesquisei sobre essa possibilidade
#mas como nao foi ensinado, eu nao fiz

'''from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#jogo.items() retorna em tupla e key=itemgetter(1) pega o indice 1 da tupla, que e o numero sorteado
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}') #v[0] indice 0 nome e v[1] inidice 1 numero
    sleep(1)'''

