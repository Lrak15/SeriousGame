
# Import libraries
import math
from random import randrange

import pygame
from pygame import mixer

from GameObjects import Enemy
from GameObjects import Player
from GameObjects import Projectile
from GameObjects import Structure
from GameObjects import StructureHitBox

pygame.init()
mixer.init()

# Set frames per second
fps = 20
timer = pygame.time.Clock()

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('Animation')

# Define center coordinates
centerX, centerY = screenWidth / 2, screenHeight / 2
print(screenWidth)
print(centerX)
print(screenHeight)
print(centerY)

# Define pixel size
# Format for new pixel size should be 320:180
px = round(screenHeight / 180)

################################################################################################################################
###   ########         ###         ###      ############         ###   ###   ###         ###         ###         ###         ###
###   ########   ###   ###   ###   ###   ###   ############   ######         ###   ###   ###   #########   #########   #########
###   ########   ###   ###         ###   ###   ############   ######         ###         ###   #########      ######         ###
###   ########   ###   ###   ###   ###   ###   ############   ######   ###   ###   ###   ###   ###   ###   ###############   ###
###        ###         ###   ###   ###      ############         ###   ###   ###   ###   ###         ###         ###         ###
################################################################################################################################

# Load images

introImages = []
imageCount = 33
for i in range(1, imageCount + 1):
    image = pygame.image.load(f'Graphics/Abstinence title screen-{i}.png.png')
    image = pygame.transform.scale(image, (screenWidth, screenWidth))
    introImages.append(image)

titleScreen = pygame.image.load('Graphics/Abstinence title screen-34.png.png')
titleScreen = pygame.transform.scale(titleScreen, (screenWidth, screenWidth))


###############################################################################################################
###         ###   ###   ###   ###   ###         ###         ###         ###         ###   ###   ###         ###
###   #########   ###   ###   ###   ###   ############   #########   ######   ###   ###   ###   ###   #########
###      ######   ###   ###         ###   ############   #########   ######   ###   ###         ###         ###
###   #########   ###   ###         ###   ############   #########   ######   ###   ###         #########   ###
###   #########         ###   ###   ###         ######   ######         ###         ###   ###   ###         ###
###############################################################################################################


for count in range(33):
    timer.tick(15)
    gameWindow.blit(introImages[count], (0, 0))
    # Update game window
    pygame.display.flip()
