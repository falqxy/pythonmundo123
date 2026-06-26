def leiaInt():
    n = (input('Digite um número: '))
    while n.isnumeric() == False:
        print('ERRO: Digite um número inteiro')
        n = (input('Digite um número: '))
    print(f'Você digitou o número {n}')
leiaInt()

#certo

#resolucao do professor

'''def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''