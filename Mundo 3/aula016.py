'''lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'  # 0 ham, 1 suc, 3 pizz, 4 pud
for c in lanche:
    # toda vez que ele printa isso ele volta o looping e lanche muda pro prox item
    print(f'Eu vou comer {c}')
print('Comi pra caramba')'''

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'  # 0 ham, 1 suc, 3 pizz, 4 pud
for cont in range(0, len(lanche)):
    # se precisar mostrar a posicao
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')
print(sorted(lanche)) #sorted organiza, nesse caso em ordem alfabetica

'''for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos} ')'''  # se precisar mostrar a posicao
