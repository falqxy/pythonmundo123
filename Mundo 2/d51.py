termo = int(input('Digite o primeiro termo: ')) #em qual numero vai comecar
razao = int(input('Digite a razão: '))#quantos numeros vai pular
print('Os primeiros números sao')
decimo = termo + (10  - 1) * razao
for c in range (termo, decimo + razao, razao):
    print(c)

#errei na parte do decimo em for e botei so 10, nao sabia da formula matematica pra ir ate 10 termos
#meio certo