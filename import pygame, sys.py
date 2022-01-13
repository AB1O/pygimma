import pygame, sys
from pygame.locals import *
pygame.init()

resolution=(500,500)
win = pygame.display.set_mode((resolution))
fpsClock = pygame.time.Clock()


car = pygame.image.load('assets/auto1.png')
FPS = 120
width = 40
height = 60
x_pos = (250-(width/2))
y_pos = (250-(height/2))
start_pos = (x_pos,y_pos)
vel = 2.5

run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x_pos > 0:
        # pygame.transform.rotate(player,45)
        x_pos -= vel

    if keys[pygame.K_RIGHT]and x_pos < resolution[0]-width:
        x_pos += vel

    if keys[pygame.K_UP] and y_pos > 0:
        y_pos -= vel

    if keys[pygame.K_DOWN] and y_pos < resolution[1]-height:
        y_pos += vel
    win.blit(car, (start_pos))
    # win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x_pos, y_pos, width, height))  
    fpsClock.tick(FPS)
    pygame.display.update()

pygame.quit()

# https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-animation/

# https://www.youtube.com/watch?v=Lw8ndzcWFFw