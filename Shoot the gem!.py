import pgzrun
import random

WIDTH=600
HEIGHT=600
score=0
TITLE="Shoot the gem!"
gameover=0

gem=Actor("gem")
gem.x=random.randint(20,550)
gem.y=20

gun=Actor("gun")
gun.x=100
gun.y=450

def draw():
    screen.fill("blue")
    if gameover:
        screen.draw.text("gameover",color="red",topleft=(10,10))

        screen.draw.text("Score:"+str(score),color="red",topleft=(20,20))
    else:
        gem.draw()
        gun.draw()
     
        screen.draw.text("Score:"+str(score),color="red",topleft=(20,20))
    

                    

def update():
    global score,gameover
    gem.y=gem.y+2
    if gem.y>HEIGHT:
        gem.x=random.randint(20,550)
        gem.y=20
        gameover=True
    if keyboard.left:
        gun.x=gun.x-2
    if keyboard.right:
        gun.x=gun.x+2
    if gem.colliderect(gun):
        score+=10
        gem.x=random.randint(20,550)
        gem.y=20









pgzrun.go()