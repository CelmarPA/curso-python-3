def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)


"""def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)"""

"""def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valore {núm} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 5)"""


"""def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print(f'FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 5)
"""
"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print(f'')


# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
"""