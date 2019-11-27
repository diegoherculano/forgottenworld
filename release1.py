import sys, pygame, random
from time import sleep
### Inicializável ###
pygame.init()
pygame.font.init()
### Variáveis ###
size = width, height = 640, 480
white = (255,255,255)
red = (255,204,204)
blue = (3, 74, 236)
green = (50, 249, 47)
x = 70
y = 250
tela = 0
r = 10
fundo = (0, 0, 0)
circulo = (255,255,255)
pa = 1
bosscont = 0
pygame.display.set_caption("Forgotten World")
zerou = 0
gameover = 0
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
npc = ["images/npc1.png","images/npc2.png","images/npc3.png","images/npc4.png", "images/npc5.png", "images/capitao.png", "images/npcblack.png"]
boss = []
monster = ["images/skelwarfrente.png", "images/skelwartras.png", "images/skelwardead.png", "images/goblinfrente.png", "images/goblintras.png", "images/goblindead.png", "images/magefrente.png", "images/magecosta.png", "images/magecaido.png"]
efeitos = ["images/efeito1.png", "images/efeito2.png", "images/efeito3.png"]
#Tela
screen = pygame.display.set_mode(size)
surface = pygame.Surface(size, pygame.SRCALPHA, 32)
#Carregamento de PNGs
person = pygame.image.load(persondown[0]).convert_alpha()
faca = pygame.image.load("images/faca.png").convert_alpha()
npcsc1 = pygame.image.load(npc[0]).convert_alpha()
npcsc2 = pygame.image.load(npc[1]).convert_alpha()
npcsc3 = pygame.image.load(npc[2]).convert_alpha()
npcsc4 = pygame.image.load(npc[3]).convert_alpha()
npcsc5 = pygame.image.load(npc[4]).convert_alpha()
npcsc6 = pygame.image.load(npc[5]).convert_alpha()
npcsc7 = pygame.image.load(npc[6]).convert_alpha()
bg = pygame.image.load("bg3icons.png").convert()
bg2 = pygame.image.load("images/bg2icons.png").convert()
bg3 = pygame.image.load("images/bg3icons.png").convert()
bg4 = pygame.image.load("images/bg4icons.png").convert()
bg5 = pygame.image.load("images/bg5icons.png").convert()
bgmenu = pygame.image.load("images/bgmenu.png").convert()
bgseta = pygame.image.load("images/bgseta.png").convert_alpha()
bghistoria = pygame.image.load("images/bghistoria.png").convert()
imghistoria = pygame.image.load("images/historia.png").convert_alpha()
imgpedra = pygame.image.load("images/pedra.png").convert_alpha()
imgpick = pygame.image.load("images/pick.png").convert_alpha()
#pygame.mouse.set_visible(0)

##Funcao Efeito Circle
def rad():
    global r
    if r == 380:
        print('fim')
    else:
        r += 1

## Funcao Efeito Andar ##
andar = -1
def walk():
    global andar
    andar += 1
    if andar < 8:
        return andar
    else:
        andar = 0
        return andar
## Funcao Efeito Plasma ##
plasma = -1
cont = 0
def plasmasoma():
    global plasma, cont
    if cont == 10:
        if plasma == -1:
            plasma += 1
            cont = 0
            return plasma
        if plasma == 0:
            plasma += 1
            cont = 0
            return plasma
        if plasma == 1:
            plasma = -1
            cont = 0
            return plasma
    else:
        cont += 1
        return plasma

## FUNCAO AREA #area(241, 138, 349, 253)#
def area(topx, topy, rightx, righty):
    global x; global y;
    '''
    pygame.draw.line(screen, white, [241+23, 253], [349, 253], 2)
    pygame.draw.line(screen, white, [349, 253], [349, 138+48], 2)
    pygame.draw.line(screen, white, [241+23, 138+48], [349, 138+48], 2)
    pygame.draw.line(screen, white, [241+23, 138+48], [241+23, 253], 2)
    '''
    #pygame.draw.rect(screen, white, [topx, topy, rightx-topx, righty-topy], 2)
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
    if x == (topx) and (topy) <= y <= (righty):
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
        textx = cordtopx-60; texty = cordtopy;
        text = font.render(texto, 1, white)
        itens.append(item) ##Add na lista
        sleep(0.5)
        print(itens)
