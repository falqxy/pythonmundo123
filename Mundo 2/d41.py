from time import sleep
from datetime import date


print(10 * ('=-') + '\033[1mCONFEDERAÇÃO NACIONAL DE NATAÇÃO' + ('=-') *10)
sleep(1)
print(10 * ('=-') + '\033[1mCARREGANDO PROGRAMA. AGUARDE...'+ ('=-') *10)
sleep(3)
print(10 * ('=-') + '\033[1mPROGRAMA CARREGADO.'+ ('=-') *10)
nasc = int(input('Qual a o ano de nascimento do atleta do atleta? '))
idade = date.today().year - nasc
print(f'Sua idade é {idade}')


if idade <= 9:
    print('O(a) atleta pertence a categoria MIRIM')
elif idade <= 14:
    print('O(a) atleta pertence a categoria INFANTIL')
elif idade <= 19:
    print('O(a) atleta pertence a categoria JUNIOR')
elif idade <= 20:
    print('O(a) atleta pertence a categoria SÊNIOR')
else:
    print('O(a) atleta pertence a categoria MASTER')

#certo