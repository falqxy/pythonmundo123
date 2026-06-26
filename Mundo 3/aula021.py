
print('=-' *10, 'AULA DE HELP', '=-' *10)
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    ''' #isso e uma docstring, quando chama help(func) aparece isso
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM!')


help(contador)

print(10 * '=-', 'AULA DE VAR OPCIONAIS', '=-' * 10)

def soma(a=0, b=0, c=0): # isso sao variaveis opcionais
    s = a + b + c
    print(f'A soma dos números é {s}')

soma(3, 2, 5)

print(10 * '=-', 'AULA DE ESCOPO', '=-' * 10)

def teste():
    x  = 8 #escopo local
    global n
    n = 9
    print(f'Na função teste x vale {x}')
    print(f'Na função teste n vale {n}')

print('PROGRAMA PRINCIPAL')
n = 2 #escopo global
print(f'No programa principal n vale {n}')
teste()
print(f'No programa principal x vale ')

print(10 * '=-', 'AULA DE RETURN', '=-' * 10)

def soma2(a=0, b=0, c=0):
    s = a + b + c
    return s

resposta = soma2(3, 2, 5)
print(f'O calculo vale {resposta}')
print(soma2(3, 7, 1))