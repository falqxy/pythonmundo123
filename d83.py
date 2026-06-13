'''contador = 0
exp = input('Digite uma expressão: ')
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
    print('A expressão é aberta e está errada!')'''

lista = []
contador = 0

exp = input('Digite uma expressão: ')
for c in exp:
    if c == '(':
        lista.append(c)
    elif c == ')':
        lista.append(c)

for c in lista:
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