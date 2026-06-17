#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

#for c in range(0, 4):

#print(c)

#print(‘Acabou’)


'''for c in range (6, 0, -1): #-1 conta de tras pra frente, ele vai tirando, sem isso nao funciona
#for c in range (0, 8, 2): pulando de dois em doi
    print(c) #vai printar uma contagem
print('FIM')'''

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: ')) #quantos numeros vai pular
for c in range (i, f+1, p): #o mais um é necessario se n ele conta 1 numero a menos por conta do 0
    print(c)
print('FIM')
