n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
div = n1 / n2
dint = n1 // n2
exp = n1 ** n2

print('A soma é {}, a multiplicação {}, a divisao {:.3f}, a div inteira {} e a exponenciacao {}' .format(s, m, div, dint, exp))

#o uso de :3.f em divisao é pra limitar se for uma divisao muito alta com numeros floats
#a repeticao de numeros (esqueci o termo) em 3 casas apos a virgula


#/////////////////////////////////////////////////////////////////////////////////////////////////////


#PARA O CODIGO NAO FICAR MUITO GRANDE E NAO SAIR DA TELA ELE COLOCOU 2 PRINTS
#ASSIM FAZENDO COM QUE A LINHA QUEBRE, PARA NAO QUEBRAR É SO USAR end=''

#print('A soma é {}, a multiplicação {}, a divisao {:.3f}'.format(s, m, div), end='')
#print('a div inteira {} e a exponenciacao {}'.format(dint, exp))

#//////////////////////////////////////////////////////////////////////////////////////////////////////

#PARA QUEBRAR A LINHA DURANTE A EXECUCAO DO PRINT USAMOS \n

#print(' A soma é {}, \n a multiplicação {}, \n a divisao {:.3f}, \n a div inteira {} \n e a exponenciacao {}' .format(s, m, div, dint, exp))