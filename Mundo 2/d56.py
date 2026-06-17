somaidade = 0
qm2 = 0
maisvelho = 0
nomemaisvelho = ''
for c in range (0, 4):
    nome = str(input((f'Digite o nome da {c+1} pessoa : '))).strip()
    idade = int(input((f'Digite a idade da {c+1} pessoa : ')))
    sexo = str(input((f'Digite o sexo da {c+1} pessoa [F/M]: '))).strip().upper()
    print('=-' *20)

    #media
    somaidade += idade

    #mulheres com menos de 20
    if idade < 20 and sexo == 'F':
        qm2 += 1

    #mais velho
    if sexo == 'M':
        if idade > maisvelho:
            maisvelho = idade        # atualiza só quando achar alguém mais velho
            nomemaisvelho = nome

media = somaidade / 4
print(f'O nome do Homem mais velho é "{nomemaisvelho}", com {maisvelho} anos')
print(f'A média das idades é: {media:.1f}')
print(f'Existem {qm2} mulheres com com menos de 20 anos')

#depois de estudar as resolucoes dos exercicios anteriores da aula, consegui fazer
#apenas no #mais velho precisei de ajuda 