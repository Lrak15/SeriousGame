import math
import pygame
from random import randrange


class GameObject:
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height):
        self.gameWindow = game_window
        self.wMoved = 69
        self.aMoved = 69
        self.sMoved = 69
        self.dMoved = 69
        # self.keyPressed = pygame.key.get_pressed()
        self.xPos = x_pos
        self.yPos = y_pos
        self.width = cool_variable_width
        self.height = cool_variable_height

    def move(self, movement_speed):
        self.wMoved = 0
        self.aMoved = 0
        self.sMoved = 0
        self.dMoved = 0
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_w]:
            self.wMoved = movement_speed

        if key_pressed[pygame.K_a]:
            self.aMoved = movement_speed

        if key_pressed[pygame.K_s]:
            self.sMoved = -movement_speed

        if key_pressed[pygame.K_d]:
            self.dMoved = -movement_speed

        # The following code checks if a movement in the vertical direction and a movement in the horizontal direction
        # both aren't equal to 0, meaning that there is diagonal movement. If so, both movement directions, making up
        # the diagonal movement, is shortened, so that the diagonal movement speed is the same speed as vertical or
        # horizontal movement
        if self.wMoved and self.aMoved != 0:
            self.wMoved = math.sin(45) * movement_speed
            self.aMoved = math.sin(45) * movement_speed

        if self.wMoved and self.dMoved != 0:
            self.wMoved = math.sin(45) * movement_speed
            self.dMoved = -math.sin(45) * movement_speed

        if self.sMoved and self.aMoved != 0:
            self.sMoved = -math.sin(45) * movement_speed
            self.aMoved = math.sin(45) * movement_speed

        if self.sMoved and self.dMoved != 0:
            self.sMoved = -math.sin(45) * movement_speed
            self.dMoved = -math.sin(45) * movement_speed

        # Movement in all directions is added up
        self.xPos += self.aMoved + self.dMoved
        self.yPos += self.wMoved + self.sMoved


class Structure(GameObject):
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height, cool_image):
        super().__init__(game_window, x_pos, y_pos, cool_variable_width, cool_variable_height)
        self.graphics = cool_image
        self.hey = 69
        # width and height needed?

    def draw(self):
        self.gameWindow.blit(self.graphics, (self.xPos, self.yPos))



class HitBox(GameObject):
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height, cool_variable_color,
                 cool_border_thickness_variable):
        super().__init__(game_window, x_pos, y_pos, cool_variable_width, cool_variable_height)
        self.color = cool_variable_color
        self.thickness = cool_border_thickness_variable
        # self.player_hitbox = pygame.Rect()


    def draw(self):
        pygame.draw.rect(self.gameWindow, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height),
                         self.thickness)

    '''
    def draw_player_hitbox
        pygame.draw.rect(self.gameWindow, 'blue', self.player_hitbox)
    '''

class Player():
    def __init__(self, game_window, center_x, center_y, width, height):
        self.gameWindow = game_window
        self.xPos = center_x - width / 2
        self.yPos = center_y - height / 2
        self.hitbox = pygame.Rect(self.xPos, self.yPos, width, height)

    def draw(self):
        pygame.draw.rect(self.gameWindow, 'blue', self.hitbox)

        # blit.shoes
        # blit.shirt
        # blit.pants
        # blit.face and hands
        # blit.hair
        # blit.overShirt
        # blit.hat?

class Enemy(GameObject):
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height, enemy_damage,
                 enemy_speed, enemy_health):
        super().__init__(game_window, x_pos, y_pos, cool_variable_width, cool_variable_height)
        self.damage = enemy_damage
        self.speed = enemy_speed
        self.color = (randrange(255), 0, 0)
        self.health = enemy_health
        self.hitbox = pygame.Rect(self.xPos, self.yPos, self.width, self.height)


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
        pygame.draw.rect(self.gameWindow, self.color, self.hitbox)

    def attack(self):
        if self.hitbox.colliderect(self.playerHitbox):
            self




class Projectile(GameObject):
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height, projectile_damage,
                 projectile_speed, mouse_x, mouse_y, cool_variable_angle):
        super().__init__(game_window, x_pos, y_pos, cool_variable_width, cool_variable_height)
        self.damage = projectile_damage
        self.speed = projectile_speed
        self.mouseX = mouse_x
        self.mouseY = mouse_y
        self.angle = cool_variable_angle
        self.color = (randrange(50)+205, randrange(50)+150, 50)
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
