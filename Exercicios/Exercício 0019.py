# ______ Exercício 0019 ______

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]

print(f'O aluno escolhido foi {choice(alunos)}.')
