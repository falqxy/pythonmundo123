lnotas = {}
def notas(*num, sit=None):
    '''    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.'''
    lnotas['quant'] = len(num)
    lnotas['maior'] = max(num) 
    lnotas['menor'] = min(num)
    lnotas['mediat'] = sum(num) / len(num)
    if sit: #claude ajudou pra botar os ifs dentro de um if, se sit for verdadeira
        if lnotas['mediat'] >= 7:
            lnotas['sit'] = 'Boa'
        elif lnotas['mediat'] >= 5:
            lnotas['sit'] = 'Razoável'
        else:
            lnotas['sit'] = 'Ruim'
    return lnotas

notas(5.5, 9.5, 10, 6.5, sit=False)
print(lnotas)

#certo