print('---------- BANCO DOS AMIGOS ----------')
v = int(input('Quanto você deseja sacar? R$ '))
tot50 = 0
tot20 = 0
tot10 = 0
tot1 = 0  # contar quantas cedulas
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
while True:
    if v >= ced50:
        v -= ced50
        tot50 += 1
    elif v >= ced20:
        v -= ced20
        tot20 += 1
    elif v >= ced10:
        v -= ced10
        tot10 += 1
    elif v >= ced1:
        v -= ced1
        tot1 += 1
    if v == 0:
        break
print(f'Total de {tot50} cedulas de {ced50}')
print(f'Total de {tot20} cedulas de {ced20}')
print(f'Total de {tot10} cedulas de {ced10}')
print(f'Total de {tot1} cedulas de {ced1}')


#vi a resolucao nao copiei e fiz com a minha logica deu isso mas foi certo
#o claude falou que é mais limpo toma
#agora o jeito dele

'''```python
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
```'''