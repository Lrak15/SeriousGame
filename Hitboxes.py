import math
import pygame
#  ?????????????????????????????????????????????

class HitboxClass:
    def __init__(self, assetNumber, gameWindow):
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













