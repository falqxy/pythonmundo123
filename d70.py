s = 0
c = 0
savenome = ''
#savemenor = 0 NAO ADIANTA COLOCAR 0 PQ NAO TEM NADA MENOR QUE 0, COLOCA NOME
#ai nao coloca savemenor < p, mas sim if savemenor is None
savemenor = None

while True:

    print('----------------- LOJA DOS AMIGOS -----------------')
    nome = str(input('Nome do produto: ')).strip().lower()
    p = float(input('Preço: R$'))
    con = str(input('Deseja continuar [S/N]? ')).strip().upper()
    s += p  # soma dos precos
    if p > 1000:  # se for maior que 1000 reais
        c += 1
    if savemenor is None or p < savemenor:
        savemenor = p
        savenome = nome
    while con != 'S' and con != 'N':
        print('Entrada inválida')
        con = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if con in 'N':
        print('------------- Programa encerrado! -------------')
        break

print(f'O total da sua compra foi R${s:.2f}')
print(f'Temos {c} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {savenome} custando R${savemenor:.2f}')

#certo