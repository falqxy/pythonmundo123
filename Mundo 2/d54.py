from datetime import date
q = 0 #declara variavel q pra ser o contador de pessoas na maioridade, declara 0 pq tem q somar
for c in range (1, 8):
    ano = int(input((f'Digite o {c} ano de nascimento: '))) #ano armazena a data de nasc
    idade = date.today().year - ano #calcula ano atual - ano de nascimento pra dar a idade
    if idade >= 18: #se a idade for maior de 18
        q += 1 # adiciona mais 1 no contador (identa pra dentro do if)
print(f'Temos {q} maioridades ')

#certo