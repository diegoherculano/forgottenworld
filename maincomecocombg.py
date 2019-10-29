import sys, pygame, random
from time import sleep
### Inicializável ###
pygame.init()
pygame.font.init()
### Variáveis ###
size = width, height = 640, 480
white = (255,255,255)
red = (255,204,204)
x = 70
y = 250
tela = 0
pygame.display.set_caption("Forgotten World")

##Textos
textx = 100; texty = 100; ##Cord Text Padrao
font = pygame.font.SysFont(("Tahoma"), 14, bold=1)
text = font.render('', 1, white)
textx2 = 100; texty2 = 100; ##Cord Text Padrao
text2 = font.render('', 1, white)

##Listas
itens = []
vida = ['♥','♥','♥']
titem = ', '.join(itens)
tvida = ', '.join(vida)

### Imagens ###
personright = ['images/direita/direita0.png', 'images/direita/direita1.png', 'images/direita/direita2.png', 'images/direita/direita3.png', 'images/direita/direita4.png', 'images/direita/direita5.png', 'images/direita/direita6.png', 'images/direita/direita7.png', 'images/direita/direita8.png']
persondown = ['images/frente/frente0.png', 'images/frente/frente1.png', 'images/frente/frente2.png', 'images/frente/frente3.png', 'images/frente/frente4.png', 'images/frente/frente5.png', 'images/frente/frente6.png', 'images/frente/frente7.png', 'images/frente/frente8.png']
personleft = ['images/esquerda/esquerda0.png', 'images/esquerda/esquerda1.png', 'images/esquerda/esquerda2.png', 'images/esquerda/esquerda3.png', 'images/esquerda/esquerda4.png', 'images/esquerda/esquerda5.png', 'images/esquerda/esquerda6.png', 'images/esquerda/esquerda7.png', 'images/esquerda/esquerda8.png']
personup = ['images/tras/tras0.png', 'images/tras/tras1.png', 'images/tras/tras2.png', 'images/tras/tras3.png', 'images/tras/tras4.png', 'images/tras/tras5.png', 'images/tras/tras6.png', 'images/tras/tras7.png', 'images/tras/tras8.png']
npc = ["images/npc1.png","images/npc2.png"]
monster = ["images/skelwarfrente.png", "images/skelwartras.png", "images/skelwardead.png"]

#Tela
screen = pygame.display.set_mode(size)
#Carregamento de PNGs
person = pygame.image.load(persondown[0]).convert_alpha()
npcsc1 = pygame.image.load(npc[0]).convert_alpha()
npcsc2 = pygame.image.load(npc[1]).convert_alpha()
bg = pygame.image.load("bg3.png").convert()
bg2 = pygame.image.load("images/bg2.png").convert()
bgmenu = pygame.image.load("images/bgmenu.png").convert()
bgseta = pygame.image.load("images/bgseta.png").convert_alpha()
bghistoria = pygame.image.load("images/bghistoria.png").convert()
imghistoria = pygame.image.load("images/historia.png").convert_alpha()
#pygame.mouse.set_visible(0)

## Funcao Andar ##
andar = -1
def walk():
    global andar
    andar += 1
    if andar < 8:
        return andar
    else:
        andar = 0
        return andar
## FUNCAO AREA ##
def area(topx, topy, rightx, righty):
    global x; global y;
    if x == (topx) and (topy) <= y <= (righty):
        x -= 1
    if y == (righty) and (topx) <= x <= (rightx):
        y += 1
    if x == (rightx) and (topy) <= y <= (righty):
        x += 1
    if y == (topy) and (topx) <= x <= (rightx):
        y -= 1
    return

## FUNCAO NPC ##
def npc(topx, topy, rightx, righty, ttx, tty, texto, texto2=''):
    global x; global y; global text; global textx; global texty; global text2; global textx2; global texty2;
    if x == (topx) and (topy) <= y <= (topy):
        x -= 1
    if y == (righty) and (topx) <= x <= (rightx):
        y += 1
        textx = ttx;
        if texto2 == '':
            texty = tty + 19
        else:
            texty = tty
        text = font.render(texto, 1, white)
        textx2 = ttx; texty2 = tty + 19;
        text2 = font.render(texto2, 1, white)
    if x == (rightx) and (topy) <= y <= (righty):
        x += 1
    if y == (topy) and (topx) <= x <= (rightx):
        y -= 1
    return

