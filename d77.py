palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:  # 'p' percore as strings em 'palavras'
    print(f'\nNa palavra {p.upper()} temos as vogais:', end=' ') #\n no comeco pra quebrar a linha quando o loop voltar e end pra continnur o print de baixo
    for letra in p:  # p pq ele pega a palavra onde o looping p está
        if letra in 'aeiou':
            print(f'{letra.upper()}', end=' ')
