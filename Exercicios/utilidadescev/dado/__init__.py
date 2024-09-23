# Lista de cores
c = ('\033[m',          # 0 - sem cor
     '\033[0;31m',   # 1 - vermelho
     '\033[0;97;42m',   # 2 - verde
     '\033[0;97;43m',   # 3 - amarelo
     '\033[0;97;44m',   # 4 - azul
     '\033[0;97;45m',   # 5 - roxo
     '\033[0;97m'       # 6 - branco
     )


def leiadinheiro(val):
    valido = False
    while not valido:
        valor = str(input(val)).replace(',', '.').strip()
        if valor.isalpha() or valor == '' or valor.isalnum():
            print(f'{c[1]}ERRO: \"{valor}\" é umm preço inválido!{c[0]}')
        else:
            valido = True
            return float(valor)
