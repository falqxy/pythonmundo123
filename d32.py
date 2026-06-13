from datetime import date

ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year #funcao pra pegar o ano do computador escrevendo 0
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #esqueci o ano % 400 == 0 mas tava funcionando
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

#esse F e depois {} que eu usei é uma funcao nova o f-string, substitui em certas ocasioes o .format
#substitui quando a informacao e exata e nao preciso trabalhar com ela dentro da funcao