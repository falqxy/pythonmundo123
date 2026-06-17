import math

'''cato = float(input('Qual o comprimento do cateto oposto? '))
cata = float(input('Qual o comprimento do cateto adjacente? '))
s = (cato **2) + (cata ** 2)
hipo = math.sqrt(s)
print('O comprimento da hipotenusa é de', hipo)'''

#usando agora math

cato = float(input('Qual o comprimento do cateto oposto? '))
cata = float(input('Qual o comprimento do cateto adjacente? '))
hipo = math.hypot(cata, cato)
print('O comprimento da hipotenusa é de', hipo)


