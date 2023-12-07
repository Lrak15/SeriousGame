import math
import pygame
from random import randrange


class GameObject:
    def __init__(self, game_window, x_pos, y_pos, width, height):
        self.gameWindow = game_window
        self.xPos = x_pos
        self.yPos = y_pos
        self.width = width
        self.height = height

    def move(self, w_moved, a_moved, s_moved, d_moved):
        # Movement in all directions is added up
        self.xPos += a_moved + d_moved
        self.yPos += w_moved + s_moved


class Structure(GameObject):
    def __init__(self, game_window, x_pos, y_pos, width, height, image):
        super().__init__(game_window, x_pos, y_pos, width, height)
        self.graphics = image

    def draw(self):
        self.gameWindow.blit(self.graphics, (self.xPos, self.yPos))


class StructureHitBox(GameObject):
    def __init__(self, game_window, x_pos, y_pos, width, height, color,
                 border_thickness):
        super().__init__(game_window, x_pos, y_pos, width, height)
        self.color = color
        self.thickness = border_thickness

    def draw(self):
        pygame.draw.rect(self.gameWindow, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height),
                         self.thickness)


class Player():
    def __init__(self, game_window, center_x, center_y, width, height, image):
        self.gameWindow = game_window
        self.xPos = center_x - width / 2
        self.yPos = center_y - height / 2
        self.image = image
        self.hitbox = pygame.Rect(self.xPos, self.yPos, width, height)

    def draw(self):
        self.gameWindow.blit(self.image, self.hitbox)
        pygame.draw.rect(self.gameWindow, 'blue', self.hitbox, 2)

        # blit.shoes
        # blit.shirt
        # blit.pants
        # blit.face and hands
        # blit.hair
        # blit.overShirt
        # blit.hat?


class Enemy(GameObject):
    def __init__(self, game_window, x_pos, y_pos, width, height, damage,
                 speed, health, image):
        super().__init__(game_window, x_pos, y_pos, width, height)
        self.damage = damage
        self.speed = speed
        self.color = (randrange(255), 0, 0)
        self.health = health
        self.image = image
        self.hitbox = self.image.get_rect()

    def travel(self, center_x, center_y):
        angle = math.atan((center_y - self.yPos) / (center_x - self.xPos))

        if self.xPos < center_x:
            self.xPos += math.cos(angle) * self.speed
            self.yPos += math.sin(angle) * self.speed

        elif self.xPos > center_x:
            self.xPos -= math.cos(angle) * self.speed
            self.yPos -= math.sin(angle) * self.speed

        # Updating hitbox
        self.hitbox = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def draw(self):
        # pygame.draw.rect(self.gameWindow, self.color, self.hitbox, 2)
        self.gameWindow.blit(self.image, self.hitbox)
        pygame.draw.rect(self.gameWindow, 'red', self.hitbox, 2)

    def attack(self):
        if self.hitbox.colliderect(self.playerHitbox):
            self


class Projectile(GameObject):
    def __init__(self, game_window, x_pos, y_pos, width, height, damage,
                 speed, mouse_x, mouse_y, angle):
        super().__init__(game_window, x_pos, y_pos, width, height)
        self.damage = damage
        self.speed = speed
        self.color = (255, randrange(150) + 105, 0)
        self.mouseX = mouse_x
        self.mouseY = mouse_y
        self.angle = angle
        # self.hitbox = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def travel(self, center_x):
        if self.mouseX > center_x:
            self.xPos += math.cos(self.angle) * self.speed
            self.yPos += math.sin(self.angle) * self.speed
        else:
            self.xPos -= math.cos(self.angle) * self.speed
            self.yPos -= math.sin(self.angle) * self.speed

            # Updating hitbox
            # self.hitbox = pygame.Rect(self.xPos, self.yPos, self.width, self.height)

    def draw(self):
        # pygame.draw.rect(self.gameWindow, self.color, self.hitbox)

        if self.xPos > -1:

            pygame.draw.circle(self.gameWindow, self.color, (self.xPos, self.yPos), 10)



'''
class test:
    def __init__(self):
        self._hitboxes = []

    def add_hitbox(self, hitbox: HitBox):
        self._hitboxes.append(hitbox)

    def move(self, x, y):
        # move structure
        for hitbox in self._hitboxes:
            hitbox.move(x, y)

thing = test()
test.add_hitbox(HitBox(gameWindow, 100, 100, 100, 100, 'red', px)

thing.move(2, 4);
'''
