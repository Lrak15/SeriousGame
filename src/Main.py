
# Import libraries
from GameObjects import GameObject
from GameObjects import Structure
from GameObjects import HitBox
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

calculatorForGameobjects = GameObject(gameWindow, 69, 69, 69, 69)

graveyardStructureTing = Structure(gameWindow, 100, 100, 69, 69, graveyard)

graveyardHitBox1 = HitBox(gameWindow, 100, 100, 100, 100, 'red', px)
graveyardHitBox2 = HitBox(gameWindow, 200, 200, 90, 90, 'red', px)
graveyardHitBox3 = HitBox(gameWindow, 300, 300, 70, 70, 'red', px)
graveyardHitBox4 = HitBox(gameWindow, 400, 400, 40, 40, 'red', px)

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


def display_mouse_coordinates():
    mouse_coordinates = font.render(f'coordinates: {mousePosition[0]} ; {mousePosition[1]}', True, 'red')
    gameWindow.blit(mouse_coordinates, (mousePosition[0], mousePosition[1]))


def willpower_bar(points, level):

    level_progression = 10 + willpowerLevel * 5

    points_display = font.render(f'{points}/{level_progression}', True, 'purple')
    level_display = font.render(f'-LEVEL({level})-', True, 'purple')

    pygame.draw.rect(gameWindow, 'black', (100, 650, 1100, 50))
    pygame.draw.rect(gameWindow, 'darkgrey', (110, 660, 1080, 30))
    pygame.draw.rect(gameWindow, 'yellow', (110, 660, (points / level_progression) * 1080, 30))

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

    graveyardStructureTing.move(movementSpeed)
    graveyardStructureTing.draw()

    player.draw()

    for i in graveyardHitBoxes:
        i.move(movementSpeed)
        i.draw()

    for attack in projectiles:
        for monster in enemies:

            if monster.xPos <= attack.xPos <= monster.xPos + monster.width and monster.yPos <= attack.yPos <= monster.yPos + monster.height:
                monster.health -= 1
                try:
                    projectiles.remove(attack)
                except ValueError:
                    pass


        attack.move(movementSpeed)
        attack.travel(centerX)
        attack.draw()

    for monster in enemies:
        if monster.health == 0:
            enemies.remove(monster)
            willpowerPoints += 1
        enemy_attack(monster, player)
        monster.move(movementSpeed)
        monster.travel(centerX, centerY)
        monster.draw()

    display_mouse_coordinates()

    willpower_bar(willpowerPoints, willpowerLevel)

    if willpowerPoints >= 10 + willpowerLevel * 2:
        willpowerLevel += 1
        willpowerPoints = 0

    # Update game window
    pygame.display.flip()
