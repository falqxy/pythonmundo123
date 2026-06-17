frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso da frase {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um palíndromo!')
else:
    print(f'A frase nao é um palíndromo')

#o lobo ama o bolo
#tentei nem terminar
