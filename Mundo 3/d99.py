def maior(*num):
    maiornum = 0
    for n in num:
        if n > maiornum:
            maiornum = n
    print('=-' * 20)
    print('Analisando os valores passados...')
    print(f'{num} Foram informados {len(num)} valores ao todo.\nO maior valor informado foi {maiornum}.')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#certo