import pygame
from pygame.locals import *
from sys import exit

background_image_filename ='fundo.jpg'
logo_image_filename = 'selo.png'

pygame.init()

screen =pygame.display.set_mode((640, 480),0, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename)


# coordenada da logo 
x = 0.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
             exit()

    screen.blit(background, (0,0))
    screen.blit(logo, (x, 100))
    x += 0.2 # velocidade

    # verifica se a imagem saiu da tela
    if x > 640:
        x -= 640
    
    pygame.display.update()


