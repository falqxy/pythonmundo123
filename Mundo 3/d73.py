brasileirao = (
    'Palmeiras',
    'Flamengo',
    'Fluminense',
    'Athletico-PR',
    'Bragantino',
    'Bahia',
    'Coritiba',
    'São Paulo',
    'Atlético-MG',
    'Corinthians',
    'Cruzeiro',
    'Botafogo',
    'Vitória',
    'Internacional',
    'Santos',
    'Grêmio',
    'Vasco da Gama',
    'Remo',
    'Mirassol',
    'Chapecoense'
)

print(f'Os 5 primeiros colocados são: {brasileirao[:5]}')
print('-=' * 20)
print(f'Os 4 últimos na zona de rebaixamento são? {brasileirao[16:20]}')
print('-=' * 20)
print(f'Lista dos times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 20)
# +1 pq comeca no 0
print(f'O time da Chapecoense está na {brasileirao.index('Chapecoense')+1} colocação')

#certo