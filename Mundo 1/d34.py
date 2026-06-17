sal = float(input('Qual é o seu salário? R$ '))
if sal > 1250:
    print('Com um aumento de 10%, agora seu salario é R${:.2f}' .format(sal * 1.10))
else:
    print('Com um aumento de 15%, agora seu salário é R${:.2f}' .format(sal * 1.15))

#ficou certinho, ele fez desse jeito
'''```python
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
```'''