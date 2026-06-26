def fatorial(n=1, show=None):
    '''
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1 
    for c in range (n, 0, -1):
        f *= c
    if show == False:
        return f
    if show == True:
        for c in range (n, 0, -1):
            if c == 1:
                print(c, end='')
            else:
                print(f'{c} x ', end='')
        print(' = ', end='') 
        return f

print(fatorial(5, show=True))
help(fatorial)

#certo
#dava pra fazer com import math tambem inves de for