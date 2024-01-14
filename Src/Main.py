
# Import libraries
import math
from random import randrange

import pygame
from pygame import mixer

from GameObjects import Enemy
from GameObjects import Player
from GameObjects import Projectile
from GameObjects import Structure
from GameObjects import StructureHitBox

pygame.init()
mixer.init()

# Set frames per second
fps = 60
timer = pygame.time.Clock()

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('Abstinence')

# Define center coordinates
centerX, centerY = screenWidth / 2, screenHeight / 2
print(screenWidth)
print(centerX)
print(screenHeight)
print(centerY)

# Define pixel size
# Format for new pixel size should be 320:180
px = round(screenHeight / 180)

####################################################################################################################
###   ########         ###         ###      ############         ###         ###   ###   ###         ###         ###
###   ########   ###   ###   ###   ###   ###   #########   #########   ###   ###   ###   ######   ######   #########
###   ########   ###   ###         ###   ###   #########         ###   ###   ###         ######   ######         ###
###   ########   ###   ###   ###   ###   ###   #########   #########   ###   ###         ######   ############   ###
###        ###         ###   ###   ###      ############   #########         ###   ###   ######   ######         ###
####################################################################################################################

# Load fonts

font = pygame.font.Font('Graphics/DS-DIGIB.TTF', 5 * px)
font2 = pygame.font.Font('Graphics/DS-DIGIB.TTF', 10 * px)
font3 = pygame.font.Font('Graphics/LEDLIGHT.otf', 10 * px)
font4 = pygame.font.Font('Graphics/LEDLIGHT.otf', 5 * px)


################################################################################################################################
###   ########         ###         ###      ############         ###         ###   ###   ###   ###   ###      ######         ###
###   ########   ###   ###   ###   ###   ###   #########   #########   ###   ###   ###   ###   ###   ###   ###   ###   #########
###   ########   ###   ###         ###   ###   #########         ###   ###   ###   ###   ###         ###   ###   ###         ###
###   ########   ###   ###   ###   ###   ###   ###############   ###   ###   ###   ###   ###         ###   ###   #########   ###
###        ###         ###   ###   ###      ############         ###         ###         ###   ###   ###      ######         ###
################################################################################################################################

# Load sounds
# Inspiration from:
# https://stackoverflow.com/questions/65247656/how-do-i-change-the-volume-of-the-sound-or-music-in-pygame

shootSound = pygame.mixer.Sound("Sfx/shootsound.mp3")
shootSound.set_volume(0.2)

enemyHitSound = pygame.mixer.Sound("Sfx/killsound.mp3")
enemyHitSound.set_volume(0.1)

killSound = pygame.mixer.Sound("Sfx/killsound2.mp3")
killSound.set_volume(0.1)

playerHitSound = pygame.mixer.Sound('Sfx/playerhitsound.mp3')
playerHitSound.set_volume(0.1)

levelUpSound = pygame.mixer.Sound('Sfx/levelup.mp3')
levelUpSound.set_volume(0.1)

music = 'Sfx/Amynedd Main Theme SMT-2 0.8S.mp3'
pygame.mixer.music.load(music)

# mixer.music.load("")
mixer.music.set_volume(0.2)



################################################################################################################################
###   ########         ###         ###      ############         ###   ###   ###         ###         ###         ###         ###
###   ########   ###   ###   ###   ###   ###   ############   ######         ###   ###   ###   #########   #########   #########
###   ########   ###   ###         ###   ###   ############   ######         ###         ###   #########      ######         ###
###   ########   ###   ###   ###   ###   ###   ############   ######   ###   ###   ###   ###   ###   ###   ###############   ###
###        ###         ###   ###   ###      ############         ###   ###   ###   ###   ###         ###         ###         ###
################################################################################################################################

# Load images

