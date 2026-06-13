lista = []

while True:
    n = (int(input('Digite um valor: ')))
    contagem = lista.count(n)
    if contagem >= 1:
        print('Valor ja existe na lista, portanto, nao foi adicionado!')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    opc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while opc[0] not in 'SsNn':
        print('Entrada inválida!')
        opc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if opc[0] in 'Ssim':
        continue
    elif opc[0] in 'Nnao':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A ordem decrescente é {lista}')
if 5 in lista:
    print('Existe o número 5 na lista!')
else:
    print('Não existe o número 5 na lista!')
