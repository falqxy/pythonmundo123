frase = input('Digite uma frase: ').strip()
print('Existem {} letra "A" nessa frase' .format(frase.lower().count('a')))
print('O primeiro "A" aparece em: {}'.format(frase.lower().find('a')+1)) #esta correto mas pro usuario leigo sempre vai estar na posicao 1, entao +1
print('O último "A" aparece em {}' .format(frase.lower().rfind('a')+1)) #esta correto mas pro usuario leigo sempre vai estar na posicao 1, entao +1
