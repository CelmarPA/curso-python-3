# ______ Exercício 0048 ______

# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.
count = 0
summ = 0
for odd in range(1, 501, 2):
    if odd % 3 == 0:
        summ += odd
        count += 1
print(f'A soma de todos os {count} valores solicitados é {summ}.')
