import pygame

pygame.init()
pygame.display.set_caption("Space invaders!")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False
#Player
timer = 0
xpos = 400
ypos = 750
moveLeft = False
moveRight = False
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
        
    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos-=5
        if self.ypos < 0:
            self.isAlive = False
            self.xpos = xpos
            self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 3, 20))
bullet = Bullet(xpos+28, ypos)

class Alien:
    def move(self, time):
        if timer%500==0:
            self.ypos+=100
            self.direction *=-1
            return 0
        if time % 60 == 0:
            self.xpos+=10*self.direction
        return time
            
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
       
armada = []
for i in range (4):
    for j in range (9):
        armada.append(Alien(j*70+80, i*80+70))
while not gameover: #game loooop
    clock.tick(60)
    timer += 1
    #input whoooo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True#Quit game
       
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xpos-=5
            moveLeft = True
               
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            moveLeft = False
           
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            xpos+=5
            moveRight = True
               
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            moveRight = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            shoot = True
    
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            shoot = False
               
    #Physics section----------------------------------------------
   
    #check variables input
    if moveLeft == True:
        vx =- 3
    else:
        vx = 0
   
    if moveRight == True:
        vx = 3
    else:
        vx = 0
       
    for i in range (len(armada)):
        timer = armada[i].move(timer)

    if shoot == True:
        bullet.isAlive = True
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)
    else:
        bullet.xpos = xpos+28
        bullet.ypos = ypos
    
       
    #update player position
    xpos += vx
   
    #Render section----------------------------------------------------
   
    screen.fill((0,0,0)) #wipe screen
    for i in range (len(armada)):
        armada[i].draw()
    bullet.draw()
    pygame.draw.rect(screen, (0, 250, 0), (xpos, 750, 60, 20)) #Player
    pygame.draw.rect(screen, (0, 250, 0), (xpos+10, 745, 40, 20))
    pygame.draw.rect(screen, (0, 250, 0), (xpos+25, 730, 10, 30))

    pygame.display.flip() #Flips buffer

#End game loop

pygame.quit()