import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
personright = ['direita/direita0.png', 'direita/direita1.png', 'direita/direita2.png', 'direita/direita3.png', 'direita/direita4.png', 'direita/direita5.png', 'direita/direita6.png', 'direita/direita7.png', 'direita/direita8.png']
persondown = ['frente/frente0.png', 'frente/frente1.png', 'frente/frente2.png', 'frente/frente3.png', 'frente/frente4.png', 'frente/frente5.png', 'frente/frente6.png', 'frente/frente7.png', 'frente/frente8.png']
personleft = ['esquerda/esquerda0.png', 'esquerda/esquerda1.png', 'esquerda/esquerda2.png', 'esquerda/esquerda3.png', 'esquerda/esquerda4.png', 'esquerda/esquerda5.png', 'esquerda/esquerda6.png', 'esquerda/esquerda7.png', 'esquerda/esquerda8.png']
personup = ['tras/tras0.png', 'tras/tras1.png', 'tras/tras2.png', 'tras/tras3.png', 'tras/tras4.png', 'tras/tras5.png', 'tras/tras6.png', 'tras/tras7.png', 'tras/tras8.png']
loadbg = pygame.image.load('bg3.jpg').convert()
loadperson = pygame.image.load(personright[0]).convert_alpha()
personx = 70
persony = 250
andar = -1

def walk():
    global andar
    andar += 1
    if andar < 8:
        return andar
    else:
        andar = 0
        return andar

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    screen.blit(loadbg, (0,0))
    pressed = pygame.key.get_pressed() 
    if pressed[pygame.K_RIGHT]:
        personx += 1
        loadperson = pygame.image.load(personright[walk()]).convert_alpha()
    if pressed[pygame.K_DOWN]:
        persony += 1
        loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
    if pressed[pygame.K_LEFT]:
        personx -= 1
        loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
    if pressed[pygame.K_UP]:
        persony -= 1
        loadperson = pygame.image.load(personup[walk()]).convert_alpha()
    screen.blit(loadperson, pygame.rect.Rect(personx,persony,0,0))
    pygame.display.update()
    pygame.time.delay(100)