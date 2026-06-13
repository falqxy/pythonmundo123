nome = str(input('Digite seu nome: ')).strip() #tira os espaços extras
separa = nome.split()
print('Seu nome em maiúsculas é:', nome.upper())
print('Seu nome em minúsculas é:', nome.lower())
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' '))) 
print('Seu primeiro nome é {} e tem {} letras' .format(separa[0], (len(nome.split()[0]))))
