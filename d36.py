print(('=- ' * 10) + 'APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO' + (' =-' * 10))

valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos a casa será paga? '))

prestacao = valor / (anos * 12)
if prestacao > sal * 0.3: 
    print('Seu empréstimo foi negado por exceder 30% do seu salário')
else:
    print(f'Empréstimo aprovado! Você pagará R${prestacao:.2f} por mês durante {anos} anos ')

#ajuda do claude, faltou converter anos em meses e nao mostrei o valor da prestacao mensal no else
#certo

'''casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')'''