import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
personright = ['images\\direita\\direita0.png', 'images\\direita\\direita1.png', 'images\\direita\\direita2.png', 'images\\direita\\direita3.png', 'images\\direita\\direita4.png', 'images\\direita\\direita5.png', 'images\\direita\\direita6.png', 'images\\direita\\direita7.png', 'images\\direita\\direita8.png']
persondown = ['images\\frente\\frente0.png', 'images\\frente\\frente1.png', 'images\\frente\\frente2.png', 'images\\frente\\frente3.png', 'images\\frente\\frente4.png', 'images\\frente\\frente5.png', 'images\\frente\\frente6.png', 'images\\frente\\frente7.png', 'images\\frente\\frente8.png']
personleft = ['images\\esquerda\\esquerda0.png', 'images\\esquerda\\esquerda1.png', 'images\\esquerda\\esquerda2.png', 'images\\esquerda\\esquerda3.png', 'images\\esquerda\\esquerda4.png', 'images\\esquerda\\esquerda5.png', 'images\\esquerda\\esquerda6.png', 'images\\esquerda\\esquerda7.png', 'images\\esquerda\\esquerda8.png']
personup = ['images\\tras\\tras0.png', 'images\\tras\\tras1.png', 'images\\tras\\tras2.png', 'images\\tras\\tras3.png', 'images\\tras\\tras4.png', 'images\\tras\\tras5.png', 'images\\tras\\tras6.png', 'images\\tras\\tras7.png', 'images\\tras\\tras8.png']
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
