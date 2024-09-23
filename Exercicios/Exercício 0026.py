# ______ Exercício 0026 ______

# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.

frase = str(input("Digite um frase: ")).strip().lower()

print(f'''A letra A aparece {frase.count("a")} na frase.
A letra A aparece a primeira vez na posição {frase.find("a") + 1}.
A letra A aparece a última vez na posição {frase.rfind("a") + 1}.''')
