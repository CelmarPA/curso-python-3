# ______ Exercício 0043 ______

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# -> Abaixo de 18.5: Abaixo do peso
# -> Entre 18.5 e 25: Peso ideal
# -> 25 até 30: Sobrepeso
# -> 30 até 40: Obesidade
# -> Acima de 40: Obesidade mórbida

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'black': '\033[30m', 'magenta': '\033[35m'}

# Título do programa
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)
print(f'{cores["red"]}{"Calculadora de Ídice de Massa Corporal (IMC)":^60}')
print(f'{cores["blue"]}-=-{cores["reset"]}' * 20)

# Solicita o dados ao usuário
peso = float(input('Qual é seu peso em quilos? '))
altura = float(input('Qual é sua altura em metro? '))

# Calcula o IMC
imc = peso / (altura ** 2)

# Imprime o IMC
print(f'Seu IMC é de {cores["green"]}{imc:.1f}{cores["reset"]}.')

# Avalia o IMC
if imc < 18.5:
    print(f'Você está {cores["red"]}ABAIXO DO PESO{cores["reset"]} normal"!')
elif 18.5 <= imc < 25:
    print(f'Parabéns, você está com {cores["green"]}PESO IDEAL{cores["reset"]}!')
elif 25 <= imc < 30:
    print(f'Você esté em {cores["yellow"]}SOBRE PESO{cores["reset"]}!')
elif 30 <= imc < 40:
    print(f'Você está em {cores["magenta"]}OBESIDADE{cores["reset"]}!')
else:
    print(f'Você está em {cores["black"]}OBESIDADE MÓRBIDA{cores["reset"]}, cuidado!!!')
