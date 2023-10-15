
# Import libraries
import math
import pygame
pygame.init()

# tiangna dnnasdnas das nasdn asdn nasdn wannds adnwandn nwan n d'
from Player import draw_player

# Set up game window
screenWidth, screenHeight = 1600, 900
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('placeholder title')

# Set frames per second
fps = 69
timer = pygame.time.Clock()

# Load images
Graveyard = pygame.image.load('Graphics/graveyard.png')







Running = True

while Running:
    timer.tick(fps)

    gameWindow.blit(Graveyard, (0, 0))

    draw_player()

    # Close game if the game windows close button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    # Update game window
    pygame.display.flip()
