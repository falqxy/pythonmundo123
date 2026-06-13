# LISTAS DIFERENTES DE TUPLAS, SAO MUTAVEIS, OU SEJA PODEMOS ALTERAR AS LITAS AO DECORRER DO CODIGO, UTILIZAM [] INVES DE ()
# s.append '' cria um novo espaço na memoria e adiciona oq quiser
# s.insert (0, '') move quem esta do 0 pra casa da frente sucessivamente e a adiciona oq quiser na casa escolhida
# del s[3] deleta o elemento 3
# s.pop[3] remove tambem
# s.remove('pizza') elimina por conteudo, nao pela numeracao da lista
# s.sort ordena todos os valores
# s.sort(reverse = True) ordena invertido
# len(s) para ver o tamanho da lista

'''num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não existe numéro 4 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

'''a = [2, 3, 4, 7]
b = a
b[2] = 8
print(a)
print(b)'''

#[2, 3, 8, 7]
#[2, 3, 8, 7]

#isso e oq ele vai printar, quando voce usa o = voce cria uma conexao entre 2 strings
#se voce alterar uma altera outra tambem, agora o jeito pra fazer copia de uma lista é

'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(a)
print(b)'''

#[2, 3, 4, 7]
#[2, 3, 8, 7]
