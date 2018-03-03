import pygame, sys
from pygame.locals import *
from sys import exit


height = 800
width = 600
pygame.init()
Display = pygame.display.set_mode((height, width))
pygame.display.set_caption('Snooke')
playerSrc = 'player.png'
speed = 1
playerX = height / 2
playerY = width  / 2
player = pygame.image.load(playerSrc).convert_alpha()

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit = True
           
    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[K_LEFT]:
        playerX -= speed
    elif pressedKeys[K_RIGHT]:
        playerX += speed
    if pressedKeys[K_UP]:
        playerY -= speed
    elif pressedKeys[K_DOWN]:
        playerY += speed


    if playerX > height:
        playerX = height
    elif playerX < 0:
        playerX = 0
    if playerY > width:
        playerY = width
    elif playerY < 0:
        playerY = 0

    Display.fill((255, 165, 0))
    Display.blit(player, (playerX, playerY))


    
    pygame.display.update()
        
pygame.quit()
sys.exit()

