a = 4
b =  5
s = a + b 
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1 
s = a + b
print(s)

#///////////////////////////////////////////////////////////////////////////////////////////
print('PROGRAMA PRINCIPAL 1')
#///////////////////////////////////////////////////////////////////////////////////////////

def soma(a, b):
    print(f'"A" igual a {a} e "B" igual a {b}')
    print(f'A soma de A + B é igual a {a+b}')
    print()

soma(b=4, a=5)

soma(8, 9)

soma(2, 1) #se eu botar mais um numero dentro do (), ele da erro pq so explicitei 2 parametros a e b
#para isso existe o enpacotamento

#///////////////////////////////////////////////////////////////////////////////////////////
print('PROGRAMA PRINCIPAL 2')
#///////////////////////////////////////////////////////////////////////////////////////////

def contador(*num):
    print(num)
    print(f'O tamanho da tupla é {len(num)}')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 1, 0, 9, 2]
print(valores)
def dobra(lst): #dobra os valores
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

dobra(valores)
print(valores)

def soma2(* n):
    s = 0
    for numeros in n:
        s+= numeros
    print(f'Somandos os valores {n} temos {s}')

soma2(5,2)
soma2(2, 9, 4)