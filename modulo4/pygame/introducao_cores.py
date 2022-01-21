
import pygame
pygame.init()

Screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Teste de Cores')

branco = (255,255,255) #RGB
preto = (0,0,0)
vermelho = (255,0,0)

#pygame.display.update()

game_exit= False

while not game_exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True

    Screen.fill(vermelho)
    pygame.display.update()

pygame.quit()
quit()