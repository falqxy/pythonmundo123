dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro percorreu? '))
r = 60 * dias + 0.15 * km
print('O valor a se pago é R${:.2f}' .format(r))