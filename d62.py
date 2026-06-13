termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('Os primeiros números são:')

c = 0  # declara o c da contagem como nada
# enquanto o c for menor que 10(primeiros numeros) ele vai calcular
while c < 10:
    print(termo)
    termo += razao
    c = c+1  # adiciona +1 quando o while for concluido, quando o c chega a 10 o programa e terminado
t = int(input(('Mais quantos termos você deseja ver? ')))
while t != 0:
    c2 = 0
    while c2 < t:
        print(termo)
        termo += razao
        c2 = c2+1
    t = int(input('Mais quantos termos você deseja ver? '))

#certo