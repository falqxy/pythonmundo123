num = []

for val in range (0, 5):
    n = (int(input('Digite um valor: ')))
    for c, v in enumerate(num):
        if n < v:
            num.insert(c, n)
            break
print(f'Os valores em ordem digitados são {num}')