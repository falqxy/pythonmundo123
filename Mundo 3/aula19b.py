estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(estado1)  # printa o dic estado1
print(estado2)  # printa o dic estado2
print(brasil)  # printa o a lista brasil
print(brasil[0]) #printa o indice 0 do dic adicionado a lista, o RJ
print(brasil[0]['uf']) #pega o indice 0 e dentro desse indice pega o value que ta dentro da key uf que corresponde ao indice 0 (Rio de Janeiro)
