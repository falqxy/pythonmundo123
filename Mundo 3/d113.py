def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
            return n
        except KeyboardInterrupt:
            print('O usário preferiu não informar os dados!')
        except:
            print('ERRO: Digite um número inteiro válido')
def leiaReal():
    while True:
        try:
            n = float(input('Digite um número real: '))
            return n
        except KeyboardInterrupt:
            print('O usário preferiu não informar os dados!')
        except:
            print('ERRO: Digite um número real válido')
ni = leiaInt()
nr = leiaReal()
print(f'Você digitou o número inteiro {ni} e o número real {nr}')

#certo