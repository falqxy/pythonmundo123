from datetime import date

ano = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano
diferenca = abs(idade - 18) 
if idade < 18: 
    print(f'Ainda não é o ano do seu alistamento! Faltam {diferenca} anos')
elif idade == 18:
    print('É o ano de voce se alistar!')
else:
    print(f'Seu alistamento ja passou há {diferenca} anos!')

#certo