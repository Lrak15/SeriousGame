
# Import libraries
from GameObjects import Structure
from GameObjects import StructureHitBox
from GameObjects import Player
from GameObjects import Enemy
from GameObjects import Projectile
from random import randrange
import math
import pygame
pygame.init()

# Set frames per second
fps = 69
timer = pygame.time.Clock()

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('placeholder title')

# Define center coordinates
centerX, centerY = screenWidth / 2, screenHeight / 2
print(screenWidth)
print(centerX)
print(screenHeight)
print(centerY)

# Define pixel size
px = round(screenHeight / 200)

# Load font
font = pygame.font.Font('freesansbold.ttf', 20)

# Load images
graveyard = pygame.image.load('Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (100 * px, 100 * px))
graveyardRect = graveyard.get_rect()

spillermandhahasej = pygame.image.load('Graphics/PLayer.png')
spiller = pygame.transform.scale(spillermandhahasej, (100, 200))

rygemonster = pygame.image.load('Graphics/Ryge_monster.png')
fjende = pygame.transform.scale(rygemonster, (100, 100))

graveyardStructureTing = Structure(gameWindow, 100, 100, 69, 69, graveyard)

graveyardHitBox1 = StructureHitBox(gameWindow, 100, 100, 100, 100, 'red', px)
graveyardHitBox2 = StructureHitBox(gameWindow, 200, 200, 90, 90, 'red', px)
graveyardHitBox3 = StructureHitBox(gameWindow, 300, 300, 70, 70, 'red', px)
graveyardHitBox4 = StructureHitBox(gameWindow, 400, 400, 40, 40, 'red', px)

graveyardHitBoxes = [graveyardHitBox1, graveyardHitBox2, graveyardHitBox3, graveyardHitBox4]

player_health = 100
player_width = 100
player_heigth = 200

player = Player(gameWindow, centerX, centerY, player_width, player_heigth, spiller)

spawnDelay = 10
attackDelay = 0

willpowerPoints = 0
willpowerLevel = 0

projectiles = []
enemies = []


'''
def check_collisions():
    collision_tolerance = 10
    for hitbox in graveyardHitBoxes:
        if hitbox.colliderect(Player.)
'''


def calculate_movement(movement_speed):
    global w_moved, a_moved, s_moved, d_moved

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_w]:
        w_moved = movement_speed

    if key_pressed[pygame.K_a]:
        a_moved = movement_speed

    if key_pressed[pygame.K_s]:
        s_moved = -movement_speed

    if key_pressed[pygame.K_d]:
        d_moved = -movement_speed

    # The following code checks if a movement in the vertical direction and a movement in the horizontal direction
    # both aren't equal to 0, meaning that there is diagonal movement. If so, both movement directions, making up
    # the diagonal movement, is shortened, so that the diagonal movement speed is the same speed as vertical or
    # horizontal movement
    if w_moved and a_moved != 0:
        w_moved = math.sin(45) * movement_speed
        a_moved = math.sin(45) * movement_speed

    if w_moved and d_moved != 0:
        w_moved = math.sin(45) * movement_speed
        d_moved = -math.sin(45) * movement_speed

    if s_moved and a_moved != 0:
        s_moved = -math.sin(45) * movement_speed
        a_moved = math.sin(45) * movement_speed

    if s_moved and d_moved != 0:
        s_moved = -math.sin(45) * movement_speed
        d_moved = -math.sin(45) * movement_speed


def display_mouse_coordinates():
    mouse_coordinates = font.render(f'coordinates: {mousePosition[0]} ; {mousePosition[1]}', True, 'red')
    gameWindow.blit(mouse_coordinates, (mousePosition[0], mousePosition[1]))


def willpower_bar(points, level, progress):

    points_display = font.render(f'-{points}/{progress}-', True, 'purple')
    level_display = font.render(f'-LEVEL({level})-', True, 'purple')

    pygame.draw.rect(gameWindow, 'black', (100, 650, 1100, 50))
    pygame.draw.rect(gameWindow, 'darkgrey', (110, 660, 1080, 30))
    pygame.draw.rect(gameWindow, 'yellow', (110, 660, (points / progress) * 1080, 30))

    gameWindow.blit(points_display, (115, 666))
    gameWindow.blit(level_display, (1080, 666))


