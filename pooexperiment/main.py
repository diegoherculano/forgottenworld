import pygame
import sys
from modulos import GameObject

pygame.init()
pygame.font.init()
pygame.display.set_caption('Forgotten World')
background = GameObject('background.jpg', 0, 0)
char = GameObject('player.png', 220, 300)

while 1:
    background.create()
    char.create()
    char.Gamepad()
    char.npc('player2.png', 300, 300, 'Olá seja bem vindo ao meu jogo!')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    pygame.time.delay(10)
