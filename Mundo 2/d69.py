c = 0
ch = 0
cm = 0
while True:
    print('-------------- CADASTRO DE PESSOAL --------------')
    i = int(input('Qual sua idade? '))
    sex = str(input('Qual seu sexo [F/M]? ')).strip().upper()[0]#0 so le a primeira letra
    while sex != 'F' and sex != 'M': #podia ser while sex not in 'FM':
        print('Entrada inválida')
        sex = str(input('Qual seu sexo [F/M]? ')).strip().upper()[0]
    if i >= 18:
        c += 1
    if sex in 'M':
        ch += 1
    if i < 20 and sex in 'F':
        cm += 1
    p = str(input('Deseja continuar cadastrando [S/N]? '))
    while p != 'S' and p != 'N':
        print('Entrada inválida')
        p = str(input('Deseja continuar cadastrando [S/N]? '))
    if p in 'N':
        print('Programa encerrado!')
        break
print('-------------- ESTATÍSTICAS --------------')
print(f'Existem {c} pessoas maiores de 18 anos cadastradas!')
print(f'Existem {ch} homens cadastrados!')
print(f'Existem {cm} mulheres com menos de 20 anos cadastradas!')

#certo