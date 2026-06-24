from datetime import date

dado = {}
dado['nome'] = str(input('Nome: '))
dado['ano'] = int(input('Ano de Nascimento: '))
idade = date.today().year - dado['ano']
dado['carteira'] = int(input('Carteira de Trabalho (0 = nao tem): '))
if dado['carteira'] != 0:
    dado['contratado'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: R$ '))
    trabalhado = date.today().year - dado['contratado']
    aposentar = 35 - trabalhado
print(dado)
print(f"Nome tem o valor: {dado['nome']}")
print(f"Idade tem o valor: {idade}")
print(f"CTPS tem o valor: {dado['carteira']}")
if dado['carteira'] != 0:
    print(f"Contratação tem o valor: {dado['contratado']}")
    print(f"Salário tem o valor: {dado['salario']}")
    print(f"Aposentadoria tem o valor {aposentar}")

#certo

'''from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')'''