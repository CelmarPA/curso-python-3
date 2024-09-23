def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')


"""def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(2, 2)
somar(6)"""

"""def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')"""

"""def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
# Programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')"""

"""def somar(a=0, b=0, c=0):
    """"""
    -> Faz a soma de três valore e mostra o resultado na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: não possui
    """
"""   s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()"""

"""def contador(i, f, p):
    """"""
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """"""
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print(f'FIM!')
"""

"contador(0, 100, 10)"

"help(contador)"
