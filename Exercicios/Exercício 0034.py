# ______ Exercício 0034 ______

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1200,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$1200,00, o aumento é de 15%.

# Solicita ao usuário o salário atual do funcionário
salario = float(input('Qual é o salário do funcionário? R$'))

# Calcula o aumento do salário
if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')
