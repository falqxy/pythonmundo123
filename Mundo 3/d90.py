aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Média do aluno: '))

print(f'O nome do aluno é {aluno['nome']}')
print(f'A média do aluno é {aluno['media']}')
if aluno['media'] >= 7:
    print('A situação do aluno é Aprovado!')
elif aluno['media'] < 5:
    print('A situação do aluno é Reprovado!')
else:
    print('Aluno em recuperação')

#certo, ele quis elaborar mais

'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')'''
