import pygame
from pygame.locals import *
from sys import exit

background_image_filename ='fundo.jpg'
logo_image_filename = 'selo.png'

pygame.init()

screen =pygame.display.set_mode((640, 480),0, 32)

background = pygame.image.load(background_image_filename).convert()
logo = pygame.image.load(logo_image_filename)

clock = pygame.time.Clock()

# posição inicial
x = 0 

# velocidade  do movimento
speed = 300


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(logo,(x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    if x > 640:
        x -= 640 # aula 4.6 min 3:47


    pygame.display.update()