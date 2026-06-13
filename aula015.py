n = s = 0
while True:
    n = int(input('Digite um valor: ')) #looping infinito
    if n == 999:
        break #funcao para sair do looping
    s += n 
print(f'A soma vale {s}')