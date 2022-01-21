# conding: isso-8859-1 -*-

background_image_filename = 'fundo.jpg'
mouse_image_filename = 'selo.png'

import pygame
from pygame.locals import *
from sys import exit

# inicializando o console
pygame.init()

#definindo a tela 
screen = pygame.display.set_mode((720, 640))

#adicionando um nome para a tela
pygame.display.set_caption("ola mundo dos games")

#definindo a imagem de background e converye para o mesmo formato do display
background = pygame.image.load(background_image_filename).convert()
#definindo a imagem do cursor (convert_alpha permite que as formas sejam desenhadas)
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():# loop infinito que fica esperando o evento quit(clio no x da janela)
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, (0,0)) #coloca o backgorund na tela
        x, y = pygame.mouse.get_pos() #obtém posição do mouse na tela

        #coloca imagem cmo o centro do cursor do mousse
        y-= mouse_cursor.get_width() / 2
        x-= mouse_cursor.get_height() / 2

        #coloca o cursor com a imagem na tela
        screen.blit(mouse_cursor,(x, y))

        # realiza o upgrade na tela 
        pygame.display.update()