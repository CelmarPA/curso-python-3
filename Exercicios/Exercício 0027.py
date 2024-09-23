# ______ Exercício 0027 ______

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.
# Ex: Ana Maria de Souza
# Primeiro = Ana
# Último = Souza

nome = str(input('Digite o seu nome completo: ')).strip()

print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nome.split()[0]}.
Seu segundo nome é {nome.split()[-1]}.''')
