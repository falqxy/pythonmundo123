v = float(input('Qual a velocidade do carro? '))
limite = 80
excesso = v - limite
multa = excesso * 7

if v > limite:
    print('Você está em alta velocidade e foi multado em: R${:.2f}' .format(multa))
else:
    print('Você está numa velocidade normal')

#ta certo ele fez assim

'''```python
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
```'''