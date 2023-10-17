import math
import pygame
# ????????????????

class GameObject:
    def __init__(self, gameWindow):
        self.gameWindow = gameWindow
        self.xPos = 0
        self.yPos = 0
        self.width = 50
        self.height = 50
        self.wMoved = 0
        self.aMoved = 0
        self.sMoved = 0
        self.dMoved = 0

    def calculate_movement(self, movementSpeed):
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


class Structure(GameObject):
    def __init__(self, gameWindow, xPos, yPos, width, height):
        super().__init__(gameWindow)
        self.joe = 0

    def move(self, wMoved, aMoved, sMoved, dMoved):
        self.xPos += aMoved + dMoved
        self.yPos += wMoved + sMoved

    def draw(self, graveyard):
        self.gameWindow.blit(graveyard, (self.xPos, self.yPos))




class Hitbox(GameObject):
    def __init__(self, assetNumber, gameWindow, xPos, yPos, width, height):
        super().__init__()
        self.name = assetNumber
        self.gameWindow = gameWindow
        self.xPos = 0
        self.yPos = 0
        self.width = 50
        self.height = 50

    def move(self, wMoved, aMoved, sMoved, dMoved):
        self.xPos += aMoved + dMoved
        self.yPos += wMoved + sMoved

    def draw(self, graveyard):
        self.gameWindow.blit(graveyard, (self.xPos, self.yPos))













