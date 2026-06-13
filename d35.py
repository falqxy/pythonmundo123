l1 = float(input('Digite o comprimento de uma reta: '))
l2 = float(input('Digite o segundo comprimento de uma reta: '))
l3 = float(input('Digite o terceiro comprimento de uma reta: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('As retas podem formar um triângulo')
else:
    print('As retas não podem formar um triângulo')

#ficou certo

'''print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')'''