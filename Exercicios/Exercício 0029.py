# ______ Exercício 0029 ______

# Escreva um programa que leia a velocide de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km/h acima do limite.

# Importar biblioteca
from colorama import Fore

vel = float(input('Qual é a velocidade atual do carro? '))    # Solicita ao usuário a velocidade

# Condição para multa
if vel > 80:
    multa = (vel - 80) * 7
    print(Fore.RED + f'MULTADO! Você ultrapassou o limite de velocidade permitido que é de 80Km/h!')
    print(Fore.RED + f'Você deve pagar uma multa de', Fore.LIGHTYELLOW_EX + f'R${multa:.2f}!')

print(Fore.GREEN + f'Tenha um bom dia! Dirija com segurança!')
