print(f'\033[0;97;41m Teste \033[m')
print(f'\033[4;33;44m Teste \033[m')
print(f'\033[1;35;43m Teste \033[m')
print(f'\033[30;42m Teste \033[m')
print(f'\033[m Teste \033[m')
print(f'\033[030;107m Teste \033[m')

nome = 'Celmar'
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[30;107m'}

print(f'Olá! Muito prazer em te conhecer, {cores["amarelo"]}{nome}{cores["limpa"]}')
print(f'Olá! Muito prazer em te conhecer, {cores["pretoebranco"]}{nome}{cores["limpa"]}')
