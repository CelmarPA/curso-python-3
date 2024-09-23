n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print(f'A sua média foi {m:.2f}.')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print(f'A sua média foi {m:.2f}.')

if m >= 6:
    print(f'A sua média foi boa! Parabéns!')
else:
    print(f'A sua média foi ruim! Estude mais!')

# If simplificado
print('Parabéns!' if m >= 6 else 'Estude mais!')
