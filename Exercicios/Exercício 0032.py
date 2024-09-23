# ______ Exercício 0032 ______

# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

# Importar biblioteca
from datetime import datetime

# Solicita o ano ao usuário
ano = int(input('Que ano quer analisa? Coloque 0 para analisar o ano atual: '))

# Obtém o ano atual do sistema
if ano == 0:
    ano = datetime.now().year  # A função date.today().year também funciona

# Condição para avaliar ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÂO é BISSEXTO!')
