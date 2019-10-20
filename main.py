import sys, pygame, random
from time import sleep
### Inicializável ###
pygame.init()
pygame.font.init()
### Variáveis ###
size = width, height = 640, 480
white = (255,255,255)
red = (255,204,204)
x = 100
y = 97
gameover = 0

ve = 1; tx = 'Que ventania começou!'; tx1 = 'Tronco cortado.' ##NPC
##Textos
textx: int = 100; texty: int = 100; ##Cord Text Padrao
font = pygame.font.SysFont(("Tahoma"), 11, bold=1)
text = font.render('', 1, white)

##Listas
itens = []
vida = ['♥','♥','♥']
titem = ', '.join(itens)
tvida = ', '.join(vida)

### Imagens ###
char = ["images\\charfrente.png","images\\charfrentemov1.png","images\\charfrentemov2.png",
        "images\\charcosta.png", "images\\charcostamov1.png", "images\\charcostamov2.png",
        "images\\chardir.png", "images\\chardirmov1.png", "images\\chardirmov2.png",
        "images\\charesq.png", "images\\charesqmov1.png", "images\\charesqmov2.png",
        "images\\charespada1.png", "images\\charespada2.png"]
npc = ["images\\zelda.png"]
monster = ["images\\skelfrente.png", "images\\skeltras.png", "images\\skeldead.png"]

#Tela
screen = pygame.display.set_mode(size)
#Carregamento de PNGs
person = pygame.image.load(char[0]).convert_alpha()
npcsc1 = pygame.image.load(npc[0]).convert_alpha()
bg = pygame.image.load("bg2.png").convert()

#pygame.mouse.set_visible(0)

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
def npc(topx, topy, rightx, righty, ttx, tty, texto):
    global x; global y; global text; global textx; global texty;
    if x == (topx) and (topy) <= y <= (righty):
        x -= 1
    if y == (righty) and (topx) <= x <= (rightx):
        y += 1
        textx = ttx; texty = tty;
        text = font.render(texto, 1, white)
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
    global y; global texty; global textx; global text; global gameover;
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
                sleep(0.5)
                y += 1
            if x == (rightx) and (topy) <= y <= (righty):
                x += 1
            if y == (topy) and (topx) <= x <= (rightx):
                for i in range(0, 40):
                    person = pygame.image.load(char[random.randint(12,13)]).convert_alpha()
                    pygame.display.update()
                y -= 1
                itens.append(item)
                sleep(1)
                return pygame.image.load(monster[img+2]).convert_alpha()
            else:
                return pygame.image.load(monster[img]).convert_alpha()
    else:
        return pygame.image.load(monster[img + 2]).convert_alpha()

while gameover != 1:
    ##Saida ##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #print(event)
    ##Variáveis
    titem = ', '.join(itens)
    tvida = ' | '.join(vida)
    textitems = font.render('Itens: ' + titem, 1, white)
    textvida = font.render(' ' + tvida, 1, red)

    ##Monstro
    skel = monsters(0, 163, 68, 189, 100, 'osso')


    ##Chamada de Tela##
    screen.blit(bg, (0,0)) ##Background
    screen.blit(skel, pygame.rect.Rect(177, 86, 0, 0))  ##MonstroSkel
    screen.blit(npcsc1, pygame.rect.Rect(130, 130, 0, 0))  ##NPC1
    screen.blit(text, pygame.rect.Rect(textx, texty, 0, 0)) ##Texto NPCS
    screen.blit(textitems, pygame.rect.Rect(0, 0, 0, 0))  ##Texto Itens
    screen.blit(textvida, pygame.rect.Rect(0, 15, 0, 0))  ##Texto Vida
    screen.blit(person, pygame.rect.Rect(x, y, 0, 0))  ##Personagem

    ##Outros##
    pygame.display.set_caption("Sublime") ##Nome da Janela
    pygame.display.update() ##Atualiza a interface
    pressed = pygame.key.get_pressed() ##Recebe as hotkeys apertadas

    #print(f'x={x} y={y}') ##Coord do Person

    ### GAMEPAD ###
    if pressed[pygame.K_DOWN]:
        y += 1
        person = pygame.image.load(char[random.randint(1,2)]).convert_alpha() ##Animação andar
        text = font.render('', 1, white) ##Apaga texto
    if pressed[pygame.K_UP]:
        y -= 1
        person = pygame.image.load(char[random.randint(4,5)]).convert_alpha() ##Animação andar
    if pressed[pygame.K_RIGHT]:
        x += 1
        person = pygame.image.load(char[random.randint(7, 8)]).convert_alpha() ##Animação andar
        text = font.render('', 1, white) ##Apaga texto
    if pressed[pygame.K_LEFT]:
        x -= 1
        person = pygame.image.load(char[random.randint(10, 11)]).convert_alpha() ##Animação andar
        text = font.render('', 1, white)  ##Apaga texto
    sleep(0.1)

    #Padrão Travas Bordas
    if x < 0:
        x += 1
    if y < 0:
        y += 1
    if x > (width-28):
        x = (width-28)
    if y > (height-24):
        y = (height-24)

    ##Areas Travadas##
    area(46,5,138,80)
    area(166,142,207,195)
    ##NPCs Puzzles
    if texty == 119 and ve == 1:
        bg = pygame.image.load("bg2vento.png").convert()
        tx1 = 'A ventania passou...'
        ve = 0
    if texty == 148 and ve == 0:
        bg = pygame.image.load("bg2.png").convert()
        tx = 'Agora que o vento passou, me traga uma semente.'
        ve = 2
    if texty == 119 and ve == 2 and 'semente' in itens:
        itens.remove('semente') ##Remove da lista
        sleep(0.1)
        tx = 'Muito obrigado pela semente.'
        tx1 = 'Tronco cortado...'
    npc(114, 107, 156, 150, 100, 119, tx)
    npc(50, 152, 86, 179, 48, 148, tx1)
    ##Items
    item(208, 151, 224, 178, 'semente', 'Voce achou uma semente.')
    item(25, 65, 36, 75, 'pedra', 'Voce achou uma pedra.')

while 1:
    screen.blit(bg, (0,0)) ##Background
    pygame.display.set_caption("Sublime") ##Nome da Janela
    pygame.display.update() ##Atualiza a interface
    print('gameover!')
    sleep(1)


