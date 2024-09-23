# ______ Exercício 0031 ______

# Desenvolva um programa que pergunte a distância da viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
# para viagens até 200Km e R$0,45 para viagens mais longas.

# Solicita o usuário a distância
km = float(input("Qual é a distância da sua viagem? "))

print(f'Você está prestes a começar uma viagem de {km:.1f}Km.')

if km <= 200:
    passagem = 0.50 * km
else:
    passagem = 0.45 * km

print(f'E o preço da sua passgem será de R${passagem:.2f}.')


# ______ Exercício 0031 outra solução ______

dist = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {km:.1f}Km.')

passagem = dist * 0.50 if dist <= 200 else dist * 0.45

print(f'E o preço da sua passgem será de R${passagem:.2f}.')
