'''

import pygame


class PlayerClass:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.xPos = 0
        self.yPos = 0
        self.width = 50
        self.height = 50

    def move(self):
        movementSpeed = 10
        xMovement = 0
        yMovement = 0
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_w]:
            yMovement = movementSpeed
        elif keyPressed[pygame.K_a]:
            xMovement = -movementSpeed
        elif keyPressed[pygame.K_s]:
            yMovement = -movementSpeed
        elif keyPressed[pygame.K_d]:
            yMovement = movementSpeed

        print(yMovement)
        print(xMovement)













def draw_player():
    hey = 21

'''