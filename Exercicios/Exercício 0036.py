# ______ Exercício 0036 ______

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa. O salário do comprador e em quantos anos ele vaio pagar.
# Calculo o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
# será negado.

# Lista de Cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m'}

# Título do Programa centralizado e em cores
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{"Simulador de Empréstimos":^60}{cores["reset"]}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)

# Solicita as informações ao usuário
valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

# Calcula a parcela
parcela = valor / (anos * 12)

# Imprime a mensagem com valor da casa quantidade de anos e valor da prestação
print(f'Para pagar uma casa de {cores["blue"]}R${valor:.2f}{cores["reset"]} em {cores["blue"]}{anos}{cores["reset"]} '
      f'anos a prestação será de {cores["blue"]}R${parcela:.2f}{cores["reset"]}.')

# Condição para concentimento ou não do empréstimo
if (valor / (anos * 12)) > (salario * 0.30):
    print(f'Empréstimo {cores["red"]}NEGADO!{cores["reset"]}')
else:
    print(f'Emprestimo pode ser {cores["green"]}CONCEDIDO!{cores["reset"]}')