bossdead = 0
##FUNCAO MONSTROS
def monsters(img, topx, topy, rightx, righty, item):
    global x; global person;
    global y; global texty; global textx; global text; global gameover; global tela;
    global itens, bossdead, bosscont
    num = random.randint(0,100)
    if item not in itens:
        if num >= 94:
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
                bossdead += 1
                bosscont = 14
                return pygame.image.load(monster[img+2]).convert_alpha()
            else:
                return pygame.image.load(monster[img]).convert_alpha()
    else:
        return pygame.image.load(monster[img + 2]).convert_alpha()

##FUNCAO ITEM TRAP
def itemtrap(img, topx, topy, rightx, righty, item, imgx, imgy):
    global x; global person;
    global y; global texty; global textx; global text; global gameover; global tela;
    global itens; global pa;
    if item in itens:
        if x == (topx) and (topy) <= y <= (righty):
            pa = 0
        if y == (righty) and (topx) <= x <= (rightx):
            pa = 0
        if x == (rightx) and (topy) <= y <= (righty):
            pa = 0
        if y == (topy) and (topx) <= x <= (rightx):
            pa = 0
    else:
        if x == (topx) and (topy) <= y <= (righty):
            x -= 1
        if y == (righty) and (topx) <= x <= (rightx):
            y += 1
        if x == (rightx) and (topy) <= y <= (righty):
            x += 1
        if y == (topy) and (topx) <= x <= (rightx):
            y -= 1
    if pa == 1:
        screen.blit(img, pygame.rect.Rect(imgx, imgy, 0, 0)) ##Img pedra


##SOMs
if tela == 0:
    pygame.mixer.music.load('songs/Intro.mp3')
    pygame.mixer.music.play(-1)


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

if tela == 1:
    pygame.mixer.music.load('songs/I know your secret.mp3')
    pygame.mixer.music.play(0)
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

if tela == 2:
    pygame.mixer.music.load('songs/A Darkness Opus.mp3')
    pygame.mixer.music.play(-1)

##Efeito
while r < 380:
    screen.fill(fundo)
    rad()
    pygame.draw.circle(screen, circulo, (320, 240), r)
    pygame.display.update()
    pygame.time.delay(1)

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
    screen.blit(bg, (0, 0))  ##Background
    screen.blit(skel, pygame.rect.Rect(477, 196, 0, 0))  ##MonstroSkel
    screen.blit(npcsc1, pygame.rect.Rect(202, 216, 0, 0))  ##NPC1
    screen.blit(npcsc2, pygame.rect.Rect(336,104,0,0)) ##NPC2
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0)) ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(31, 10, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(30, 33, 0, 0))  ##Texto Vida


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
    npc(175, 175, 232, 240, 150, 180, 'Como você chegou a Hades?','Saqueadores nunca atacam pela frente.')
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
    pygame.time.delay(50) ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person


if tela == 3:
    pygame.mixer.music.load('songs/Air.mp3')
    pygame.mixer.music.play(-1)
