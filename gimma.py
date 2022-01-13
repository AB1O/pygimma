import pygame, sys
from pygame.locals import *
import random
pygame.init()
pygame.display.set_caption("Jonko Driver")

run = True
skin= "1"
debugg = False
collision = True

resolution = (840, 800)
win = pygame.display.set_mode((resolution))
fpsClock = pygame.time.Clock()

def posities ():
    positielijst=[190, 315, 445, 573]
    return random.choice(positielijst)

def backies ():
    win.blit(back1,(0,back_y1))
    win.blit(back2,(0,back_y2))    
    win.blit(back3,(0,back_y3))

def randombot ():
    autos=[truck,suv,auto1,auto2,auto3]
    return random.choice(autos)

def rectneef (bot):
    return bot.get_rect

auto1 = pygame.image.load("assets/auto1.png")
auto2 = pygame.image.load("assets/auto2.png")
auto3 = pygame.image.load("assets/auto3.png")
suv = pygame.image.load("assets/suv.png")
truck = pygame.image.load("assets/truck.png")

back1 = pygame.image.load('assets/background1.png').convert()
back2 = pygame.image.load('assets/background1.png').convert()
back3 = pygame.image.load('assets/background1.png').convert()


car = pygame.image.load('assets/skin'+ skin +'.png')


bot1 = randombot()
bot2 = randombot()
bot3 = randombot()

car_rect = car.get_rect()
bot1_rect = bot1.get_rect()
bot2_rect = bot2.get_rect()
bot3_rect = bot3.get_rect()

############## Bot pos ##############
bot1_rect.x = posities()
bot1_rect.y = -500

bot2_rect.x = posities() 
if bot2_rect.x == bot1_rect.x:
    bot2_rect.x = posities()
bot2_rect.y = -897

bot3_rect.x = posities() 
if bot3_rect.x == bot1_rect.x:
    bot3_rect.x = posities()
if bot3_rect.x == bot2_rect.x:
    bot3_rect.x = posities()
bot3_rect.y = -650

############## Variables ##############
FPS = 120
car_rect.x = ((resolution[0] - car_rect.width) / 2)
car_rect.y = (((resolution[1] - car_rect.height) / 1.25)+0.6)
turnvel = 4
angle = 0
respin_speed = 1
anglespeed = 0.5
floorspeed = 5
respin = False
steering = False

back_y1=150
back_y2=-500
back_y3=0-1150


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))

############# Floor #############
    bot1_rect.y += floorspeed
    bot2_rect.y += floorspeed
    bot3_rect.y += floorspeed 
    back_y1 += floorspeed
    back_y2 += floorspeed
    back_y3 += floorspeed
    if back_y1 >= 800:

        back_y1=-1150
    if back_y2 >= 800:
        back_y2=-1150
    if back_y3 >= 800:
        back_y3=-1150        
    backies()

    car2 = pygame.transform.rotate(car, angle)
    win.blit(car2, (car_rect.x, car_rect.y))

############## Bot ##############
    win.blit(bot1, (bot1_rect.x, bot1_rect.y))
    win.blit(bot2, (bot2_rect.x, bot2_rect.y))    
    win.blit(bot3, (bot3_rect.x, bot3_rect.y))   

    if bot1_rect.y >= 800:
        bot1 = randombot()
        bot1_rect = bot1.get_rect()        
        bot1_rect.y = -297
        bot1_rect.x = posities()

    if bot2_rect.y >= 800:
        bot2 = randombot()
        bot2_rect = bot2.get_rect() 
        bot2_rect.y = -297
        bot2_rect.x = posities()

    if bot3_rect.y >= 800:
        bot3 = randombot()
        bot3_rect = bot3.get_rect() 
        bot3_rect.y = -297
        bot3_rect.x = posities()


############## Player ##############

    if respin == True:
        if angle > 0:
            angle -= respin_speed
        if angle < 0:
            angle += respin_speed


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_rect.x > 145 or keys[pygame.K_a] and car_rect.x > 145:
        respin = False
        car_rect.x -= turnvel
        angle += anglespeed
        if angle > 15:
            angle = 15

    elif keys[pygame.K_RIGHT] and car_rect.x < resolution[0] - car_rect.width - 142 or keys[pygame.K_d] and car_rect.x < resolution[0] - car_rect.width - 142:
        respin = False
        car_rect.x += turnvel
        angle -= anglespeed
        if angle < -15:
            angle = -15

    else:
        respin = True

    if keys[pygame.K_z]:
        if debugg:
            debugg = False
        elif debugg == False:
            debugg = True
        if collision == True:
            collision = False
        elif collision == False:
            collision = True

    if collision:
        if car_rect.colliderect(bot1_rect):
            print("hit")
            run=False
        elif car_rect.colliderect(bot2_rect):
            print("hit")
            run=False
        elif car_rect.colliderect(bot3_rect):
            print("hit")
            run=False

    if debugg:
        pygame.draw.rect(win, (0,255,100), (car_rect.x,car_rect.y,car_rect.width,car_rect.height), 1)       #player  
        pygame.draw.rect(win, (200,0,255), (bot1_rect.x,bot1_rect.y,bot1_rect.width,bot1_rect.height), 1)   #bot1
        pygame.draw.rect(win, (20,50,255), (bot2_rect.x,bot2_rect.y,bot2_rect.width,bot2_rect.height), 1)   #bot2
        pygame.draw.rect(win, (20,50,255), (bot3_rect.x,bot3_rect.y,bot3_rect.width,bot3_rect.height), 1)   #bot3
        pygame.draw.rect(win, (255,0,0), (0,back_y1,840,650), 1)                                            #back1
        pygame.draw.rect(win, (0,255,0), (0,back_y2,840,650), 1)                                            #back2                                          
        pygame.draw.rect(win, (0,0,255), (0,back_y3,840,650), 1)                                            #back3

    pygame.display.update()

    fpsClock.tick(FPS)
