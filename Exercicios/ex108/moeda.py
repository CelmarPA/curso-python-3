def metade(val=0):
    valor = val / 2
    return valor


def dobro(val=0):
    valor = val * 2
    return valor


def aumentar(val=0, por=0):
    valor = (val + (val * por / 100))
    return valor


def diminuir(val=0, por=0):
    valor = (val - (val * por / 100))
    return valor


def moeda(val=0, sifra='R$'):
    return f'{sifra}{val:.2f}'.replace('.', ',')
