# ______ Exercício 0012 ______

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input('Qual é o preço do produto? R$'))

desc = valor - (valor * (5/100))

print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${desc:.2f}.')
