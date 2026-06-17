exp = input('Digite uma expressão: ')
contador = 0
for c in exp:
    if c == '(':
        contador += 1
    elif c == ')':
        contador -= 1
    if contador < 0:
        break
if contador == 0:
    print('A expressão é fechada e está certa!')
else:
    print('A expressão é aberta e está errada!')

#certo
#eu nao sei como mas funcionou