# Importação de pacotes e classes
from lib.classes. usuario import *
from lib.classes. transacao import *

# Exemplo de uso da classe Livro

# Criando instâncias de Livro e Usuario e atribuindo ids
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605)
livro1.id = 1
livro2 = Livro("1984", "George Orwell", 1949)
livro2.id = 2
livro3 = Livro("Saudades", "George Orwell", 1955)
livro3.id = 3

usuario1 = Usuario("Celmar Pereira")
usuario1.id = 1
usuario2 = Usuario("Valmir Lucas")
usuario2.id = 2

# Adicionando os livros à lista
Livro.livros.append(livro1)
Livro.livros.append(livro2)
Livro.livros.append(livro3)
Usuario.usuarios.append(usuario1)
Usuario.usuarios.append(usuario2)

# Adicionando livros aos usuários
usuario1.livros = livro1.to_dict()
usuario1.livros = livro2.to_dict()
usuario2.livros = livro2.to_dict()

# Salvando os livros em um arquivo JSON
Livro.salvar_livros()
Usuario.salvar_usuarios()

# Carregando os livros do arquivo JSON
Livro.carregar_livros()
Usuario.carregar_usuarios()
usuario1.livros = livro1.to_dict()

# Imprimindo as informações
Livro.informacoes_livro()
Usuario.informacoes_usuario()

usuario1.remover_livro(livro2.to_dict()['id'])

Livro.salvar_livros()
Usuario.salvar_usuarios()
Livro.carregar_livros()
Usuario.carregar_usuarios()

Usuario.informacoes_usuario()

transacao_emprestimo = Transacao(usuario=usuario1)

transacao_emprestimo.realizar_emprestimo(livro3)
Usuario.informacoes_usuario()
Livro.salvar_livros()
Usuario.salvar_usuarios()
Livro.carregar_livros()
Usuario.carregar_usuarios()
