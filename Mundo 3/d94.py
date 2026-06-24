pessoas = {}
mulheres = []
pessoasacima = []
plista = []
media = sidade = 0

while True:
    pessoas["nome"] = str(input("Nome: "))
    pessoas["idade"] = int(input("Idade: "))
    sidade += pessoas["idade"]
    pessoas["sexo"] = str(input("Sexo [F/M]: "))
    if pessoas["sexo"] in 'Ff':
        mulheres.append(pessoas["nome"])
    plista.append(pessoas.copy())

    while True:
        sn = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if sn[0] in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')     
    if sn == 'N':
        break

print("=-" *30)
print(plista)
print("=-" *30)

print(f"Tivemos {len(plista)} pessoas cadastradas")
media = sidade / len(plista)
print(f"A média de idade é {media}")
print(f"Lista das mulheres: {mulheres}")
for i in plista:
    if i["idade"] > media:
        pessoasacima.append(i["nome"])
print(f"Lista de pessoas com idade acima da média: {pessoasacima}")

#certo

'''galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''