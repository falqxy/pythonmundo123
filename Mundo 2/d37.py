n = int(input('Digite um número inteiro: '))
conversao = int(input('Agora, digite para converter:\n 1 para binário\n 2 para octal\n 3 para hexadecimal\n Digite: '))
if conversao == 1:
    print(f'O número {n} em binário é: {bin(n)[2:]}')
elif conversao == 2:
    print(f'O número {n} em octal é: {oct(n)[2:]}')
elif conversao == 3:
    print(f'O número {n} em hexadecimal é: {hex(n[2:])}')
else:
    print('O número digitado não é uma das opções')


#dei uma colada para saber o bin, oct, hex
#tive que adicionar o [2:] tambem pq serve pra tirar as marcacoes que o compilador bota pra
# saber se um numero e bin hex ou oct, :2 comeca a escrever no terminal apos o 2 digito
#certo


#num = int(input('Digite um número inteiro: '))
#print('''Escolha uma das bases para conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')
#opcao = int(input('Sua opção: '))

#if opcao == 1:
#    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
#elif opcao == 2:
#    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
#elif opcao == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
#else:
#    print('Opção inválida. Tente novamente.')