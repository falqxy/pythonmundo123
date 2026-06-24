jogador = {}
lista = []

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantidade de partidas de {jogador["nome"]}: '))
    jogador['golspartida'] = [] #claude helps
    for c in range(jogador['partidas']):
        gols = int(input(f'Quantos gols na partida {c+1}: '))
        jogador['golspartida'].append(gols)
    lista.append(jogador.copy())
    print(jogador)
    print(lista)
    while True:
        sn = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if sn[0] in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')     
    if sn == 'N':
        break

print(lista)
print(jogador)
print('=-' * 30)
print(f'{'cod':<5}{'nome':<15}{'gols':<20}{'total':<10}')
print('-' * 45)
for k, v in enumerate(lista): 
    print(f'{k+1:<5}', end='')
    print(f'{v['nome']:<15}', end='')
    print(f'{str(v['golspartida']):<20}', end='') #claude ajudou, transforma a lista em str
    print(f'{sum(v['golspartida']):<10}')
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 PARA PARAR): '))
    if dados == 999:
        break
    elif 1 <= dados <= len(lista):
        jogadorescolhido = lista[dados - 1]
        print(f'-- LEVANTAMENTO DO JOGADOR: {jogadorescolhido['nome']}')
        for i, gols in enumerate(jogadorescolhido['golspartida']):
            print(f'    No jogo {i+1} fez {gols} gols')
    else:
        print('Jogador não existe!')

#certo