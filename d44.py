preco = float(input('Digite o preço do produto: '))

pag = int(input('Qual a forma de pagamento?\n ' \
f'1 - À vista DINHEIRO/CHEQUE: 10% de desconto - \033[1;32mR${preco * 0.90:.2f}\033[m\n ' \
f'2 - À vista no CARTÃO: 5% de desconto - \033[1;32mR${preco * 0.95:.2f}\033[m\n ' \
f'3 - Até 2x no cartão: Preço normal - \033[1;32mR${preco:.2f}\033[m\n ' \
f'4 - 3x ou mais no cartão: 20% de juros - \033[1;32mR${(preco * 0.20) + preco:.2f}\033[m\n ' \
'Digite a forma de pagamento: '))

if pag == 1:
    print(f'Voce irá pagar \033[1;32mR${preco * 0.90:.2f}\033[m!')
elif pag == 2:
    print(f'Você irá pagar \033[1;32mR${preco * 0.95:.2f}\033[m!')
elif pag == 3:
    print(f'Voce irá pagar o preço normal! \033[1;32mR${preco:.2f}\033[m!')
elif pag == 4:
    print(f'Você irá pagar \033[1;32mR${(preco * 0.20) + preco:.2f}\033[m!')
else:
    print('A opção digitada é inválida!')

#certo