# ______ Exercício 0022 ______

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas a lestras maiúsculas e minúsculas.
# -> Quantas letras ao tdo (sem considerar espaços).
# -> Qual o primeiro nome e quantas letras ele tem.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'''Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}.
Seu nome em minusculas é {nome.lower()}.
Seu nome tem ao todo {len(nome.replace(" ", ""))} letras.  # Pode usar len(nome) - nome.count(' ')
Seu primeiro nome é {nome.split()[0]} {len(nome.split()[0])} letras.''')
