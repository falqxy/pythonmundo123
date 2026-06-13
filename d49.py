'''n = float(input('Escreva um número: '))

print('========== TABUADA DO NÚMERO {} ==========' .format(n))
print(n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10)''' #esse eu que fiz no desafio 9

n = float(input('Escreva um número: '))

print('========== TABUADA DO NÚMERO {} ==========' .format(n))
for c in range (1, 11):
    print(f'{n} * {c} = {n*c}')

#certo
