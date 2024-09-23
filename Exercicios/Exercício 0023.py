# ______ Exercício 0023 ______

# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada uma dos digitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 3
# Fazer como string e matematicamente

num = int(input('Digite um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'''Analisando o número {num}
Ele possui:
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m} ''')

# ______ Exercício 0023 outra solução ______

num = int(input("Digite um número: "))
n = str(num)
print(f'''Analsando o número {num}
Ele possui:
Unidade: {len(n)-1}
Dezena: 
Centena: 
Milhar: ''')