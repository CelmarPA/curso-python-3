# ______ Exercício 0044 ______

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# -> À vista dinheiro/ pix /cheque: 10% de desconto
# -> À vista no cartão: 5% de desconto
# -> Em até 2x no cartão: preço normal
# -> 3x ou mais no cartão: 20% de juros

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m'}

# Título do programa
print(f'{cores["yellow"]}{" LOJAS PYTHON " :=^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["green"]}{"Gerenciador de Pagamentos":^60}{cores["reset"]}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita o valor das compras
preco = float(input('Valor das compras: R$'))

# Imprime e solicita a opção de pagamento
print(f'''{cores["blue"]}{"FORMAS DE PAGAMENTO":^45}{cores["reset"]}
[ {cores["green"]}1{cores["reset"]} ] à vista no dinheiro / pix / cheque
[ {cores["blue"]}2{cores["reset"]} ] à vista no cartão
[ {cores["yellow"]}3{cores["reset"]} ] em 2x no cartão
[ {cores["red"]}4{cores["reset"]} ] em 3x ou mais no cartão''')

pagamento = int(input('Qual a forma de pagamento desejada? '))
if pagamento == 1:
    valor = preco - (preco * 0.10)
    print(f'Sua compra de {cores["blue"]}R${preco:.2f}{cores["reset"]} sairá por '
          f'{cores["green"]}{valor:.2f}{cores["reset"]} com desconto de 10%!')
elif pagamento == 2:
    valor = preco - (preco * 0.05)
    print(f'Sua compra de {cores["blue"]}R${preco:.2f}{cores["reset"]} sairá por '
          f'{cores["blue"]}R${valor:.2f}{cores["reset"]} com desconto de 5%!')
elif pagamento == 3:
    valor = preco
    val_parc = valor / 2
    print(f'Sua compra será parcelada em {cores["blue"]}2x{cores["reset"]} de '
          f'{cores["blue"]}R${val_parc:.2f}{cores["reset"]} sem juros.')
    print(f'Sua compra sairá por {cores["yellow"]}R${valor:.2f}{cores["reset"]}!')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        valor = preco + (preco * 0.20)
        val_parc = valor / parcelas
        print(f'Sua compra será parcelada em {cores["blue"]}{parcelas}x{cores["reset"]} de '
              f'{cores["blue"]}R${val_parc:.2f}{cores["reset"]} com juros.')
        print(f'Sua compra de {cores["blue"]}R${preco:.2f}{cores["reset"]} sairá por {cores["red"]}R${valor:.2f}{cores["reset"]}!')
    else:
        print(f'{cores["red"]}{"Quantidade de parcelas inválida, por favor recomeçe a operação!":^45}{cores["reset"]}')
        quit()
else:
    print(f'{cores["red"]}{"Forma de pagamento invalida, por favor tente novamente!":^45}{cores["reset"]}')
    quit()
