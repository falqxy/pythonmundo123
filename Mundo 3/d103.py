def ficha(nome= None, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    else:
        gols = int(gols) #claude ajudou a transformar em int
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
ficha(nome, gols)

#certo