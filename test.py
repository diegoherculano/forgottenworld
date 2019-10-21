import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
images = ['direita/direita0.png', 'direita/direita1.png', 'direita/direita2.png', 'direita/direita3.png', 'direita/direita4.png', 'direita/direita5.png', 'direita/direita6.png', 'direita/direita7.png', 'direita/direita8.png']
loadbg = pygame.image.load('bg3.jpg').convert()
loadperson = pygame.image.load(images[0]).convert_alpha()
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
        loadperson = pygame.image.load(images[walk()]).convert_alpha()
    screen.blit(loadperson, pygame.rect.Rect(personx,persony,0,0))
    pygame.display.update()
    pygame.time.delay(100)