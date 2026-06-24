'''def escreva(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))  

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')'''

#nao pensei em criar a variavel tam pra centralizar, a minha nao centralizava
# meio certo
#resolucao

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)  

escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')