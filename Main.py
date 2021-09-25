import pygame

pygame.init()

displayHeight = 805
displayWidth = 1535
tileSize = 200

bg = pygame.image.load( 'C:/Users/91976/Desktop/TheSpaceFineumX/Thespacefineum/TheSpaceFineum/Programming/GameDev/PyGame/Assets/Background.png')
grass = pygame.image.load('C:/Users/91976/Desktop/TheSpaceFineumX/Thespacefineum/TheSpaceFineum/Programming/GameDev/PyGame/Assets/Grass.png')
dirt = pygame.image.load('C:/Users/91976/Desktop/TheSpaceFineumX/Thespacefineum/TheSpaceFineum/Programming/GameDev/PyGame/Assets/Dirt.png')



def draw_grid():
    for line in range(0, 6): 
        pygame.draw.line(display, (255, 255, 255), (0, line * tileSize), (displayWidth, line * tileSize))
        pygame.draw.line(display, (255, 255, 255), (line * tileSize, 0), (line * tileSize, displayHeight))

display = pygame.display.set_mode((displayWidth, displayHeight)) 
pygame.display.set_caption('Platformer')
pygame.display.set_icon(grass)

running = True

class World():
    def __init__(self, data):
        self.tile_list = []
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1: 
                    img = pygame.transform.scale(dirt, (tileSize, tileSize))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tileSize
                    img_rect.y = row_count * tileSize
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])


#game data
level1_data = [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1], 
               [1, 0, 0, 0, 1],
               [1, 0, 0, 0, 1], 
               [1, 1, 1, 1, 1]]

level_data = [level1_data]

world = World(level1_data)

while running:
    pygame.transform.scale(bg, (1535, 805))
    display.blit(bg, (0, 0))

    world.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()