x=337;y=193
sleep(0.5)
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
    if 'faca' in itens:
        screen.blit(bg2, (0, 0))  ##Background
    else:
        screen.blit(bg2, (0, 0))  ##Background
        screen.blit(faca, pygame.rect.Rect(479, 298, 0, 0))  ##Faca
    screen.blit(npcsc3, pygame.rect.Rect(397, 190, 0, 0)) ##NPC1
    screen.blit(npcsc4, pygame.rect.Rect(540, 335, 0, 0)) ##NPC2
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(31, 10, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(30, 33, 0, 0))  ##Texto Vida


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

    ##NPCs
    npc(370, 143, 425, 205, 372, 142, 'Sou o guarda de Tártaro', 'Seja cuidadoso.')
    npc(518, 293, 565, 362, 420, 292, 'Tenha cuidado com a floresta..', 'Ela é muito perigosa.')
    ##NPC Pluzze
    if textx == 420 and 'faca' in itens:
        tela = 4
    elif textx == 420:
        text = font.render('Você deveria pegar aquela faca', 1, white)
        text2 = font.render('Ela lhe ajudará na floresta', 1, white)
        textx = 419
    ##Areas
    if x < 312:
        x += 1
    if y < 192:
        y += 1
    if y > 380:
        y -= 1
    if x > 545:
       x -= 1
    area(358, 284, 384, 360)
    area(358, 299, 517, 360)
    area(406, 290, 412, 302)
    area(480, 192, 539, 360)
    area(479, 149, 569, 219)
    ##Itens
    item(446, 243, 508, 296, 'faca', 'Você achou uma faca.')
    ##Outros##
    pygame.display.update() ##Atualiza a interface
    pygame.time.delay(50) ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person

if tela == 4:
    pygame.mixer.music.load('songs/Mystery Forest.mp3')
    pygame.mixer.music.play(-1)

x=62;y=244
text = font.render('Tenha cuidado com a floresta', 1, white)  ##Apaga texto
text2 = font.render('Ela é muito perigosa!', 1, white)  ##Apaga
sleep(0.5)
while tela == 4:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)
    globin = monsters(3, 418, 164, 466, 253 , 'chave')  ##Monstro

    ##Chamada de Tela##
    screen.blit(bg3, (0, 0))  ##Background
    itemtrap(imgpedra, 419, 145, 467, 207, 'picareta', 438, 188) ##Img Pedra Funciton
    if 'picareta' not in itens: ## Some picareta
        screen.blit(imgpick, pygame.rect.Rect(545, 102, 0, 0)) ##Img picareta
    screen.blit(npcsc5, pygame.rect.Rect(546, 265, 0, 0)) ##NPC
    screen.blit(globin, pygame.rect.Rect(441, 205, 0, 0))  ##Monster
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(31, 10, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(30, 33, 0, 0))  ##Texto Vida

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
    ##Itens
    item(520, 53, 572, 87, 'picareta', 'Você achou uma picareta.')
    if 'chave' in itens:
        item(283, 265, 330, 327, 'moedas', 'Você achou moedas de ouro.')
    else:
        npc(283, 265, 330, 327, 270, 265, 'Baú trancado.')
    #NPCS
    npc(97, 153, 145, 201, 90, 152, 'Cuidado!', 'Globins selvagens.') ##Placa
    if 'moedas' in itens and textx == 450:
        npc(517, 223, 573, 289, 450, 223, 'Me dá logo isso aqui!', 'Adeus!')
        itens.remove('moedas')
        tela = 5
    elif 'moedas' in itens:
        npc(517, 223, 573, 289, 450, 223, '', '')
        if textx == 450:
            textx = 50
            if textx == 50:
                text = font.render('Me dá logo isso aqui!', 1, white)  ##Apaga texto
                #text2 = font.render('Adeus!', 1, white)  ##Apaga
                itens.remove('moedas')
                tela = 5
    else:
        npc(517, 223, 573, 289, 450, 223, 'HAHA! Jamais sairá daqui!', 'Ao menos que me pague...')
    ##Areas
    area(36, 285, 74, 419)
    area(54, 300, 115, 428)
    area(91, 318, 139, 428)
    area(114, 336, 179, 428)
    area(156, 355, 204, 419)
    area(181, 364, 212, 429)
    area(194, 378, 200, 424)
    area(39, 46, 360, 124)
    area(101, 100, 350, 152)
    area(151, 133, 350, 182)
    area(41, 155, 113, 208)
    area(38, 101, 114, 192)
    area(212, 150, 347, 257)
    area(298, 11, 368, 205)
    area(340, 8, 403, 86)
    area(376, -2, 541, 67)
    area(505, -3, 582, 67)
    area(511, 169, 567, 237)
    area(514, 162, 560, 201)
    area(389, 357, 526, 424)
    area(506, 368, 540, 424)
    area(408, 331, 510, 383)
    area(427, 316, 499, 368)
    area(188, 269, 261, 338)
    area(148, 245, 204, 308)
    area(157, 224, 200, 266)
    area(527,367,574,439)
    #Padrão Travas Bordas
    if x < 58:
        x += 1
    if y < 0:
        y += 1
    if x > 554:
        x = 551
    if y > 386:
        y = 386
    ##Outros##
    pygame.display.update() ##Atualiza a interface
    pygame.time.delay(50) ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person


