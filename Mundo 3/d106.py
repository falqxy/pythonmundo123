def IH():
    while True:
        print('\033[0;30;42m' + '~' * 30)
        print('  SISTEMA DE AJUDA PyHELP')
        print('~' * 30 + '\033[m')
        resp = input('\033[0;44mFunção ou biblioteca > \033[0;36m')
        print('\033[m', end='')
        if resp.upper() == 'FIM':
            break
        print('\033[0;30;44m' + '~' * 30)
        print(f"  Acessando o manual do comando '{resp.lower()}'")
        print('~' * 30 + '\033[m')
        help(resp)
    print('FIM DO PROGRAMA')

IH()

#o vscode aparentemente buga com esse programa e fica meio quebrado
#mas ta certo

#tinha feito assim

'''```python
def IH():
    resp = str(input('Função ou biblioteca > '))
    while resp != 'FIM':
        help(resp)
        resp = str(input('Função ou biblioteca > '))

IH()
```'''