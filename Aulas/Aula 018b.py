"""test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])  # Cuidado para não esquecer de copiar a lista
test[0] = 'Maria'
test[1] = '22'
galera.append(test[:])
print(galera)"""

"""galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')"""

galera = list()
dados = list()
totmaior = 0
totmenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])  # Ficar atento a [:] para gerar copia dos dados
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