if tela == 5:
    pygame.mixer.music.load('songs/Dark Quest.mp3')
    pygame.mixer.music.play(-1)
rain = []
for q in range(100):
    rainx = random.randrange(65, 580)
    rainy = random.randrange(47, 435)
    rain.append([rainx, rainy])

x=62;y=244
sleep(0.5)
while tela == 5:
    ##Saida ##
    for event in pygame.event.get():
        efeito = pygame.image.load(efeitos[plasmasoma()]).convert_alpha()
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)
    efeito = pygame.image.load(efeitos[plasmasoma()]).convert_alpha()

    ##Chamada de Tela##
    screen.blit(bg4, (0, 0))  ##Background
    screen.blit(npcsc6, pygame.rect.Rect(343, 199, 0, 0))  ##NPC
    screen.blit(efeito, pygame.rect.Rect(408, 180, 0, 0))  ##Efeito Plasma
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(31, 10, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(30, 33, 0, 0))  ##Texto Vida

    ##Animação Chuva
    for i in rain:
        i[1] += 1
        pygame.draw.circle(screen, blue, i, 1)
    for v in rain:
        v[1] += 2
        pygame.draw.circle(screen, blue, v, 1)
        if v[1] > 435:
            i[1] = random.randrange(30, 80)
            i[0] = random.randrange(65, 580)
            v[1] = random.randrange(30, 80)
            v[0] = random.randrange(65, 580)

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

    #NPCS
    npc(318, 155, 370, 222, 318, 155, 'Não temos saída.','O mago é muito forte.')

    ##Areas
    if x < 62:
        x += 1
    if y > 388:
        y -= 1
    if x > 551:
        x -= 1
    if y < 44:
        y += 1

    area(34, 37, 169, 168)
    area(145, 1, 197, 131)
    area(230, 144, 263, 185)
    area(234, 131, 261, 172)
    area(246, 5, 584, 126)
    area(433, 76, 535, 185)
    area(516, 94, 547, 142)
    area(283, 91, 392, 193)
    area(471, 361, 578, 429)
    area(496, 341, 573, 387)
    area(459, 385, 578, 427)
    area(255, 274, 320, 337)
    area(267, 256, 308, 300)
    area(270, 250, 306, 294)
    area(56, 305, 133, 375)
    area(71, 292, 119, 335)
    area(528, 195, 580, 261)
    area(533, 186, 581, 239)
    area(268, 165, 308, 209)

    ##Outros##
    pygame.display.update()  ##Atualiza a interface
    pygame.time.delay(50)  ##Delay
    #print(f'x={x} y={y}')  ##Coord do Person

    ##Passagem
    if 424 > x > 393 and y <= 177:
        tela = 6


if tela == 6:
    pygame.mixer.music.load('songs/Darkness March.mp3')
    pygame.mixer.music.play(-1)
