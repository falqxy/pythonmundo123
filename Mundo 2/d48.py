s = 0
print('DE 0 A 500, OS NÚMEROS ÍMPARES SAO:')
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(f'O número {c} é ímpar e múltiplo de 3')
        s += c
print(f'A soma de todos os números ímpares múltiplos de 3 {s} é:')
print('FIM!')

#claude ajudou com a formula c % 3 == 0
#certo

'''soma = 0
cont = 0
for c in range (1, 500, 2)
    if c % 3 == 0
        cont = cont + 1 #ou cont += 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma})'''