l1 = float(input('Digite o comprimento de uma reta: '))
l2 = float(input('Digite o segundo comprimento de uma reta: '))
l3 = float(input('Digite o terceiro comprimento de uma reta: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('As retas podem formar um triângulo')
    if l1 == l2 and l2 == l3:
        print('O triângulo é EQUILÁTERO')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('O triângulo é ISÓSCELES')
    else:
        print('O triângulo é escaleno')
else:
    print('As retas não podem formar um triângulo')
 
#certo

#trabalhamos com if dentro do if, so acontece a verificacao do tipo de triangulo se der pra
#formar triangulo com as retas

#arrumei pq nao li no enunciado que tinha que ter o sistema de verificar que dava pra foramr o triangulo 
#e acabei excluindo