"""a = [2, 3, 4, 7]
b = a
b[2] = 8"""  # Assim que uma lista é igualada a outra elas são linkadas

a = [2, 3, 4, 7]
b = a[:]  # Cria uma copia de da lista A dentro de B
b[2] = 8  # Assim que uma lista é igualada a outra elas são linkadas


print(f'Lista A: {a}')
print(f'Lista B: {b}')


"""num = (2, 5, 9, 1)
num[2] = 3 # Tupla são imutáveis
print(num)"""

"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print(f'Não achei o número 5.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')"""

"""valores = list()  # ou valores = lis()
valores.append(5)
valores.append(9)
valores.append(4)

for count in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)"""
"""for valor in valores:
    print(f'{valor}...', end='')"""

"""for c, valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {valor}!')
print(f'Cheguei ao final da lista!')"""