def enemy_attack(monster, player):
    if monster.hitbox.colliderect(player.hitbox):
        player_health = 25
        try:
            enemies.remove(monster)
        except ValueError:
            pass

    # if abs(first.xPos - second.xPos) <= 5 and abs(first.yPos - second.yPos) <= 5:




Customise = True
Running = True
Spawning = True


while Customise:
    timer.tick(fps)

    gameWindow.fill('red')

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:

            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                Customise = False
                Running = False

            elif event.key == pygame.K_SPACE:
                Customise = False

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Customise = False
            Running = False

    # Update game window
    pygame.display.flip()

while Running:
    timer.tick(fps)

    movementSpeed = 4
    w_moved = 0
    a_moved = 0
    s_moved = 0
    d_moved = 0

    projectileSpeed = 10
    enemySpeed = 2

    spawn_x = randrange(screenWidth)
    spawn_y = randrange(screenHeight)
    # make projectilespeed inside clasSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    mousePosition = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]
    rightClick = pygame.mouse.get_pressed()[2]

    gameWindow.fill('grey')

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:

            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                Running = False

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Running = False

    if leftClick:
        if attackDelay <= 0:
            attackDelay = 10
            try:
                angle = (math.atan((mousePosition[1] - centerY) / (mousePosition[0] - centerX)))
            except ZeroDivisionError:
                angle = 1.57079633

            '''
            if mousePosition[0] == centerX:
                angle = 1.57079633
            elif mousePosition[0] == centerX and mousePosition[1] < centerY:
                angle = 4.71238898
            else:
                angle = (math.atan((mousePosition[1] - centerY) / (mousePosition[0] - centerX)))
    
            
            '''
            shot = Projectile(gameWindow, centerX, centerY, 69, 69, 420, projectileSpeed, mousePosition[0], (screenHeight - mousePosition[1]), angle)

            print(f'mouseX({mousePosition[0]}) - centerX({centerX}) = {mousePosition[0] - centerX}')
            print(f'mouseY({screenHeight - mousePosition[1]}) - centerY({centerY}) = {(screenHeight - mousePosition[1]) - centerY}')
            print(f'angle between these is arctan({(screenHeight - mousePosition[1]) - centerY} / {mousePosition[0] - centerX}) = {shot.angle}')
            # print(f'x-direction = {shot.xDirectionzzz} and y-direction = {shot.yDirectionzzz}')
            projectiles.append(shot)

    attackDelay -= 1

    if Spawning:
        if spawnDelay == 0:
            dude = Enemy(gameWindow, spawn_x, spawn_y, 100, 100, 4, enemySpeed, 1, fjende)
            enemies.append(dude)

    spawnDelay -= 1
    if spawnDelay < 0:
        spawnDelay = 10

    calculate_movement(movementSpeed)

    graveyardStructureTing.move(w_moved, a_moved, s_moved, d_moved)
    graveyardStructureTing.draw()

    player.draw()

    for i in graveyardHitBoxes:
        i.move(w_moved, a_moved, s_moved, d_moved)
        i.draw()

    for attack in projectiles:
        for monster in enemies:

            if monster.xPos <= attack.xPos <= monster.xPos + monster.width and monster.yPos <= attack.yPos <= monster.yPos + monster.height:
                monster.health -= 1
                try:
                    projectiles.remove(attack)
                except ValueError:
                    pass

        attack.move(w_moved, a_moved, s_moved, d_moved)
        attack.travel(centerX)
        attack.draw()

    for monster in enemies:
        if monster.health == 0:
            enemies.remove(monster)
            willpowerPoints += 1
        enemy_attack(monster, player)
        monster.move(w_moved, a_moved, s_moved, d_moved)
        monster.travel(centerX, centerY)
        monster.draw()

    display_mouse_coordinates()

    level_progression = 10 + willpowerLevel * 5
    willpower_bar(willpowerPoints, willpowerLevel, level_progression)
    if willpowerPoints >= level_progression:
        willpowerLevel += 1
        willpowerPoints = 0

    # Update game window
    pygame.display.flip()
