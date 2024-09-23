# ______ Exercício 00105 ______

# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# Lista de cores
cores = {'reset': '\033[m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m',
         'magenta': '\033[35m', 'cyan': '\033[36m', 'grey': '\033[37m'}

# Imprime o título do programa
print(f'{cores["yellow"]}-=-' * 20)
print(f'{cores["blue"]}{"Analisando e gerando Dicionários":^60}')
print(f'{cores["yellow"]}-=-{cores["reset"]}' * 20)


# Função de avaliação das notas
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou nái adicionar a situação.
    :return: Retorna o diciónario com várias informações sobre a situação da turma.
    """
    nota = dict()
    count = maior = media = menor = soma = 0
    for v in n:
        if count == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        soma += v
        media = soma / len(n)
        count += 1
    nota['total'] = count
    nota['maior'] = maior
    nota['menor'] = menor
    nota['média'] = media
    if sit is True:
        if 6 < media < 7:
            nota['situação'] = 'RAZOÁVEL!'
        elif media >= 7:
            nota['situação'] = 'BOA!'
        else:
            nota['situação'] = 'RUIM!'
    return nota


# Programa principal
resp = notas(5.5, 9.5, 3, 8.5, 9, sit=False)
print(resp)
