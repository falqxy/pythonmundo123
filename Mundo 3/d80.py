lista = []

for val in range(5):
    n = int(input('Digite um valor: '))
    if val == 0 or n > lista[-1]:
        lista.append(n)
        print(f'O valor {n} foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            pos += 1
print(f'A lista em ordem é {lista}')
