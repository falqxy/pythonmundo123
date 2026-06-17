c = 0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro um número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = n1, n2, n3, n4

'''podia fazer isso acima em tupla colocando tudo em ()'''

print(f'Você digitou os números: {tupla}')
if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3)+1} posição')
else:
    print('O número 3 não foi digitado')
print(f'O número 9 aparece {tupla.count(9)} vezes')  # claude ajudou
for n in tupla:
    if n % 2 == 0:
        c += 1  # claude ajudou sou muito ruim com for
print(f'{c} pares')

#certo