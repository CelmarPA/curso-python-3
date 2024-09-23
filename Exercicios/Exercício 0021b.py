# ______ Exercício 0021 ______

# Importar biblioteca
import pygame

# Iniciar o pygame
pygame.init()

# Carregar o arquivo
pygame.mixer.music.load('music.mp3')

# Tocar a musica
pygame.mixer.music.play()

# Solicita um evento
input('Pressione ENTER para encerrar!')

# Aguarda até o evento para finalizar
pygame.event.wait()
print('Obrigado por ouvir!')