x=305;y=274
##BOSS POSICAO
bosslist1 = [363, 335, 345, 311, 402, 383] #direita
bosslist2 = [225, 335, 199, 311, 259, 383] #esquerda
bosslist3 = [295, 335, 274, 311, 335, 383] #centro
bosscont = 0
bossdead = 0
bossn = 0
bosslife = ['┼','┼','┼']
sleep(0.5)
##FUNCAO RANDOM BOSS
def bossrandom():
    global bosscont, bossn
    if bosscont > 10 and bosscont < 12 and bossdead <= 2:
        bossn = random.randint(0,2)
        bosscont = 0
    elif bosscont > 13 and bossdead <= 2:
        if bossn <= 1:
            bossn += 1
            bosscont = 0
        if bossn == 2:
            bossn = 0
            bosscont = 0
    else:
        bosscont += 1
    #print(random.randint(0,3))
    if bossn == 0:
        return bosslist1
    if bossn == 1:
        return bosslist2
    if bossn == 2:
        return bosslist3
m = 0
while tela == 6:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    tvidaboss = ' | '.join(bosslife)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)
    textvidaboss = font.render(' ' + tvidaboss, 1, green)
    ##BOSS
    bosslist = bossrandom()
    if bossdead == 0:
        mage = monsters(6, bosslist[2], bosslist[3], bosslist[4], bosslist[5], 'life')  ##Monstro
        if 'life' in itens:
            if len(bosslife) == 3:
                x = 305
                y = 274
                bosslife.pop()
            itens.remove('life')
    if bossdead == 1:
        mage = monsters(6, bosslist[2], bosslist[3], bosslist[4], bosslist[5], 'life')  ##Monstro
        if 'life' in itens:
            if len(bosslife) == 2:
                x = 305
                y = 274
                bosslife.pop()
            itens.remove('life')
    if bossdead >= 2:
        mage = monsters(6, bosslist[2], bosslist[3], bosslist[4], bosslist[5], 'trofeu')  ##Monstro
        if 'trofeu' in itens:
            if len(bosslife) != 0:
                bosslife.pop()
            zerou = 1
            tela = 7

    ##Chamada de Tela##
    screen.blit(bg5, (0, 0))  ##Background
    screen.blit(npcsc7, pygame.rect.Rect(386, 218, 0, 0))  ##Npc
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem
    screen.blit(mage, pygame.rect.Rect(bosslist[0], bosslist[1], 0, 0))  ##Boss
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0))  ##Texto NPCS
    screen.blit(text2, pygame.rect.Rect(textx2, texty2, 0, 0))  ##Texto2 NPCS
    screen.blit(textitems, pygame.rect.Rect(31, 10, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(30, 33, 0, 0))  ##Texto Vida
    screen.blit(textvidaboss, pygame.rect.Rect(280, 450, 0, 0))  ##Texto VidaBoss

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

    ##Npcs
    npc(360, 183, 423, 254, 360, 183, 'Não consigo derrotá-lo!', 'Mas o enfraqueci! é sua chance!')
    ##Area
    if y < 254:
        y += 1
    if x < 130:
        x += 1
    if y > 378:
        y -= 1
    if x > 479:
        x -= 1
    area(129,315, 200,423)
    area(408, 316, 508,420)

    ##Outros##
    if 'trofeu' in itens and m == 0:
        pygame.mixer.music.load('songs/Land of fearless.mp3')
        pygame.mixer.music.play(-1)
        m = 1
    pygame.display.update()  ##Atualiza a interface
    pygame.time.delay(50)  ##Delay
    print(f'x={x} y={y}')  ##Coord do Person
    #print(bossdead)

if gameover == 1:
    pygame.mixer.music.load('songs/gameover.mp3')
    pygame.mixer.music.play(0)
while gameover == 1:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    bg = pygame.image.load("bgover.jpg").convert()
    screen.blit(bg, (0,0)) ##Background
    pygame.display.update() ##Atualiza a interface
    print('gameover!')
    pygame.time.delay(100)
while zerou == 1:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    bg = pygame.image.load("images/continua.png").convert()
    screen.blit(bg, (0,0)) ##Background
    pygame.display.update() ##Atualiza a interface
    print('CONTINUA')
    pygame.time.delay(100)


