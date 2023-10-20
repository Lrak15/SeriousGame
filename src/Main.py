
# Import libraries
#from Structures import StructureClass
#from Hitboxes import HitboxClass

from GameObjects import GameObject
from  GameObjects import Structure
from  GameObjects import HitBox
import math

import pygame
pygame.init()


# Set frames per second
fps = 69
timer = pygame.time.Clock()


# Set up game window
screenWidth, screenHeight = 1600, 900
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('placeholder title')

''''
# tiangna dnnasdnas das nasdn asdn nasdn wannds adnwandn nwan n d'
structure = StructureClass(5, gameWindow)
graveyardHitbox1 = HitboxClass(1, gameWindow, 100, 100, 50, 50)
graveyardHitbox2 = HitboxClass(1, gameWindow, 200, 200, 50, 50)
graveyardHitbox3 = HitboxClass(1, gameWindow, 300, 300, 50, 50)

graveyardHitboxes = [graveyardHitbox1, graveyardHitbox2, graveyardHitbox3]
'''

# Load images
graveyard = pygame.image.load('../Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (500, 500))
graveyardRect = graveyard.get_rect()

redHitbox = pygame.Rect(200, 200, 500, 500)


graveyardStructureTing = Structure(gameWindow, 500, 500, 100, 100)




'''
def draw_graveyardHitboxes():
    for i in range (graveyardHitboxes):
        gameWindow.blit(i)
'''

Running = True

while Running:
    timer.tick(fps)

    gameWindow.fill('blue')

    movementSpeed = 2
    GameObject.calculate_movement(movementSpeed)

    Structure.move()
    Structure.draw()









    #for


    #structure.move(wMoved, aMoved, sMoved, dMoved)
    #structure.draw(graveyard)
    #draw_graveyardHitboxes()

    pygame.draw.rect(gameWindow, ('red'), pygame.Rect(800, 450, 10, 10))

    # gameWindow.blit(graveyard, (structure.xPos, structure.yPos))


    pygame.draw.rect(gameWindow, ('red'), redHitbox, 10)



    # Check for keys pressed
    for event in pygame.event.get():
        # Close game escape key is pressed
        '''if event.key == pygame.K_ESCAPE:
            Running = False
        '''

        # Close game if the game windows close button is pressed
        '''el'''
        if event.type == pygame.QUIT:
            Running = False

    # Update game window
    pygame.display.flip()
