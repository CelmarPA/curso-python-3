n1 = int(input('Digite um valor: '))

n2 = int(input('Digite outro valor: '))

s = n1 + n2

# Nas versões mais nova se pode usar essa formatação
print(f'A soma de {n1} + {n2} é {s}!')

# Nas versões antigas pode se usar esse formato
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
