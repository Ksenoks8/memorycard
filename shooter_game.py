#библиотеки
from pygame import *
from random import randint


window = display.set_mode((700, 500))
display.set_caption('Инопришленцы')
backgroung = transform.scale(image.load('galaxy.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()




#основной класс
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс игрока
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 30:
            self.rect.x -= 10
        if keys_pressed[K_d] and self.rect.x < 610:
            self.rect.x += 10
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15)
        bullets.add(bullet)
#класс врага
g=0
class Enemy(GameSprite):
    def update(self):
        global g
        if self.rect.y>500:
            self.rect.y=0
            self.rect.x=randint(0,700)
            g=g+1
        else:
            self.rect.y=self.rect.y+self.speed
class Asteroid(GameSprite):
    def update(self):
        if self.rect.y>500:
            self.rect.y=0
            self.rect.x=randint(0,700)
        else:
            self.rect.y=self.rect.y+self.speed

#класс пули
hg = 0
class Bullet(GameSprite):
    global hg
    def update(self):
        if self.rect.y>0:
            self.rect.y-=3
        else:
            self.kill()

player=Player('rocket.png', 325, 425, 2)


font.init()
font = font.SysFont('Arial', 30)






monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range(5):
    monster=Enemy('ufo.png', randint(30,610), 0, randint(1,5))
    monsters.add(monster)
for i in range(2):
    asteroid=Asteroid('asteroid.png', randint(30,610), 0, randint(1,5))
    asteroids.add(asteroid)
#игровой цикл 
game = True
finish= False

while game:

    


    if finish != True:
        window.blit(backgroung,(0, 0))
        player.update()
        bullets.update()
        bullets.draw(window)
        
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        player.reset()
        
        win = font.render('Счет:'+str(hg),True,(255,215,0))
        window.blit(win,(10, 10))
        lose = font.render('Пропущено:'+str(g),True,(255,215,0))
        window.blit(lose,(10, 40))
    if sprite.spritecollide(player,monsters,False):
        finish=True
    if sprite.spritecollide(player,asteroids,False):
        finish=True
    if sprite.groupcollide(monsters,bullets,True,True):
        monster = Enemy('ufo.png', randint(30,610), 0, randint(1,5))
        monsters.add(monster)
        hg =hg+1
    if g >= 3:
        finish = True
        looser = font.render('LOSEE!!',True,(255,0,0))
        window.blit(looser,(300,200))
    if hg >= 11:
        finish = True
        winner = font.render('WINN',True,(255,0,0))
        window.blit(winner,(300,200))

        
        
        
        
       
        
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    

    clock.tick(FPS)
    display.update()