import math
import pygame


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

    def draw(self):
        pygame.draw.rect(self.gameWindow, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height),
                         self.thickness)

# class Player('???'):
class Player():
    def __init__(self):
        pass

    def draw(self):
        pass
        # blit.shoes
        # blit.shirt
        # blit.pants
        # blit.face and hands
        # blit.hair
        # blit.overShirt
        # blit.hat?


class Projectile(GameObject):
    def __init__(self, game_window, x_pos, y_pos, cool_variable_width, cool_variable_height, projectile_damage,
                 projectile_speed, mouse_x, mouse_y):
        super().__init__(game_window, x_pos, y_pos, cool_variable_width, cool_variable_height)
        self.damage = projectile_damage
        self.speed = projectile_speed
        self.mouseX = mouse_x
        self.mouseY = mouse_y
        self.angle = math.atan((self.mouseY - self.yPos)/(self.mouseX - self.xPos))
        # self.xDirectionzzz = self.xPos + math.cos(self.angle) * self.speed
        # self.yDirectionzzz = self.yPos + math.sin(self.angle) * self.speed

    def travel(self, center_x):
        if self.mouseX < center_x:
            self.xPos -= math.cos(self.angle) * self.speed
            self.yPos += math.sin(self.angle) * self.speed
        elif self.mouseX > center_x:
            self.xPos += math.cos(self.angle) * self.speed
            self.yPos -= math.sin(self.angle) * self.speed

    def draw(self):
        if self.xPos > -1:

            pygame.draw.circle(self.gameWindow, 'yellow', (self.xPos, self.yPos), 10)
            # pygame.draw.circle(self.gameWindow, 'white', (-1, 310), 10)
            pygame.draw.circle(self.gameWindow, 'white', (0, 300), 10)

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
