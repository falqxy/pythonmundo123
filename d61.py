'''termo = int(input('Digite o primeiro termo: ')) #em qual numero vai comecar
razao = int(input('Digite a razão: '))#quantos numeros vai pular
print('Os primeiros números sao')
decimo = termo + (10  - 1) * razao
for c in range (termo, decimo + razao, razao):
    print(c)'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('Os primeiros números são:')

c = 0#declara o c da contagem como nada 
while c < 10: #enquanto o c for menor que 10(primeiros numeros) ele vai calcular
    print(termo)
    termo += razao
    c = c+1 #adiciona +1 quando o while for concluido, quando o c chega a 10 o programa e terminado

#claude ajudou pra entender a estrutura, mas eu que fiz

#certo