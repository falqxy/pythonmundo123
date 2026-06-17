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
