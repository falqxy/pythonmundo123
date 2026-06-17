s = 0 #acumulador, somador
cont = 0  #contador
for c in range (1, 7):
    n = int(input(f'Digite o {c} número: '))
    if n % 2 == 0:
        s += n # soma os numeros armazenados na variavel n e pega o 0 do s pq sim
        cont += 1 #adiciona mais um no contador quando o if é suprido
print(f'Voce informou {cont} números pares e a soma dos valores digitados é: {s}')

#certo
#esse é bom pra estudar pq fiz a construcao de um contador e um acumulador/somador

