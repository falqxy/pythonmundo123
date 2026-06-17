n = int(input('Quantos termos você quer mostrar: '))

t1 = 0 #primeiro numero de fibonnaci
t2 = 1 #segundo numero de fibonnaci
print('~'*30)
print('{} → {}'.format(t1, t2), end='')
cont = 3  #t4
while cont <= n: #t4
    t3 = t1 + t2 #a partir do 3 numero fibonnaci soma os 2 numeros anteriores t1 e t2
    print(' → {}'.format(t3), end='')
    t1 = t2 #transforma o t1 em t2
    t2 = t3 #transforma o t2 em t3 para calcularmos o prox numero
    cont += 1
print(' → FIM')

'''n = int(input('Quantos termos você quer mostrar: '))

c = 0 #contador
f = 0 #atual
p = 1 #proximo
while c < n:
    f, p = p, f + p
    print(f)
    c += 1 #adc no contador
print('Acabou')

#fiz o contador a formula eu nao entendi'''

