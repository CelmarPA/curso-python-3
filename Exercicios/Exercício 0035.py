# ______ Exercício 0035 ______

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não fomar um triângulo.

# Imprime o enunciado do programa
print(f'-=-' * 20)
print(f'Analisador de triângulos')
print(f'-=-' * 20)

# Solicita ao usuário as três retas
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print(f'Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo!')
