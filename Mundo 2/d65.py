sn = ''
c = 0
media = 0
soma = 0
menor = None
maior = 0
while sn != 'N':
    n = int(input('Digite um valor: '))
    sn = str(input('Você deseja continuar adicionando números? [S/N] ')).upper().strip()

    soma += n
    c += 1
    if n > maior:
        maior = n
    if menor is None or n < menor: #claude ajudou com isso apenas
        menor = n

    if sn != 'S' and sn != 'N':
        print('[ERROR] Entrada Inválida!')
        sn = str(input('Você deseja continuar adicionando números? [S/N] ')).upper().strip()
    elif sn == 'N':
        media = soma / c
print(f'A média dos valores é {media}')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')

#certo