
# Import libraries
from GameObjects import Structure
from GameObjects import StructureHitBox
from GameObjects import Player
from GameObjects import Enemy
from GameObjects import Projectile
from random import randrange
import math
import pygame
from pygame import mixer
pygame.init()
mixer.init()

# Set frames per second
fps = 10
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
font = pygame.font.Font('Graphics/DS-DIGIB.TTF', 20)
font2 = pygame.font.Font('Graphics/DS-DIGIB.TTF', 50)
font3 = pygame.font.Font('Graphics/LEDLIGHT.otf', 50)
font4 = pygame.font.Font('Graphics/LEDLIGHT.otf', 52)
font5 = pygame.font.Font('Graphics/LEDLIGHT.otf', 20)

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

# mixer.music.load("")
mixer.music.set_volume(0.7)


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

HUD = pygame.image.load('Graphics/New Piskel-2.png (1).png')
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
parkRect = park.get_rect()

intro1 = pygame.image.load('Graphics/Abstinence title screen-1.png.png')
intro1 = pygame.transform.scale(intro1, (screenWidth, screenWidth))
intro2 = pygame.image.load('Graphics/Abstinence title screen-2.png.png')
intro2 = pygame.transform.scale(intro2, (screenWidth, screenWidth))
intro3 = pygame.image.load('Graphics/Abstinence title screen-3.png.png')
intro3 = pygame.transform.scale(intro3, (screenWidth, screenWidth))
intro4 = pygame.image.load('Graphics/Abstinence title screen-4.png.png')
intro4 = pygame.transform.scale(intro4, (screenWidth, screenWidth))
intro5 = pygame.image.load('Graphics/Abstinence title screen-5.png.png')
intro5 = pygame.transform.scale(intro5, (screenWidth, screenWidth))
intro6 = pygame.image.load('Graphics/Abstinence title screen-6.png.png')
intro6 = pygame.transform.scale(intro6, (screenWidth, screenWidth))
intro7 = pygame.image.load('Graphics/Abstinence title screen-7.png.png')
intro7 = pygame.transform.scale(intro7, (screenWidth, screenWidth))
intro8 = pygame.image.load('Graphics/Abstinence title screen-8.png.png')
intro8 = pygame.transform.scale(intro8, (screenWidth, screenWidth))
intro9 = pygame.image.load('Graphics/Abstinence title screen-9.png.png')
intro9 = pygame.transform.scale(intro9, (screenWidth, screenWidth))
intro10 = pygame.image.load('Graphics/Abstinence title screen-10.png.png')
intro10 = pygame.transform.scale(intro10, (screenWidth, screenWidth))
intro11 = pygame.image.load('Graphics/Abstinence title screen-11.png.png')
intro11 = pygame.transform.scale(intro11, (screenWidth, screenWidth))
intro12 = pygame.image.load('Graphics/Abstinence title screen-12.png.png')
intro12 = pygame.transform.scale(intro12, (screenWidth, screenWidth))
intro13 = pygame.image.load('Graphics/Abstinence title screen-13.png.png')
intro13 = pygame.transform.scale(intro13, (screenWidth, screenWidth))
intro14 = pygame.image.load('Graphics/Abstinence title screen-14.png.png')
intro14 = pygame.transform.scale(intro14, (screenWidth, screenWidth))
intro15 = pygame.image.load('Graphics/Abstinence title screen-15.png.png')
intro15 = pygame.transform.scale(intro15, (screenWidth, screenWidth))
intro16 = pygame.image.load('Graphics/Abstinence title screen-16.png.png')
intro16 = pygame.transform.scale(intro16, (screenWidth, screenWidth))
intro17 = pygame.image.load('Graphics/Abstinence title screen-17.png.png')
intro17 = pygame.transform.scale(intro17, (screenWidth, screenWidth))
intro18 = pygame.image.load('Graphics/Abstinence title screen-18.png.png')
intro18 = pygame.transform.scale(intro18, (screenWidth, screenWidth))
intro19 = pygame.image.load('Graphics/Abstinence title screen-19.png.png')
intro19 = pygame.transform.scale(intro19, (screenWidth, screenWidth))
intro20 = pygame.image.load('Graphics/Abstinence title screen-20.png.png')
intro20 = pygame.transform.scale(intro20, (screenWidth, screenWidth))
intro21 = pygame.image.load('Graphics/Abstinence title screen-21.png.png')
intro21 = pygame.transform.scale(intro21, (screenWidth, screenWidth))
intro22 = pygame.image.load('Graphics/Abstinence title screen-22.png.png')
intro22 = pygame.transform.scale(intro22, (screenWidth, screenWidth))
intro23 = pygame.image.load('Graphics/Abstinence title screen-23.png.png')
intro23 = pygame.transform.scale(intro23, (screenWidth, screenWidth))
intro24 = pygame.image.load('Graphics/Abstinence title screen-24.png.png')
intro24 = pygame.transform.scale(intro24, (screenWidth, screenWidth))
intro25 = pygame.image.load('Graphics/Abstinence title screen-25.png.png')
intro25 = pygame.transform.scale(intro25, (screenWidth, screenWidth))
intro26 = pygame.image.load('Graphics/Abstinence title screen-26.png.png')
intro26 = pygame.transform.scale(intro26, (screenWidth, screenWidth))
intro27 = pygame.image.load('Graphics/Abstinence title screen-27.png.png')
intro27 = pygame.transform.scale(intro27, (screenWidth, screenWidth))
intro28 = pygame.image.load('Graphics/Abstinence title screen-28.png.png')
intro28 = pygame.transform.scale(intro28, (screenWidth, screenWidth))
intro29 = pygame.image.load('Graphics/Abstinence title screen-29.png.png')
intro29 = pygame.transform.scale(intro29, (screenWidth, screenWidth))
intro30 = pygame.image.load('Graphics/Abstinence title screen-30.png.png')
intro30 = pygame.transform.scale(intro30, (screenWidth, screenWidth))
intro31 = pygame.image.load('Graphics/Abstinence title screen-31.png.png')
intro31 = pygame.transform.scale(intro31, (screenWidth, screenWidth))
intro32 = pygame.image.load('Graphics/Abstinence title screen-32.png.png')
intro32 = pygame.transform.scale(intro32, (screenWidth, screenWidth))
intro33 = pygame.image.load('Graphics/Abstinence title screen-33.png.png')
intro33 = pygame.transform.scale(intro33, (screenWidth, screenWidth))

