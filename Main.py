
# Import libraries
from Structure import StructureClass
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


# tiangna dnnasdnas das nasdn asdn nasdn wannds adnwandn nwan n d'
structure = StructureClass(5, gameWindow)


# Load images
graveyard = pygame.image.load('Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (1000, 1000))







Running = True

while Running:
    timer.tick(fps)

    gameWindow.fill('blue')

    structure.move()
    structure.draw_structure(graveyard)

    # gameWindow.blit(graveyard, (structure.xPos, structure.yPos))



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
