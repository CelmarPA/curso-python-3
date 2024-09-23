""" Exercício 012 - Você tem uma lista de informações sobre livros, onde cada elemento da lista é um dicionário contendo
    o título, o autor e a pontuação do livro. Sua tarefa é criar uma nova lista contendo apenas os títulos dos livros
    com pontuação maior ou igual a 4.

    books_info = [
    {'title': 'A Tale of Two Cities', 'author': 'Charles Dickens', 'score': 4.5},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'score': 4.8},
    {'title': '1984', 'author': 'George Orwell', 'score': 3.9},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'score': 4.2},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'score': 4.6}]

    Você deve usar list comprehension para criar uma nova lista chamada 'highly_rated_books' contendo os títulos dos
    livros que têm uma pontuação igual ou superior a 4. """

# Lista de livros

books_info = [
    {'title': 'A Tale of Two Cities', 'author': 'Charles Dickens', 'score': 4.5},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'score': 4.8},
    {'title': '1984', 'author': 'George Orwell', 'score': 3.9},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'score': 4.2},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'score': 4.6}
]

# Cria a lista contendo os títulos dos livros com pontuação maior ou igual a 4
highly_rated_books = [book['title'] for book in books_info if book['score'] >= 4]

print(highly_rated_books)
