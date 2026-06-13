sex = ''
sex = str(input('Qual seu sexo? [F/M]: ')).upper().strip()[0] #[0] so pega a primeira letra, ou seja se escrever masculino so pega o m e valida
while sex != 'F' and sex != 'M':
    print('O termo digitado é inválido! Digite novamente!')
    sex = str(input('Qual seu sexo? [F/M]: ')).upper().strip()[0]
print(f'Fim! Seu sexo é {sex}')

#certo