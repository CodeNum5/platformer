import pygame 
from pygame.locals import *

pygame.init()

#load 
bg = pygame.image.load('assets/background.png')
grass = pygame.image.load('assets/grass.png')
dirt = pygame.image.load('assets/dirt.png')

displayHeight = 805
displayWidth = 1535
tileSize = 200

def drawGrid():
    for line in range(0, 6): 
        pygame.draw.line(display, (255, 255, 255), (0, line * tileSize), (displayWidth, line * tileSize))
        pygame.draw.line(display, (255, 255, 255), (line * tileSize, 0), (line * tileSize, displayHeight))

display = pygame.display.set_mode((displayWidth, displayHeight)) 
pygame.display.set_caption('Platformer')
pygame.display.set_icon(grass)

running = True

#game data
level1_data = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1], 
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1], 
               [1, 1, 1, 1, 1]]

level_data = [level1_data]

#level 


while running:
    pygame.transform.scale(bg, (1535, 805))
    display.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()