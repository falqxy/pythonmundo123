n = 0
n2 = None
n = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'

n2 = int(input('Digite um número entre 0 e 20: '))
while n2 < 0 or n2 > 20:
    print('Entrada invalida')
    n2 = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n[n2]}')

#certo