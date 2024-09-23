tempo = int(input('Quantos anos tem o seu carro? '))

if tempo <= 3:
    print(f'Carro novo.')
else:
    print(f'Carro velho.')
print('--Fim--')

tempo = int(input('Quantos anos tem o seu carro? '))

print('Carro novo.' if tempo <= 3 else 'Carro velho.')
print('--Fim--')
