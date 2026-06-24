from time import sleep

def contador(i, f, passo):
    passo = abs(passo)
    if i > f:
        passo = -passo
        f -= 1
    elif passo == 0:
        passo = 1
        f += 1
    else:
        f += 1
    print(f'Contagem de {i} até {f - 1 if passo > 0 else f + 1} de {abs(passo)} em {abs(passo)}') #claudezudo nesse print
    for c in range(i, f, passo):
        print(c, end=' ')
        sleep(0.1)

contador(1, 10, 1)
print()
contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
passo = int(input('Passo: '))
contador(i, f, passo)

#no fim, deu certo

#o codigo que eu tinha feito tava "funcionando"
#tinha feito assim antes de ver a correcao pra ajustar as contagens de 0 a 10 e 10 a 0
#o professor fez com while, realmente era mais facil kk

'''from time import sleep

def contador(i, f, passo):
    print(f'Contagem de {i} até {f-1} de {abs(passo)} em {abs(passo)}')
    for c in range(i, f, passo):
        print(c, end=' ')
        sleep(0.1)
        

contador(1, 11, 1)
print()
contador(12, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
passo = int(input('Passo: '))
passo = abs(passo) #claudezudo
if i > f:
    passo = -passo
    f -= 1 
    #if i > f:
    #passo = -passo
    #f = f-1 tinha feito assim
elif passo == 0:
    passo = 1
    f += 1
else:
    f += 1

contador(i, f, passo)

#fiz mais ou menos'''