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
