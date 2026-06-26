def metade(n, show=False):
    r = n/2
    if show:
        return moeda(r)
    return r
def dobro(n, show=None):
    r = n*2
    if show:
        return moeda(r)
    return r
def aumentar(n, show=None):
    r = n * 1.10
    if show:
        return moeda(r)
    return r
def diminuir(n, show=None):
    r = n * 0.87
    if show:
        return moeda(r)
    return
def moeda(n):
        return f'R${n:.2f}'