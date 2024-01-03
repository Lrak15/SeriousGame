
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

# Load font
font = pygame.font.Font('Graphics/DS-DIGIB.TTF', 20)
font2 = pygame.font.Font('Graphics/DS-DIGIB.TTF', 50)
font3 = pygame.font.Font('Graphics/LEDLIGHT.otf', 50)
font4 = pygame.font.Font('Graphics/LEDLIGHT.otf', 52)


# Load images
graveyard = pygame.image.load('Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (100 * px, 100 * px))
graveyardRect = graveyard.get_rect()

spillermandhahasej = pygame.image.load('Graphics/PLayer.png')
spiller = pygame.transform.scale(spillermandhahasej, (100, 200))

rygemonster = pygame.image.load('Graphics/Ryge_monster.png')
fjende = pygame.transform.scale(rygemonster, (100, 100))

unfittedHUD = pygame.image.load('Graphics/New Piskel-2.png (1).png')
HUD = pygame.transform.scale(unfittedHUD, (screenWidth, screenHeight))

unfittedSetbackFrame = pygame.image.load('Graphics/setback-1.png.png')
setbackFrame = pygame.transform.scale(unfittedSetbackFrame, (screenWidth, screenHeight))

unfittedFog1 = pygame.image.load('Graphics/fog-1.png.png')
fog1TopLeft = pygame.transform.scale(unfittedFog1, (screenWidth, screenHeight))
fog1TopRight = pygame.transform.flip(fog1TopLeft, True, False)
fog1BottomLeft = pygame.transform.flip(fog1TopLeft, False, True)
fog1BottomRight = pygame.transform.flip(fog1TopLeft, True, True)

unfittedFog2 = pygame.image.load('Graphics/fog-2.png.png')
fog2TopLeft = pygame.transform.scale(unfittedFog2, (screenWidth, screenHeight))
fog2TopRight = pygame.transform.flip(fog2TopLeft, True, False)
fog2BottomLeft = pygame.transform.flip(fog2TopLeft, False, True)
fog2BottomRight = pygame.transform.flip(fog2TopLeft, True, True)

unfittedFog3 = pygame.image.load('Graphics/fog-3.png.png')
fog3TopLeft = pygame.transform.scale(unfittedFog3, (screenWidth, screenHeight))
fog3TopRight = pygame.transform.flip(fog3TopLeft, True, False)
fog3BottomLeft = pygame.transform.flip(fog3TopLeft, False, True)
fog3BottomRight = pygame.transform.flip(fog3TopLeft, True, True)

fogTopLeft = [fog1TopLeft, fog2TopLeft, fog3TopLeft]
fogTopRight = [fog1TopRight, fog2TopRight, fog3TopRight]
fogBottomLeft = [fog1BottomLeft, fog2BottomLeft, fog3BottomLeft]
fogBottomRight = [fog1BottomRight, fog2BottomRight, fog3BottomRight]



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

spawnDelay = 30
attackDelay = 0
graphicsDelay = 0


willpowerPoints = 0
willpowerLevel = 0

temptationPoints = 0

projectiles = []
enemies = []

startTime = None


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
    points_display = font.render(f'{points}/{progress}', True, 'purple')
    level_display = font.render(f'LEVEL {level}', True, 'purple')

    pygame.draw.rect(gameWindow, 'yellow', (40 * px, 172 * px, (points / progress) * 240 * px, 5 * px))

    gameWindow.blit(points_display, (41 * px, 172.2 * px))
    gameWindow.blit(level_display, (262 * px, 172.2 * px))


def temptation_graphics(points):
    global graphicsDelay

    try:
        pygame.draw.rect(gameWindow, (205 + 0.5 * points, 180 - 1.8 * points, 0), (261 * px, 3 * px, (points / 100) * 50 * px, 5 * px))
    except ValueError:
        pygame.draw.rect(gameWindow, (255, 0, 0), (261 * px, 3 * px, 50 * px, 5 * px))

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





def enemy_attack(monster, player):
    global temptationPoints
    if monster.hitbox.colliderect(player.hitbox):
        player_health = 25
        try:
            enemies.remove(monster)
            temptationPoints += 10
        except ValueError:
            pass

    # if abs(first.xPos - second.xPos) <= 5 and abs(first.yPos - second.yPos) <= 5:




Customise = True
Running = True
Spawning = True
Setback = False


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

    movementSpeed = 5 - temptationPoints / 30
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
        spawnDelay = 30

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

    fog(temptationPoints)

    display_mouse_coordinates()

    gameWindow.blit(HUD, (0, 0))

    level_progression = 10 + willpowerLevel * 5
    willpower_bar(willpowerPoints, willpowerLevel, level_progression)
    if willpowerPoints >= level_progression:
        willpowerLevel += 1
        willpowerPoints = 0

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
