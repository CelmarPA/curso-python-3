# ______ Exercício 0010 ______

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Quanto dinheiro você tem na carteira? R$'))

usd = din / 4.81

print(f'Com R${din:.2f} você pode comprar US${usd:.2f}.')
