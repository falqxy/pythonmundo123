from random import randint
r = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10)) #tive que ver a resolucao

print(f'Os números escolhidos foram: {r}')
print(f'O menor valor é {min(r)}')
print(f'O maior valor é {max(r)}')

#meio certo pra menos