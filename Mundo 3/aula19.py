# podemos usar dicionarios com tuplas, listas etc
# dicionarios sao mutaveis

pessoas = {'nome': 'Bruno', 'sexo': 'M', 'idade': 21}
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5 #sem precisar de append
# del pessoas['sexo'] #apaga a key sexo e os valores dentro dele

print('==' * 10)
print('Keys: sao os atributos')
print('==' * 10)
for k in pessoas.keys():
    print(k)
print('==' * 10)

print('Values: São os valores inseridos nos atributos que sao as chaves')
print('==' * 10)
for v in pessoas.values():
    print(v)
print('==' * 10)

print('Item: sao keys e values')
print('==' * 10)
for k, v in pessoas.items():  # items sao como enumerate em tuplas e listas
    print(f'{k}, {v}')
print('==' * 10)
