while True:

    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))

    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opc = int(input('Digite uma das opções: '))

    if opc == 1:
        print(f'A soma de {n1} + {n2} é:', n1 + n2)
    elif opc == 2:
        print(f'A multiplicação de {n1} * {n2} é:', n1 * n2)
    elif opc == 3:
        if n1 > n2:
            print(f'O valor {n1} é maior que {n2}')
        elif n2 > n1:
            print(f'O valor {n2} é maior que {n1}')
        else:
            print('Os dois valores são iguais!')
    elif opc == 4:
        continue
    elif opc == 5:
        print('Você escolheu sair do programa!')
        quit()
    else:
        print('Nenhuma das opções foi válida!')

#certo