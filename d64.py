'''n = 0
c = 0
soma = 0''' #quando todo mundo receber o mesmo valor, faça isso
n = c = soma = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        c += 1
        soma += n
print(f'Voce digitou {c} números')
print(f'A soma dos números digitados é {soma}')

#certo