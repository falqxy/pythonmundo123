n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno foi {media:.1f}')
if media < 5.0:
    print('Aluno \033[1;31mREPROVADO\033[m')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em \033[1;33mRECUPERAÇÃO\033[m')
else:
    print('Aluno \033[1;32mAPROVADO\033[m')

#Certo