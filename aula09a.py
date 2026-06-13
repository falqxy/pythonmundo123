frase = 'Olá Mundo'
#frase = f1[0:3]

print (frase[0:3])
print ('Quantidade de "O" na frase:', frase.count('O'))
print ('Tamanho da frase:', len(frase))
print ('Onde começa a substring "lá":', frase.find('lá'))
print ('Existe a palavra Curso em frase:', 'Curso' in frase)
print ('Existe a palavra Video em frase:', 'Olá' in frase)
#frase.replace('Mundo', 'Humano') //troca a palavra Mundo por Humano, mas não altera a variável frase
#frase.upper() //deixa a frase toda em maiúscula, mas não altera a variável frase
#frase.lower() //deixa a frase toda em minúscula, mas não altera a variável frase
#frase.capitalize() //deixa a primeira letra da frase em maiúscula, mas não altera a variável frase
#frase.title() //deixa a primeira letra de cada palavra em maiúscula, mas não altera a variável frase
#frase.strip() //remove os espaços em branco adicionados sem querer no início e no final da frase, mas não altera a variável frase
#frase.rstrip() //o R na frente (RIGHT) remove os espaços em branco adicionados sem querer no final da frase, lado direito, mas não altera a variável frase
#frase.lstrip() //o L na frente (LEFT) remove os espaços em branco adicionados sem querer no início da frase, lado esquerdo, mas não altera a variável frase
#frase.split() //quebra a frase em uma lista de palavras, mas não altera a variável frase
#'-'.join(frase) //junta uma lista de palavras em uma frase, mas não altera a variável frase