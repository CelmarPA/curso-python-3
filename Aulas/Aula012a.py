nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print(f'Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cáudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print(f'Seu nome é bem normal!')

print(f'Tenha um bom dia, {nome}!')
