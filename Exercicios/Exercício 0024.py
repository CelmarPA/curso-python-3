# ______ Exercício 0024 ______

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Em que cidade você nasceu? ')).strip()

cid = cidade.upper().split()
print('SANTO' in cid[0])

# ______ Exercício 0024 outra solução ______

cidade = str(input('Em que cidade você nasceu? '))

print(cidade[:5].upper() == 'SANTO')
