listagem = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 20)
print('LISTAGEM DE PREÇOS')
print('-' * 20)
for c in range(0, len(listagem), 2): #range funciona COMECO, FINAL, PULO, 0, LEN(LISTAGEM) E 2 É O PULO que pega so o nome dos produtos
    print(f'{listagem[c]}................R${listagem[c+1]:.2f}') #c+1 pega sempre a listagem com os precos

#claude ajudou legal
#certo