##FUNCAO ITEM ###
def item(cordtopx, cordtopy, cordbackx, cordbacky, item, texto):
    global x; global y; global text; global textx; global texty; global itens;
    if cordtopx <= x <= cordbackx and cordtopy <= y <= cordbacky and item not in itens:
        textx = cordtopx; texty = cordtopy;
        text = font.render(texto, 1, white)
        itens.append(item) ##Add na lista
        sleep(0.5)
        print(itens)

def monsters(img, topx, topy, rightx, righty, item):
    global x; global person;
    global y; global texty; global textx; global text; global gameover; global tela;
    global itens
    num = random.randint(0,100)
    if item not in itens:
        if num >= 90:
            if x == (topx) and (topy) <= y <= (righty):
                x -= 1
            if y == (righty) and (topx) <= x <= (rightx):
                textx = x; texty = topy;
                text = font.render('-♥', 1, red)
                if len(vida) > 1:
                    vida.remove('♥')
                elif len(vida) == 1:
                    gameover = 1
                    tela = -1
                sleep(0.5)
                y += 1
            if x == (rightx) and (topy) <= y <= (righty):
                x += 1
            if y == (topy) and (topx) <= x <= (rightx):
                textx = x;
                texty = topy;
                text = font.render('-♥', 1, red)
                if len(vida) > 1:
                    vida.remove('♥')
                elif len(vida) == 1:
                    gameover = 1
                    tela = -1
                sleep(0.5)
                y -= 1
            return pygame.image.load(monster[img+1]).convert_alpha()
        else:
            if x == (topx) and (topy) <= y <= (righty):
                x -= 1
            if y == (righty) and (topx) <= x <= (rightx):
                textx = x;
                texty = topy;
                text = font.render('-♥', 1, red)
                if len(vida) > 1:
                    vida.remove('♥')
                elif len(vida) == 1:
                    gameover = 1
                    tela = -1
                sleep(0.5)
                y += 1
            if x == (rightx) and (topy) <= y <= (righty):
                x += 1
            if y == (topy) and (topx) <= x <= (rightx):
                person = pygame.image.load(persondown[0]).convert_alpha()
                pygame.display.update()
                y -= 1
                itens.append(item)
                sleep(0.5)
                return pygame.image.load(monster[img+2]).convert_alpha()
            else:
                return pygame.image.load(monster[img]).convert_alpha()
    else:
        return pygame.image.load(monster[img + 2]).convert_alpha()

bgsetax = 98
bgsetay = 241 #241,273
while tela == 0:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    screen.blit(bgmenu, (0, 0))
    screen.blit(bgseta, pygame.rect.Rect(bgsetax, bgsetay, 0, 0))
    pressed = pygame.key.get_pressed()  ##Recebe as hotkeys apertadas
    if pressed[pygame.K_DOWN]:
        bgsetay = 273
    if pressed[pygame.K_UP]:
        bgsetay = 241
        bgmenu = pygame.image.load("images/bgmenu.png").convert()
        pygame.display.update()
    if pressed[pygame.K_RETURN]:
        if bgsetay == 241:
            pygame.time.delay(100)
            tela = 1
        if bgsetay == 273:
            bgmenu = pygame.image.load("images/bgsobre.png").convert()
            pygame.display.update()
    pygame.display.update()
    pygame.time.delay(50)

historiax = 440
while tela == 1:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    screen.blit(bghistoria, (0,0))
    screen.blit(imghistoria, pygame.rect.Rect(0,historiax,0,0))
    pressed = pygame.key.get_pressed()  ##Recebe as hotkeys apertadas

    if historiax == 0 and pressed[pygame.K_RETURN]:
        tela = 2
    elif historiax == 0 or pressed[pygame.K_RETURN]:
        historiax = 0
    else:
        historiax -= 0.5
    pygame.display.update()
    pygame.time.delay(50)

