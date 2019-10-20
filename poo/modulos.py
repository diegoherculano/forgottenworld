import pygame

screen = pygame.display.set_mode((640, 480))

class GameObject:
    def __init__(self, local, x, y):
        image = pygame.image.load(local).convert()
        self.local = local
        self.x = x
        self.y = y
        self.image = image
        self.gamepad = self.Gamepad()
        self.getx = self.getX()
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def create(self):
        self.pos = self.image.get_rect().move(self.x, self.y)
        screen.blit(self.image, self.pos)
    def Gamepad(self, up=1, down=1, left=1, right=1):
        if pygame.key.get_pressed()[pygame.K_UP] and up == 1:
            self.y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN] and down == 1:
            self.y += 1
        if pygame.key.get_pressed()[pygame.K_LEFT] and left == 1:
            self.x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT] and right == 1:
            self.x += 1
        return self.x, self.y
    def write(self, any, posx, posy, seg=1000):
        self.font = pygame.font.SysFont("Ubuntu", 15)
        self.text = self.font.render(any, True, (255, 255, 255))
        screen.blit(self.text, (posx, posy))
        pygame.display.update()
        pygame.time.delay(seg)
    def npc(self, local, imgx, imgy, txt):
        image2 = pygame.image.load(local).convert()
        self.txt = txt
        self.imgx = imgx
        self.imgy = imgy
        self.imgnpc = image2
        self.posnpc = self.imgnpc.get_rect().move(self.imgx, self.imgy)
        screen.blit(self.imgnpc, self.posnpc)
        if self.x == (self.imgx - self.pos[2]) and (self.imgy - self.pos[3]) <= self.y <= (self.imgy+self.posnpc[3]):
            self.x -= 1
        if self.y == (self.imgy+self.posnpc[3]) and (self.imgx - self.pos[2]) <= self.x <= (self.imgx+self.posnpc[2]):
            self.y += 1
            self.write(self.txt, self.imgx, self.imgy)
        if self.x == (self.imgx+self.posnpc[2]) and (self.imgy - self.pos[3]) <= self.y <= (self.imgy+self.posnpc[3]):
            self.x += 1
        if self.y == (self.imgy - self.pos[3]) and (self.imgx - self.pos[2]) <= self.x <= (self.imgx+self.posnpc[2]):
            self.y -= 1