graveyard = pygame.image.load('Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (100 * px, 100 * px))
graveyardRect = graveyard.get_rect()

spiller = pygame.image.load('Graphics/avatar-3.png.png')
spiller = pygame.transform.scale(spiller, (32 * px, 32 * px))

abstinence1_R_L = pygame.image.load('Graphics/Abstinence 1-1.png.png')
abstinence1_R_L = pygame.transform.scale(abstinence1_R_L, (23 * px, 23 * px))
abstinence1 = [abstinence1_R_L, abstinence1_R_L]


abstinence2_R = pygame.image.load('Graphics/Abstinence 2-1.png.png')
abstinence2_R = pygame.transform.scale(abstinence2_R, (52 * px, 26 * px))
abstinence2_L = pygame.transform.flip(abstinence2_R, True, False)
abstinence2 = [abstinence2_R, abstinence2_L]

HUD = pygame.image.load('Graphics/hud-2.png.png')
HUD = pygame.transform.scale(HUD, (screenWidth, screenHeight))

setbackFrame = pygame.image.load('Graphics/setback-1.png.png')
setbackFrame = pygame.transform.scale(setbackFrame, (screenWidth, screenHeight))

Fog1 = pygame.image.load('Graphics/fog-1.png.png')
fog1TopLeft = pygame.transform.scale(Fog1, (screenWidth, screenHeight))
fog1TopRight = pygame.transform.flip(fog1TopLeft, True, False)
fog1BottomLeft = pygame.transform.flip(fog1TopLeft, False, True)
fog1BottomRight = pygame.transform.flip(fog1TopLeft, True, True)

Fog2 = pygame.image.load('Graphics/fog-2.png.png')
fog2TopLeft = pygame.transform.scale(Fog2, (screenWidth, screenHeight))
fog2TopRight = pygame.transform.flip(fog2TopLeft, True, False)
fog2BottomLeft = pygame.transform.flip(fog2TopLeft, False, True)
fog2BottomRight = pygame.transform.flip(fog2TopLeft, True, True)

Fog3 = pygame.image.load('Graphics/fog-3.png.png')
fog3TopLeft = pygame.transform.scale(Fog3, (screenWidth, screenHeight))
fog3TopRight = pygame.transform.flip(fog3TopLeft, True, False)
fog3BottomLeft = pygame.transform.flip(fog3TopLeft, False, True)
fog3BottomRight = pygame.transform.flip(fog3TopLeft, True, True)

fogTopLeft = [fog1TopLeft, fog2TopLeft, fog3TopLeft]
fogTopRight = [fog1TopRight, fog2TopRight, fog3TopRight]
fogBottomLeft = [fog1BottomLeft, fog2BottomLeft, fog3BottomLeft]
fogBottomRight = [fog1BottomRight, fog2BottomRight, fog3BottomRight]

park = pygame.image.load('Graphics/image.png')
park = pygame.transform.scale(park, (250 * px, 200 * px))
park2 = pygame.image.load('Graphics/Park_2.png')
park2 = pygame.transform.scale(park2, (250 * px, 200 * px))
park2 = pygame.transform.flip(park2, True, False)

building = pygame.image.load('Graphics/city structures-1.png.png')
building = pygame.transform.scale(building, (102 * px, 60 * px))


introImages = []
imageCount = 33
for i in range(1, imageCount + 1):
    image = pygame.image.load(f'Graphics/Abstinence title screen-{i}.png.png')
    image = pygame.transform.scale(image, (screenWidth, screenWidth))
    introImages.append(image)

titleScreen = pygame.image.load('Graphics/Abstinence title screen-34.png.png')
titleScreen = pygame.transform.scale(titleScreen, (screenWidth, screenWidth))

titleButton1 = pygame.image.load('Graphics/title buttons-1.png.png')
titleButton1 = pygame.transform.scale(titleButton1, (screenWidth, screenWidth / 24))
titleButton2_1 = pygame.image.load('Graphics/title buttons-2.png.png')
titleButton2_1 = pygame.transform.scale(titleButton2_1, (screenWidth, screenWidth / 24))
titleButton2_2 = pygame.image.load('Graphics/title buttons-3.png.png')
titleButton2_2 = pygame.transform.scale(titleButton2_2, (screenWidth, screenWidth / 24))
titleButton3 = pygame.image.load('Graphics/title buttons-4.png.png')
titleButton3 = pygame.transform.scale(titleButton3, (screenWidth, screenWidth / 24))
titleButton4 = pygame.image.load('Graphics/title buttons-5.png.png')
titleButton4 = pygame.transform.scale(titleButton4, (screenWidth, screenWidth / 24))

primaryProjectile = pygame.image.load('Graphics/Projectiles-1.png.png')
primaryProjectile = pygame.transform.scale(primaryProjectile, (7 * px, 7 * px))

secondaryProjectile = pygame.image.load('Graphics/Projectiles-2.png.png')
secondaryProjectile = pygame.transform.scale(secondaryProjectile, (3 * px, 3 * px))


#######################################################################################
###         ###      ######         ###         ###         ###         ###         ###
###   ###   ###   ###   #########   ###   #########   ############   ######   #########
###   ###   ###      ############   ###      ######   ############   ######         ###
###   ###   ###   ###   #########   ###   #########   ############   ############   ###
###         ###      ######      ######         ###         ######   ######         ###
#######################################################################################


parkStructure = Structure(gameWindow, 10 * px, 135 * px, 69, 69, park)
parkStructure2 = Structure(gameWindow, -238 * px, 142 * px, 69, 69, park2)
parkStructure2_2 = Structure(gameWindow, 258 * px, 135 * px, 69, 69, park2)

buildingStructure = Structure(gameWindow, -170 * px, 50 * px, 69, 69, building)

structures = [parkStructure, parkStructure2, parkStructure2_2, buildingStructure]

graveyardStructureTing = Structure(gameWindow, 80 * px, 40 * px, 69, 69, graveyard)

graveyardHitBox1 = StructureHitBox(gameWindow, 87 * px, 72 * px, 3 * px, 65 * px, 'red', px)
graveyardHitBox2 = StructureHitBox(gameWindow, 169 * px, 72 * px, 3 * px, 65 * px, 'red', px)
graveyardHitBox3 = StructureHitBox(gameWindow, 87 * px, 72 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox4 = StructureHitBox(gameWindow, 137 * px, 72 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox5 = StructureHitBox(gameWindow, 87 * px, 134 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox6 = StructureHitBox(gameWindow, 137 * px, 134 * px, 35 * px, 3 * px, 'red', px)
benchHitbox1 = StructureHitBox(gameWindow, -206 * px, 167 * px, 26 * px, 3 * px, 'blue', px)
benchHitbox2 = StructureHitBox(gameWindow, -128 * px, 165 * px, 26 * px, 3 * px, 'blue', px)
benchHitbox3 = StructureHitBox(gameWindow, -40 * px, 165 * px, 26 * px, 3 * px, 'blue', px)
benchHitbox4 = StructureHitBox(gameWindow, 290 * px, 160 * px, 26 * px, 3 * px, 'blue', px)
benchHitbox5 = StructureHitBox(gameWindow, 368 * px, 158 * px, 26 * px, 3 * px, 'blue', px)
benchHitbox6 = StructureHitBox(gameWindow, 456 * px, 158 * px, 26 * px, 3 * px, 'blue', px)
buildingHitbox1 = StructureHitBox(gameWindow, -169 * px, 50 * px, 100 * px, 51 * px, 'blue', px)
borderHitbox1 = StructureHitBox(gameWindow, -437 * px, -200 * px, 1100 * px, 200 * px, 'black', 100 * px)
borderHitbox2 = StructureHitBox(gameWindow, -437 * px, -200 * px, 200 * px, 500 * px, 'black', 100 * px)
borderHitbox3 = StructureHitBox(gameWindow, 507 * px, -200 * px, 200 * px, 1000 * px, 'black', 100 * px)
borderHitbox4 = StructureHitBox(gameWindow, -437 * px, 335 * px, 1000 * px, 200 * px, 'black', 100 * px)

structureHitboxes = [graveyardHitBox1, graveyardHitBox2, graveyardHitBox3, graveyardHitBox4, graveyardHitBox5, graveyardHitBox6, benchHitbox1, benchHitbox2, benchHitbox3, benchHitbox4, benchHitbox5, benchHitbox6, buildingHitbox1, borderHitbox1, borderHitbox2, borderHitbox3, borderHitbox4]
borderHitboxes = [borderHitbox1, borderHitbox2, borderHitbox3, borderHitbox4]

###############################################################################################################
###   ###   ###         ###      ######         ###         ###      ######   #########         ###         ###
###   ###   ###   ###   ###   ###   ######   ######   ###   ###   ###   ###   #########   #########   #########
###   ###   ###         ###      #########   ######         ###      ######   #########      ######         ###
###   ###   ###   ###   ###   ############   ######   ###   ###   ###   ###   #########   ###############   ###
######   ######   ###   ###   ###   ###         ###   ###   ###      ######         ###         ###         ###
###############################################################################################################

player_health = 100
player_width = 10 * px
player_heigth = 24 * px

player = Player(gameWindow, centerX, centerY, player_width, player_heigth, spiller)

spawn_x = 0
spawn_y = 0

spawnDelay = 0
attackDelay = 0
graphicsDelay = 0

willpowerPoints = 0
willpowerLevel = 0

temptationPoints = 0

upgradePoints = 5

attackSpeedUpgrades = 0
movementSpeedUpgrades = 0
resistanceUpgrades = 0
projectileUpgrades = 0

projectiles = []
enemies = []

Spawning = False

setbackTime = None

Regenerating = False

temptationTime = None


###############################################################################################################
###         ###   ###   ###   ###   ###         ###         ###         ###         ###   ###   ###         ###
###   #########   ###   ###   ###   ###   ############   #########   ######   ###   ###   ###   ###   #########
###      ######   ###   ###         ###   ############   #########   ######   ###   ###         ###         ###
###   #########   ###   ###         ###   ############   #########   ######   ###   ###         #########   ###
###   #########         ###   ###   ###         ######   ######         ###         ###   ###   ###         ###
###############################################################################################################


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
    mouse_coordinates = font.render(f'coordinates: {mousePosition[0]} ; {mousePosition[1]} {len(enemies)}', True, 'red')
    gameWindow.blit(mouse_coordinates, (mousePosition[0], mousePosition[1]))


def willpower_bar(points, level, progress):
    points_display = font.render(f'{points}/{progress}', True, 'purple')
    level_display = font.render(f'LEVEL {level}', True, 'purple')

    pygame.draw.rect(gameWindow, 'yellow', (40 * px, 172 * px, (points / progress) * 240 * px, 5 * px))

    gameWindow.blit(points_display, (41 * px, 172 * px))
    gameWindow.blit(level_display, (262 * px, 172 * px))


def temptation_graphics(points):
    global graphicsDelay

    try:
        pygame.draw.rect(gameWindow, (205 + 0.5 * points, 180 - 1.8 * points, 0), (261 * px, 3 * px, (points / 100) * 50 * px, 5 * px))
    except ValueError:
        pygame.draw.rect(gameWindow, (255, 0, 0), (261 * px, 3 * px, 50 * px, 5 * px))


    points_display = font.render(f'{math.floor(points)}', True, (29, 29, 29))
    gameWindow.blit(points_display, (262 * px, 3 * px))

    if graphicsDelay <= 0:
        try:
            pygame.draw.rect(gameWindow, (255 / 100 * points, 0, 0), (314 * px, 5 * px, 1 * px, 1 * px))
            pygame.draw.rect(gameWindow, (255 / 100 * points, 0, 0), (316 * px, 5 * px, 1 * px, 1 * px))
        except ValueError:
            pygame.draw.rect(gameWindow, (255, 0, 0), (314 * px, 5 * px, 1 * px, 1 * px))
            pygame.draw.rect(gameWindow, (255, 0, 0), (316 * px, 5 * px, 1 * px, 1 * px))

    if graphicsDelay <= -101 + points:
        graphicsDelay = 101 - points


def HUD_graphics(upgradePoints):
    upgrade_title_1 = font.render(f'Willpower', True, ('green'))
    upgrade_title_2 = font.render(f'Points: {upgradePoints}', True, ('green'))

    gameWindow.blit(upgrade_title_1, (4 * px, 140 * px))
    gameWindow.blit(upgrade_title_2, (4 * px, 144 * px))

    upgrade_text_1 = font.render(f'1: att speed', True, ('green'))
    upgrade_text_2 = font.render(f'2: mov speed', True, ('green'))
    upgrade_text_3 = font.render(f'3: resistance', True, ('green'))
    upgrade_text_4 = font.render(f'4: projectiles', True, ('green'))

    gameWindow.blit(upgrade_text_1, (4 * px, 154 * px))
    gameWindow.blit(upgrade_text_2, (4 * px, 160 * px))
    gameWindow.blit(upgrade_text_3, (4 * px, 166 * px))
    gameWindow.blit(upgrade_text_4, (4 * px, 172 * px))


def fog(points):
    global fogTopLeft, fogTopRight, fogBottomLeft, fogBottomRight

    gameWindow.blit(fogTopLeft[randrange(0, 3)], (-120 * px + 1.2 * points * px, -90 * px + 0.9 * points * px))
    gameWindow.blit(fogTopRight[randrange(0, 3)], (120 * px - 1.2 * points * px, -90 * px + 0.9 * points * px))
    gameWindow.blit(fogBottomLeft[randrange(0, 3)], (-120 * px + 1.2 * points * px, 90 * px - 0.9 * points * px))
    gameWindow.blit(fogBottomRight[randrange(0, 3)], (120 * px - 1.2 * points * px, 90 * px - 0.9 * points * px))


def check_collisions(structure, player):
    global w_moved, a_moved, s_moved, d_moved
    collision_tolerance = 10 * px
    if structure.hitbox.colliderect(player.hitbox):
        print('collision')
        if abs(player.hitbox.top - structure.hitbox.bottom) < collision_tolerance:
            w_moved = 0
        if abs(player.hitbox.left - structure.hitbox.right) < collision_tolerance:
            a_moved = 0
        if abs(player.hitbox.bottom - structure.hitbox.top) < collision_tolerance:
            s_moved = 0
        if abs(player.hitbox.right - structure.hitbox.left) < collision_tolerance:
            d_moved = 0


def spawn_enemy():
    global spawn_x, spawn_y
    Spawning = False
    enemyType = randrange(0, 100)
    while not Spawning:
        spawn_x = randrange(screenWidth * 3) - screenWidth
        spawn_y = randrange(screenHeight * 3) - screenHeight
        if spawn_x < - 20 * px or spawn_x > screenWidth + 20 * px or spawn_y < - 20 * px or spawn_y > screenWidth + 20 * px:
            Spawning = True

    if enemyType < 100 - 10 * willpowerLevel:
        monster = Enemy(gameWindow, spawn_x, spawn_y, 23 * px, 23 * px, 7, 1 * px, 1 + willpowerLevel, abstinence1)
    else:
        monster = Enemy(gameWindow, spawn_x, spawn_y, 52 * px, 26 * px, 15, 2 * px, 3 * (1 + willpowerLevel), abstinence2)
    enemies.append(monster)


def despawn_enemy(monster):
    if monster.xPos < - screenWidth or monster.xPos > 2 * screenWidth or monster.yPos < - screenHeight or monster.yPos > screenHeight * 2:
        try:
            enemies.remove(monster)
        except ValueError:
            pass

def despawn_projectile(attack):
    if attack.xPos < - screenWidth or attack.xPos > 2 * screenWidth or attack.yPos < - screenHeight or attack.yPos > screenHeight * 2:
        try:
            projectiles.remove(attack)
        except ValueError:
            pass

def enemy_attack(monster, player):
    global temptationPoints, Regenerating, temptationTime
    if monster.hitbox.colliderect(player.hitbox):
        try:
            enemies.remove(monster)
            temptationPoints += monster.damage * (1 - resistanceUpgrades / 15)
            Regenerating = False
            temptationTime = pygame.time.get_ticks()
            pygame.mixer.Sound.play(playerHitSound)
        except ValueError:
            pass

    # if abs(first.xPos - second.xPos) <= 5 and abs(first.yPos - second.yPos) <= 5:

def player_attack(attack, monster):
    if attack.hitbox.colliderect(monster.hitbox):
        monster.health -= attack.damage
        attack.pierce -= 1
        pygame.mixer.Sound.play(enemyHitSound)



TitleScreen = True
Running = True
Setback = False


for count in range(33):
    timer.tick(15)
    gameWindow.blit(introImages[count], (0, 0))
    # Update game window
    pygame.display.flip()

while TitleScreen:
    timer.tick(fps)

    Customize_character = False
    Options = False

    gameWindow.blit(titleScreen, (0, 0))

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:

            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                TitleScreen = False
                # Running = False ##########################################################################

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            TitleScreen = False
            Running = False

    mousePosition = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]

    if 137 * px < mousePosition[0] < 184 * px and 82.4 * px < mousePosition[1] < 89.5 * px:
        gameWindow.blit(titleButton1, (0, 81.4 * px))
        if leftClick:
            TitleScreen = False

    if 137 * px < mousePosition[0] < 184 * px and 98.4 * px < mousePosition[1] < 113.5 * px:
        gameWindow.blit(titleButton2_1, (0, 97.4 * px))
        gameWindow.blit(titleButton2_2, (0, 105.4 * px))
        if leftClick:
            Customize_character = True

    if 137 * px < mousePosition[0] < 184 * px and 122.4 * px < mousePosition[1] < 129.5 * px:
        gameWindow.blit(titleButton3, (0, 121.4 * px))
        if leftClick:
            Options = True

    if 137 * px < mousePosition[0] < 184 * px and 138.4 * px < mousePosition[1] < 145.5 * px:
        gameWindow.blit(titleButton4, (0, 137.4 * px))
        if leftClick:
            TitleScreen = False
            Running = False

    while Customize_character:
        timer.tick(fps)

        gameWindow.fill('red')

        # Check for pygame events
        for event in pygame.event.get():

            # Check for keys pressed
            if event.type == pygame.KEYDOWN:

                # Close game if escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    Customize_character = False
                    Running = False

                elif event.key == pygame.K_SPACE:
                    Customize_character = False

            # Close game if the game windows close button is pressed
            elif event.type == pygame.QUIT:
                Customize_character = False
                Running = False

        # Update game window
        pygame.display.flip()





    # Update game window
    pygame.display.flip()

# Playing music that repeats 69 times
# Inspiration from:
# https://stackoverflow.com/questions/35068209/how-do-i-repeat-music-using-pygame-mixer
pygame.mixer.music.play(69)

while Running:
    timer.tick(fps)

    movementSpeed = (1 + movementSpeedUpgrades) * px
    w_moved = 0
    a_moved = 0
    s_moved = 0
    d_moved = 0

    projectileSpeed = 6 * px + willpowerLevel

    # make projectilespeed inside clasSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    mousePosition = pygame.mouse.get_pos()
    leftClick = pygame.mouse.get_pressed()[0]
    rightClick = pygame.mouse.get_pressed()[2]

    gameWindow.fill('darkgrey')

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:
            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                Running = False

        # Check for keys let go of
        # Inspiration from:
        # https: // stackoverflow.com / questions / 58600062 / how - to - use - keyup - in -pygame
        elif event.type == pygame.KEYUP:
            # Upgrade attack speed if key 1 is let go of
            if event.key == pygame.K_1 and upgradePoints >= 1:
                attackSpeedUpgrades += 1
                upgradePoints -= 1
            # Upgrade movement speed if key 2 is let go of
            elif event.key == pygame.K_2 and upgradePoints >= 1:
                movementSpeedUpgrades += 1
                upgradePoints -= 1
            # Upgrade resistance if key 3 is let go of
            elif event.key == pygame.K_3 and upgradePoints >= 1:
                resistanceUpgrades += 1
                upgradePoints -= 1
            # Upgrade projectile count if key 4 is let go of
            elif event.key == pygame.K_4 and upgradePoints >= 2:
                projectileUpgrades += 1
                upgradePoints -= 2

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Running = False

    if leftClick:
        if attackDelay <= 0:
            attackDelay = 10 - attackSpeedUpgrades
            try:
                angle = (math.atan((mousePosition[1] - centerY) / (mousePosition[0] - centerX)))
            except ZeroDivisionError:
                angle = 1.57079633

            shot = Projectile(gameWindow, centerX, centerY, 69, 69, 3, projectileSpeed, mousePosition[0], (screenHeight - mousePosition[1]), angle, primaryProjectile)
            projectiles.append(shot)

            if projectileUpgrades > 0:
                for count in range(1, projectileUpgrades + 1):
                    print(count)
                    RightOffshoot = Projectile(gameWindow, centerX, centerY, 69, 69, 1, projectileSpeed, mousePosition[0], (screenHeight - mousePosition[1]), angle + 0.1 * count, secondaryProjectile)
                    projectiles.append(RightOffshoot)
                    LeftOffshoot = Projectile(gameWindow, centerX, centerY, 69, 69, 1, projectileSpeed, mousePosition[0], (screenHeight - mousePosition[1]), angle - 0.1 * count, secondaryProjectile)
                    projectiles.append(LeftOffshoot)

            pygame.mixer.Sound.play(shootSound)

    attackDelay -= 1

    if spawnDelay == 0:
        spawn_enemy()
    spawnDelay -= 1
    if spawnDelay < 0:
        spawnDelay = 15 - willpowerLevel

    calculate_movement(movementSpeed)

    for structure in structureHitboxes:
        check_collisions(structure, player)

    graveyardStructureTing.move(w_moved, a_moved, s_moved, d_moved)
    graveyardStructureTing.draw()

    for image in structures:
        image.move(w_moved, a_moved, s_moved, d_moved)
        image.draw()

    for structure in structureHitboxes:
        structure.move(w_moved, a_moved, s_moved, d_moved)
        structure.update()

    for border in borderHitboxes:
        border.draw()

    player.draw(px)

    for attack in projectiles:
        for monster in enemies:

            player_attack(attack, monster)

            '''
            if monster.xPos <= attack.xPos <= monster.xPos + monster.width and monster.yPos <= attack.yPos <= monster.yPos + monster.height:

                try:
                    monster.health -= 1
                    attack.pierce -= 1
                    pygame.mixer.Sound.play(enemyHitSound)

                except ValueError:
                    pass
            '''
        if attack.pierce == 0:
            projectiles.remove(attack)
        attack.move(w_moved, a_moved, s_moved, d_moved)
        attack.travel(centerX)
        despawn_projectile(attack)
        attack.draw()

    for monster in enemies:
        if monster.health <= 0:
            enemies.remove(monster)
            willpowerPoints += 1
            pygame.mixer.Sound.play(killSound)
        enemy_attack(monster, player)
        monster.move(w_moved, a_moved, s_moved, d_moved)
        monster.travel(centerX, centerY)
        despawn_enemy(monster)
        monster.draw(centerX, px)

    # fog(temptationPoints)

    # display_mouse_coordinates()

    gameWindow.blit(HUD, (0, 0))

    level_progression = 10 + willpowerLevel * 5
    willpower_bar(willpowerPoints, willpowerLevel, level_progression)
    if willpowerPoints >= level_progression:
        willpowerLevel += 1
        upgradePoints += 1
        willpowerPoints = 0
        pygame.mixer.Sound.play(levelUpSound)

    temptation_graphics(temptationPoints)

    HUD_graphics(upgradePoints)

    if temptationPoints >= 100:

        enemies.clear()

        setbackTime = pygame.time.get_ticks()
        Setback = True

        while Setback:

            # Check for pygame events
            for event in pygame.event.get():

                # Check for keys pressed
                if event.type == pygame.KEYDOWN:

                    # Close game if escape key is pressed
                    if event.key == pygame.K_ESCAPE:
                        Setback = False
                        Running = False

                    elif event.key == pygame.K_SPACE:
                        Setback = False

                # Close game if the game windows close button is pressed
                elif event.type == pygame.QUIT:
                    Setback = False
                    Running = False

            gameWindow.blit(setbackFrame, (0, 0))
            timeSinceSetback = pygame.time.get_ticks() - setbackTime
            setbackText3 = font4.render('get smoked', True, 'black')
            setbackText = font3.render('get smoked', True, 'red')
            setbackText2 = font3.render('time', True, 'black')
            setbackTimer = font2.render(f'{10000 - timeSinceSetback}', True, 'red')
            gameWindow.blit(setbackText3, (118 * px, 75 * px))
            gameWindow.blit(setbackText, (120 * px, 75 * px))
            gameWindow.blit(setbackText2, (120 * px, 95 * px))
            gameWindow.blit(setbackTimer, (125 * px, 100 * px))

            if timeSinceSetback >= 10000:
                Setback = False

            # Update game window
            pygame.display.flip()

        temptationPoints = 0
        willpowerPoints = 0
        willpowerLevel -= 3
        if willpowerLevel < 0:
            willpowerLevel = 0

    if temptationPoints > 0:
        timeSinceTemptation = pygame.time.get_ticks() - temptationTime
        if timeSinceTemptation > 10000:
            Regenerating = True

    if Regenerating:
        regenParameter = timeSinceTemptation / 1000 - 10
        temptationPoints -= (regenParameter * regenParameter) / 50
        print((regenParameter * regenParameter) / 50)



    if temptationPoints < 0:
        Regenerating = False
        temptationPoints = 0


    graphicsDelay -= 1

    # Update game window
    pygame.display.flip()
