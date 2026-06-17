#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

nome = input('Qual é seu nome? ')
if nome == 'Bruno':
    print(f'Que nome bonito {nome}')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana, Claúdia, Jéssica, Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Bem vindo, {nome}')