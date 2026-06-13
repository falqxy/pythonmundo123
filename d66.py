n = s = c = 0
while True:
    n = int(input('Digite um valor (999 PARA PARAR): '))  # looping infinito
    if n == 999:
        break  # funcao para sair do looping
    s += n
    c += 1
print(f'Você digitou {c} números, e a soma deles vale {s}')

#certo