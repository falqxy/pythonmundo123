d = float(input('Qual a distancia da viagem em Km: '))
if d <= 200:
    print('Você pagará R${:.2f}' .format(d * 0.50))
else:
    print('Você pagará R${:.2f}' .format(d *0.45))

# certinho

'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância < 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))'''

#é bom estudar essa estrutura de if else que é a simples
