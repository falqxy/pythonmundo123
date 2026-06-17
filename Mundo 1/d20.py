import random

al1 = input('Qual o nome do primeiro aluno? ')
al2 = input('Qual o nome do segundo aluno? ')
al3 = input('Qual o nome do terceiro aluno? ')
al4 = input('Qual o nome do quarto aluno? ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)

print('A ordem de apresentação será:', lista)

#nao sabia do random.shuffle
