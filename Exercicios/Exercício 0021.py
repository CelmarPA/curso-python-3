# ______ Exercício 0021 ______

# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

# Importar bibliotecas
import pygame

# Inicializar o pygame
pygame.init()

# Informar o local do arquivo
arq = "C:/Users/Celmar Pereira/Desktop/Musica/music.mp3"

# Configurar o mixer
pygame.mixer.init()

# Carregar o arquivo
pygame.mixer.music.load(arq)

# Reproduzir o arquivo MP3
pygame.mixer.music.play()

# Manter o programa em execução
while pygame.mixer.music.get_busy():
    pass

# Encerrar o programa
pygame.quit()
