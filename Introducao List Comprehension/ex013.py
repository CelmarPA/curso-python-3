""" Exercício 013 - Você tem uma lista de alunos, cada um representado por um dicionário com informações sobre o aluno,
    incluindo o nome, as notas em diferentes disciplinas e o ano em que estão estudando. Sua tarefa é calcular a média
    de cada aluno e criar uma nova lista contendo os nomes dos alunos com uma média geral superior a 7.

    students = [
    {'name': 'Alice', 'grades': {'math': 8, 'history': 7, 'english': 9}, 'year': 2},
    {'name': 'Bob', 'grades': {'math': 6, 'history': 7, 'english': 8}, 'year': 1},
    {'name': 'Charlie', 'grades': {'math': 9, 'history': 8, 'english': 7}, 'year': 3},
    {'name': 'David', 'grades': {'math': 7, 'history': 6, 'english': 8}, 'year': 2},
    {'name': 'Eva', 'grades': {'math': 8, 'history': 7, 'english': 6}, 'year': 1}]

    Você deve usar list comprehension para criar uma nova lista chamada high_achievers contendo os nomes dos alunos
    com uma média geral superior a 7. Não se esqueça de calcular a média corretamente! """

# Lista de alunos
students = [
    {'name': 'Alice', 'grades': {'math': 8, 'history': 7, 'english': 9}, 'year': 2},
    {'name': 'Bob', 'grades': {'math': 6, 'history': 7, 'english': 8}, 'year': 1},
    {'name': 'Charlie', 'grades': {'math': 9, 'history': 8, 'english': 7}, 'year': 3},
    {'name': 'David', 'grades': {'math': 7, 'history': 6, 'english': 8}, 'year': 2},
    {'name': 'Eva', 'grades': {'math': 8, 'history': 7, 'english': 6}, 'year': 1}
]


# Função para calcular média
def calc_media(grades):
    return sum(grades.values()) / len(grades)


# Cria uma lista com os alunos com média maior que 7
high_achievers = [alunos['name'] for alunos in students if calc_media(alunos['grades']) > 7]

print(high_achievers)
