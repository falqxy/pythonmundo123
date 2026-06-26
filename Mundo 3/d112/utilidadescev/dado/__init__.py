def leiadinheiro(msg):
    while True:
        n = input(msg)
        if ',' in n:
            n = n.replace(',', '.')
        if n.replace('.', '').isnumeric(): #eu tinha feito essa logica mas sem o replace
            return float(n)
        print(f'"{n}" é um valor inválido')
