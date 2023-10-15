import math

import pygame


class StructureClass:
    def __init__(self, assetNumber, gameWindow):
        self.name = assetNumber
        self.gameWindow = gameWindow
        self.xPos = 0
        self.yPos = 0
        self.width = 50
        self.height = 50

    def move(self):
        movementSpeed = 5
        wMovement = 0
        aMovement = 0
        sMovement = 0
        dMovement = 0
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_w]:
            wMovement = movementSpeed

        if keyPressed[pygame.K_a]:
            aMovement = movementSpeed

        if keyPressed[pygame.K_s]:
            sMovement = -movementSpeed

        if keyPressed[pygame.K_d]:
            dMovement = -movementSpeed

        if keyPressed[pygame.K_w] and keyPressed[pygame.K_a]:
            wMovement = math.sin(45) * movementSpeed
            aMovement = math.sin(45) * movementSpeed

        if keyPressed[pygame.K_w] and keyPressed[pygame.K_d]:
            wMovement = math.sin(45) * movementSpeed
            dMovement = -math.sin(45) * movementSpeed

        if keyPressed[pygame.K_s] and keyPressed[pygame.K_a]:
            sMovement = -math.sin(45) * movementSpeed
            aMovement = math.sin(45) * movementSpeed

        if keyPressed[pygame.K_s] and keyPressed[pygame.K_d]:
            sMovement = -math.sin(45) * movementSpeed
            dMovement = -math.sin(45) * movementSpeed

        self.xPos += aMovement + dMovement
        self.yPos += wMovement + sMovement



    def draw_structure(self, graveyard):
        self.gameWindow.blit(graveyard, (self.xPos, self.yPos))













