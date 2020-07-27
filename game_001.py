import pygame
import random
pygame.init()    
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SPACE INVADERS")
screen.fill((255,233,233))
icon = pygame.image.load("transportation.png")
pygame.display.set_icon(icon)
player = pygame.image.load("spaceship.png")
enemy = pygame.image.load("UFO1.png")
background = pygame.image.load('bacground.png')
bullet = pygame.image.load('bullet2.png')
playerX = 0.0
playerY = 0.0
class Player:
    def __init__(self):
        self.posiionX=400
        self.posiionY=500
        self.dx=0
        self.playerImg = player

    def draw(self):
        screen.blit(self.playerImg,(self.posiionX,self.posiionY))
    def move(self):
        if self.posiionX<0:
            self.posiionX=0
        elif self.posiionX>770:
            self.posiionX=770

        self.posiionX+=self.dx
        #playerX = self.posiionX
        #playerY = self.posiionY
        
class Enemy:
    def __init__(self):
        self.posiionX= random.randint(0,736)
        self.posiionY= random.randint(0,50)
        self.img = enemy
        self.dx = 3.7
        self.dy = 60
    def draw(self):
        screen.blit(self.img,(self.posiionX,self.posiionY))
    def move(self):
        if self.posiionX >= 736 or self.posiionX <=0:
            self.dx = - self.dx
           
            self.posiionY += self.dy
        self.posiionX+= self.dx 
    def collide(self,bullett):
        bullet_mask =  bullett.getMask()
        en_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.posiionX-bullett.posiionX),round(self.posiionY-bullett.posiionY))
        colid = bullet_mask.overlap(en_mask,offset)
        return colid

class Background:
    def __init__(self):
        self.posiionX = 0
        self.posiionX1 = -600
        self.posiionX2 = -1200
        self.img = background
        self.img2 = background
        self.img3 = background
        self.dx = 2.7
    def draw(self):
        screen.blit(self.img,(0,self.posiionX))
        screen.blit(self.img,(0,self.posiionX1))
       # screen.blit(self.img,(0,self.posiionX2))
    def move(self):
        if self.posiionX >=600:
            self.posiionX=-600
          
         #   print(self.posiionX1)
        if self.posiionX1 >=600:
            self.posiionX1 = -600
        self.posiionX1+=self.dx
        self.posiionX+=self.dx
        #self.posiionX2+=self.dx
    
class Bullet:
    def __init__(self,x,y):
        self.posiionX = x
        self.posiionY = y
        self.img = bullet
        self.dx = 4.2
    def draw(self):
        screen.blit(self.img,(self.posiionX+20,self.posiionY))
    def move(self):
        self.posiionY-=self.dx
    def getMask(self):
        return pygame.mask.from_surface(self.img)
    




p1 = Player()
bg = Background()
ens = []
for i in range(10):
    ens.append(Enemy())
bullets = []
COUNTER = 1

def main():
    global COUNTER
    clock = pygame.time.Clock()
    running = True
    while running:
         
            clock.tick(120)
            screen.fill((255,233,233))
            #screen.blit(background,(0,0))
            bg.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quitting")
                    pygame.display.quit()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        p1.dx=-4.5
                    if event.key == pygame.K_RIGHT:
                        p1.dx=4.5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        p1.dx=-0.0
                    if event.key == pygame.K_RIGHT:
                        p1.dx=0.0
                    if event.key == pygame.K_UP:
                        bullets.append(Bullet(p1.posiionX,p1.posiionY))
                    
            p1.move()
            for en in ens:    
                en.move()
            for en in ens:
                en.draw()
            p1.draw()
            bg.move()
            for en in ens:
                for blt in bullets:
                    if en.collide(blt):
                        ens.remove(en)
            for bullet in bullets:
                bullet.draw()
                bullet.move()
                if bullet.posiionY<0:
                    bullets.remove(bullet) 
            if(COUNTER==120*3):
                for i in range(round(COUNTER/120)*10):
                    ens.append(Enemy())
                print("1 Sec")
                COUNTER=0
            pygame.display.update()
            COUNTER+=1
            
    
    
               
main()
print("game over")