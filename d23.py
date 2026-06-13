'''n = int(input('Digite um número: '))
print('Unidade:', n[3])
print('Dezena:', n[2])
print('Centena:', n[1])
print('Milhar:', n[0])'''

#errei, essa n tinha come acertar

num = int(input ('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)