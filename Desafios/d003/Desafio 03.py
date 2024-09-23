""" DESAFIO 03 - Crie um script Python que leia dois números e tente mostrar
    a soma entre eles.

    Primeiro número: 6
    Segundo número: 3
    A soma é 9!
    
"""
print(f'====== DESAFIO 03 ======')

# Solicita os número ao usuário. Usa int para converter as string em inteiros.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

# Faz a soma dos dois números
soma = n1 + n2

# Imprime o resultado
print(f'A soma é {soma}!')
