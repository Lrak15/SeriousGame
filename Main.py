
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
graveyard = pygame.transform.scale(graveyard, (500, 500))
graveyardRect = graveyard.get_rect()

xMoved = 0
yMoved = 0
movementSpeed = 2




Running = True

while Running:
    timer.tick(fps)

    gameWindow.fill('blue')








    wMoved = 0
    aMoved = 0
    sMoved = 0
    dMoved = 0

    keyPressed = pygame.key.get_pressed()



    if keyPressed[pygame.K_w]:
        wMoved = movementSpeed

    if keyPressed[pygame.K_a]:
        aMoved = movementSpeed

    if keyPressed[pygame.K_s]:
        sMoved = -movementSpeed

    if keyPressed[pygame.K_d]:
        dMoved = -movementSpeed

    if wMoved and aMoved != 0:
        wMoved = math.sin(45) * movementSpeed
        aMoved = math.sin(45) * movementSpeed

    if wMoved and dMoved != 0:
        wMoved = math.sin(45) * movementSpeed
        dMoved = -math.sin(45) * movementSpeed

    if sMoved and aMoved != 0:
        sMoved = -math.sin(45) * movementSpeed
        aMoved = math.sin(45) * movementSpeed

    if sMoved and dMoved != 0:
        sMoved = -math.sin(45) * movementSpeed
        dMoved = -math.sin(45) * movementSpeed


    structure.move(wMoved, aMoved, sMoved, dMoved)
    structure.draw(graveyard)

    pygame.draw.rect(gameWindow, ('red'), pygame.Rect(800, 450, 10, 10))

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
