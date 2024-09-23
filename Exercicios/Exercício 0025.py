# ______ Exercício 0025 ______

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo? ')).strip().upper()

print(f'Seu nome tem Silva?', 'SILVA' in nome)
