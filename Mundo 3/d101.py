from datetime import date

def voto():
    idade = date.today().year - nasc
    print(f'Sua idade é {idade}')
    if idade >= 18 and idade < 65:
        print('Você tem o voto OBRIGATÓRIO!')
    elif idade >= 16 and idade < 18 or idade >= 65:
        print('Você tem o voto OPCIONAL!')
    else: 
        print('Você NÃO está apto a votar!')

nasc = int(input('Qual seu ano de nascimento? '))
voto()

#certo