intro = [intro1, intro2, intro3, intro4, intro5, intro6, intro7, intro8, intro9, intro10, intro11, intro12, intro13, intro14, intro15, intro16, intro17, intro18, intro19, intro20, intro21, intro22, intro23, intro24, intro25, intro26, intro27, intro28, intro29, intro30, intro31, intro32, intro33]

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


#######################################################################################
###         ###      ######         ###         ###         ###         ###         ###
###   ###   ###   ###   #########   ###   #########   ############   ######   #########
###   ###   ###      ############   ###      ######   ############   ######         ###
###   ###   ###   ###   #########   ###   #########   ############   ############   ###
###         ###      ######      ######         ###         ######   ######         ###
#######################################################################################


parkStructure = Structure(gameWindow, 250 * px, 70 * px, 69, 69, park)

graveyardStructureTing = Structure(gameWindow, 80 * px, 40 * px, 69, 69, graveyard)

graveyardHitBox1 = StructureHitBox(gameWindow, 87 * px, 72 * px, 3 * px, 65 * px, 'red', px)
graveyardHitBox2 = StructureHitBox(gameWindow, 169 * px, 72 * px, 3 * px, 65 * px, 'red', px)
graveyardHitBox3 = StructureHitBox(gameWindow, 87 * px, 72 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox4 = StructureHitBox(gameWindow, 137 * px, 72 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox5 = StructureHitBox(gameWindow, 87 * px, 134 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox6 = StructureHitBox(gameWindow, 137 * px, 134 * px, 35 * px, 3 * px, 'red', px)
graveyardHitBox7 = StructureHitBox(gameWindow, 0 * px, 0 * px, 320 * px, 180 * px, 'red', px)


graveyardHitBoxes = [graveyardHitBox1, graveyardHitBox2, graveyardHitBox3, graveyardHitBox4, graveyardHitBox5, graveyardHitBox6, graveyardHitBox7]

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

spawnDelay = 10
attackDelay = 0
graphicsDelay = 0


willpowerPoints = 0
willpowerLevel = 0

temptationPoints = 0

projectiles = []
enemies = []

startTime = None


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
    mouse_coordinates = font.render(f'coordinates: {mousePosition[0]} ; {mousePosition[1]}', True, 'red')
    gameWindow.blit(mouse_coordinates, (mousePosition[0], mousePosition[1]))


def willpower_bar(points, level, progress):
    points_display = font.render(f'{points}/{progress}', True, 'purple')
    level_display = font.render(f'LEVEL {level}', True, 'purple')

    pygame.draw.rect(gameWindow, 'yellow', (40 * px, 172 * px, (points / progress) * 240 * px, 5 * px))

    gameWindow.blit(points_display, (41 * px, 172.2 * px))
    gameWindow.blit(level_display, (262 * px, 172.2 * px))


def temptation_graphics(points):
    global graphicsDelay

    try:
        pygame.draw.rect(gameWindow, (205 + 0.5 * points, 180 - 1.8 * points, 0), (261 * px, 3 * px, (points / 100) * 50 * px, 5 * px))
        temptation_title = font5.render(f'Temptation', True, (205 + 0.5 * points, 180 - 1.8 * points, 0))
        gameWindow.blit(temptation_title, (262 * px, 8 * px))
    except ValueError:
        pygame.draw.rect(gameWindow, (255, 0, 0), (261 * px, 3 * px, 50 * px, 5 * px))
        temptation_title = font5.render(f'Temptation', True, (255, 0, 0))
        gameWindow.blit(temptation_title, (262 * px, 8 * px))

    points_display = font.render(f'{points}', True, (29, 29, 29))
    gameWindow.blit(points_display, (262 * px, 3.2 * px))

    if graphicsDelay <= 0:
        try:
            pygame.draw.rect(gameWindow, (255 / 100 * points, 0, 0), (314 * px, 5 * px, 1 * px, 1 * px))
            pygame.draw.rect(gameWindow, (255 / 100 * points, 0, 0), (316 * px, 5 * px, 1 * px, 1 * px))
        except ValueError:
            pygame.draw.rect(gameWindow, (255, 0, 0), (314 * px, 5 * px, 1 * px, 1 * px))
            pygame.draw.rect(gameWindow, (255, 0, 0), (316 * px, 5 * px, 1 * px, 1 * px))

    if graphicsDelay <= -105 + points:
        graphicsDelay = 105 - points


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



def enemy_attack(monster, player):
    global temptationPoints
    if monster.hitbox.colliderect(player.hitbox):
        try:
            enemies.remove(monster)
            temptationPoints += monster.damage
            pygame.mixer.Sound.play(playerHitSound)
        except ValueError:
            pass

    # if abs(first.xPos - second.xPos) <= 5 and abs(first.yPos - second.yPos) <= 5:


TitleScreen = True
Running = True
Spawning = True
Setback = False


for count in range(33):
    timer.tick(fps)
    gameWindow.blit(intro[count], (0, 0))
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



while Running:
    timer.tick(fps)

    movementSpeed = (2 + willpowerLevel) * px
    w_moved = 0
    a_moved = 0
    s_moved = 0
    d_moved = 0

    projectileSpeed = 6 * px

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
            attackDelay = 5
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

            pygame.mixer.Sound.play(shootSound)

    attackDelay -= 1

    if Spawning:
        if spawnDelay == 0:
            enemyType = randrange(0, 100)
            if enemyType < 66:
                monster = Enemy(gameWindow, spawn_x, spawn_y, 23 * px, 23 * px, 7, 1 * px, 2, abstinence1)
            else:
                monster = Enemy(gameWindow, spawn_x, spawn_y, 52 * px, 26 * px, 15, 2 * px, 3, abstinence2)
            enemies.append(monster)

    spawnDelay -= 1
    if spawnDelay < 0:
        spawnDelay = 10

    calculate_movement(movementSpeed)

    for structure in graveyardHitBoxes:
        check_collisions(structure, player)

    graveyardStructureTing.move(w_moved, a_moved, s_moved, d_moved)
    graveyardStructureTing.draw()

    parkStructure.move(w_moved, a_moved, s_moved, d_moved)
    parkStructure.draw()

    player.draw(px)

    for attack in projectiles:
        for monster in enemies:

            if monster.xPos <= attack.xPos <= monster.xPos + monster.width and monster.yPos <= attack.yPos <= monster.yPos + monster.height:

                try:
                    monster.health -= 1
                    projectiles.remove(attack)
                    pygame.mixer.Sound.play(enemyHitSound)

                except ValueError:
                    pass

        attack.move(w_moved, a_moved, s_moved, d_moved)
        attack.travel(centerX)
        attack.draw()

    for monster in enemies:
        if monster.health == 0:
            enemies.remove(monster)
            willpowerPoints += 1
            pygame.mixer.Sound.play(killSound)
        enemy_attack(monster, player)
        monster.move(w_moved, a_moved, s_moved, d_moved)
        monster.travel(centerX, centerY)
        monster.draw(centerX, centerY)

    for structure in graveyardHitBoxes:
        structure.move(w_moved, a_moved, s_moved, d_moved)
        structure.draw()

    # fog(temptationPoints)

    display_mouse_coordinates()

    gameWindow.blit(HUD, (0, 0))

    level_progression = 10 + willpowerLevel * 5
    willpower_bar(willpowerPoints, willpowerLevel, level_progression)
    if willpowerPoints >= level_progression:
        willpowerLevel += 1
        willpowerPoints = 0
        pygame.mixer.Sound.play(levelUpSound)

    temptation_graphics(temptationPoints)

    if temptationPoints >= 100:

        enemies.clear()

        startTime = pygame.time.get_ticks()
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
            timeSinceSetback = pygame.time.get_ticks() - startTime
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


    '''
        if startTime:
        timeSinceSetback = pygame.time.get_ticks() - startTime
        setbackTimer = font.render(f'time left: {timeSinceSetback}', True, 'purple')
        gameWindow.blit(setbackTimer, (100 * px, 100 * px))
    '''

    graphicsDelay -= 1

    # Update game window
    pygame.display.flip()