while tela == 2:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)
    skel = monsters(0, 454, 156, 503, 220, 'escudo') ##Monstro

    ##Chamada de Tela##
    screen.blit(bg, (0,0)) ##Background
    screen.blit(skel, pygame.rect.Rect(477, 196, 0, 0))  ##MonstroSkel
    screen.blit(npcsc1, pygame.rect.Rect(202, 216, 0, 0))  ##NPC1
    screen.blit(npcsc2, pygame.rect.Rect(336,104,0,0)) ##NPC2
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0)) ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(0, 0, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(0, 15, 0, 0))  ##Texto Vida
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem

    ### GAMEPAD ###
    pressed = pygame.key.get_pressed()  ##Recebe as hotkeys apertadas
    if pressed[pygame.K_DOWN]:
        y += 1
        person = pygame.image.load(persondown[walk()]).convert_alpha() ##Animação andar
        text = font.render('', 1, white) ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto
    if pressed[pygame.K_UP]:
        y -= 1
        person = pygame.image.load(personup[walk()]).convert_alpha() ##Animação andar
    if pressed[pygame.K_RIGHT]:
        x += 1
        person = pygame.image.load(personright[walk()]).convert_alpha() ##Animação andar
        text = font.render('', 1, white) ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto
    if pressed[pygame.K_LEFT]:
        x -= 1
        person = pygame.image.load(personleft[walk()]).convert_alpha() ##Animação andar
        text = font.render('', 1, white)  ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto

    #Padrão Travas Bordas
    if x < 69:
        x += 1
    if y < 0:
        y += 1
    if x > (width-28):
        x = (width-28)
    if y > (height-24):
        y = (height-24)

    ##Areas Travadas##
    area(68, 238, 201, 238)  # parede1
    area(241, 138, 349, 253)  # mesa
    area(68, 253, 195, 281)
    area(157, 254, 187, 372)
    area(148, 315, 285, 343)
    area(270, 329, 345, 371)
    area(332, 313, 432, 341)
    area(389, 220, 434, 377)
    area(391, 225, 528, 292)
    area(485, 98, 528, 293)
    area(151, 14, 199, 200)
    area(150, 16, 334, 126)
    area(355, 14, 520, 126)
    #NPCs
    npc(175, 175, 232, 240, 150, 180, 'Como você chegou a Hades?','Você nunca sairá.')
    npc(314, 62, 359, 127, 314, 62, 'Para você sair daqui,','Deverá me entregar 3 itens.')
    ##NPC Recebe Itens
    if textx == 314 and 'escudo' in itens and 'mapa' in itens and 'moeda' in itens:
        text = font.render('Até logo!', 1, white)
        text2 = font.render('', 1, white)
        itens.remove('escudo');itens.remove('mapa');itens.remove('moeda')
        tela = 3
    ##Items
    item(424,101,469,135,'moeda','Você achou uma moeda.')
    item(328,147,364,174,'mapa','Você achou um mapa.')
    #item(208, 151, 224, 178, 'semente', 'Voce achou uma semente.')

    ##Outros##
    pygame.display.update() ##Atualiza a interface
    pygame.time.delay(10) ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person

x=337;y=184
while tela == 3:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)
    ##Chamada de Tela##
    screen.blit(bg2, (0, 0))  ##Background
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(0, 0, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(0, 15, 0, 0))  ##Texto Vida
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem

    ### GAMEPAD ###
    pressed = pygame.key.get_pressed()  ##Recebe as hotkeys apertadas
    if pressed[pygame.K_DOWN]:
        y += 1
        person = pygame.image.load(persondown[walk()]).convert_alpha()  ##Animação andar
        text = font.render('', 1, white)  ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto
    if pressed[pygame.K_UP]:
        y -= 1
        person = pygame.image.load(personup[walk()]).convert_alpha()  ##Animação andar
    if pressed[pygame.K_RIGHT]:
        x += 1
        person = pygame.image.load(personright[walk()]).convert_alpha()  ##Animação andar
        text = font.render('', 1, white)  ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto
    if pressed[pygame.K_LEFT]:
        x -= 1
        person = pygame.image.load(personleft[walk()]).convert_alpha()  ##Animação andar
        text = font.render('', 1, white)  ##Apaga texto
        text2 = font.render('', 1, white)  ##Apaga texto
    ##Outros##
    pygame.display.update() ##Atualiza a interface
    pygame.time.delay(10) ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person

while gameover == 1:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    bg = pygame.image.load("bgover.jpg").convert()
    screen.blit(bg, (0,0)) ##Background
    pygame.display.set_caption("Sublime") ##Nome da Janela
    pygame.display.update() ##Atualiza a interface
    print('gameover!')
    pygame.time.delay(100)


