import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((720, 640))
pygame.display.set_caption("Desafio modulo 4")
pygame.draw.rect(screen, (255,0,0),[360,320,10,10])

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.fill((255,255,255))

        x, y = pygame.mouse.get_pos()
        print(x, y)

    pygame.display.update()