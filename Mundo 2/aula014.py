#quando sabemos quantas repeticoes queremos usamos
#for c in range (str, str):
#agora quando nao soubermos usamos o enquanto
#while not str:
    #comando
#comando


n = None #gambiarra pra funcionar, a variavel n tem que ser declarada, usa o 0 ou none pra atribuir valor
par = 0
impar = 0
while n != 0: #enquanto n for diferente de 0
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1  
print(f'Voce digitou {par} números pares e {impar} ímpares')
print('Fim')

