import os

caminho = os.path.dirname(__file__)
arquivo = os.path.join(caminho, 'cadastro.txt')

def menu():
    while True:
        try:
            print('=' * 40)
            print(f'{"MENU PRINCIPAL":^40}')
            print('=' * 40)
            print('1 - Ver pessoas cadastradas')
            print('2 - Cadastrar nova Pessoa')
            print('3 - Sair do Sistema')
            print('-' * 40)
            opc = int(input('Sua Opção: '))
        except:
            print('ERRO: Digite um opção válida')
            opc = int(input('Sua Opção: '))
        if opc == 1:
            with open(arquivo, 'r') as f:
                print('=' * 40)
                print(f'{"PESSOAS CADASTRADAS":^40}')
                print('-' * 40)
                print(f.read())
        elif opc == 2:
            print('=' * 40)
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('-' * 40)
            nome = str(input('Nome: '))
            try:
                idade = int(input('Idade: '))
            except:
                print('ERRO: Por favor, digite um numero inteiro válido')
            finally:
                print(f'Novo registro {nome} de {idade} anos registrado com sucesso')
            with open(arquivo, 'a') as f:
                f.write(f'{nome:<25}{idade} anos\n')
        elif opc == 3:
            break
    print('Volte sempre :)')
