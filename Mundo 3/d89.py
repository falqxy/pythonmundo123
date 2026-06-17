lista = [[], [], [], []]

while True:
    nome = str(input('Nome: '))
    lista[0].append(nome)
    n1 = float(input('Nota 1: '))
    lista[1].append(n1)
    n2 = float(input('Nota 2: '))
    lista[2].append(n2)
    media = (n1 + n2) / 2
    lista[3].append(media)
    sn = str(input('Deseja continuar [S/N]? '))
    if sn[0] in 'Ss':
        continue
    if sn[0] in 'Nn':
        print('Programa finalizado!')
        break
    else:
        print('Entrada inválida, digite novamente')
        sn = str(input('Deseja continuar? '))

print('=' * 35)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>10}')
print('-' * 35)
for c in range(len(lista[0])):
    # logica irada de usar o c, viciei
    print(f'{c:<4}{lista[0][c]:<12}{lista[3][c]:>10.1f}') 

while True:
    mn = int(input('Mostrar notas de qual aluno? (999 INTERROMPE): '))
    if mn == 999:
        print('Programa Finalizado!')
        break
    if mn < len(lista[0]):
        print(f'As notas de {lista[0][mn]} são {lista[1][mn]} e {lista[2][mn]}')
    else:
        print('Código de aluno inválido!')

#certo
#fica meio baguncado pq eu fiz uma lista so pra nomes, outra pra notas e outra pra medias
#ele fez uma lista pra cada aluno

'''ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')'''