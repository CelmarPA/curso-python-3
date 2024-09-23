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
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if 5 < r['média'] < 7:
            r['situação'] = 'RAZOÁVEL!'
        elif r['média'] >= 7:
            r['situação'] = 'BOA!'
        else:
            r['situação'] = 'RUIM!'
    return r


# Programa principal
resp = notas(5.5, 9.5, 3, 8.5, 9, sit=True)
print(resp)
