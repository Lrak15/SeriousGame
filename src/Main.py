
# Import libraries
from GameObjects import GameObject
from GameObjects import Structure
from GameObjects import HitBox
from GameObjects import Player
from GameObjects import Projectile
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

tingeling1, tingeling2 = screenWidth / 16, screenHeight / 9
tingeling3 = tingeling1 / tingeling2
if tingeling3 == 1:
    print('Your screen is in 16/9 format :)')
else:
    print('!!!Your screen is NOT in 16/9 format!!!')
    # Can i make this text display in red instead ?????????????????????????????????????????????????????????????????????????????????

# Define pixel size
px = round(screenHeight / 200)

# Load images
graveyard = pygame.image.load('../Graphics/graveyard.png')
graveyard = pygame.transform.scale(graveyard, (100 * px, 100 * px))
graveyardRect = graveyard.get_rect()

calculatorForGameobjects = GameObject(gameWindow, 69, 69, 69, 69)

graveyardStructureTing = Structure(gameWindow, 100, 100, 69, 69, graveyard)

graveyardHitBox1 = HitBox(gameWindow, 100, 100, 100, 100, 'red', px)
graveyardHitBox2 = HitBox(gameWindow, 200, 200, 90, 90, 'red', px)
graveyardHitBox3 = HitBox(gameWindow, 300, 300, 70, 70, 'red', px)
graveyardHitBox4 = HitBox(gameWindow, 400, 400, 40, 40, 'red', px)

graveyardHitBoxes = [graveyardHitBox1, graveyardHitBox2, graveyardHitBox3, graveyardHitBox4]

projectiles = []

Customise = True
Running = True


while Customise:
    timer.tick(fps)

    gameWindow.fill('white')

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

while Running:
    timer.tick(fps)

    movementSpeed = 2
    projectileSpeed = 1
    mousePosition = pygame.mouse.get_pos()

    gameWindow.fill('blue')

    # Check for pygame events
    for event in pygame.event.get():

        # Check for keys pressed
        if event.type == pygame.KEYDOWN:

            # Close game if escape key is pressed
            if event.key == pygame.K_ESCAPE:
                Running = False

            if event.key == pygame.K_0:
                shot = Projectile(gameWindow, centerX, centerY, 69, 69, 420, projectileSpeed, mousePosition[0],
                                  (screenHeight - mousePosition[1]))

                print(f'mouseX({mousePosition[0]}) - centerX({centerX}) = {mousePosition[0] - centerX}')
                print(f'mouseY({screenHeight - mousePosition[1]}) - centerY({centerY}) = {(screenHeight - mousePosition[1]) - centerY}')
                print(f'angle between these is arctan({(screenHeight - mousePosition[1]) - centerY} / {mousePosition[0] - centerX}) = {shot.angle}')
                # print(f'x-direction = {shot.xDirectionzzz} and y-direction = {shot.yDirectionzzz}')
                projectiles.append(shot)

        # Close game if the game windows close button is pressed
        elif event.type == pygame.QUIT:
            Running = False

    reticle = pygame.draw.rect(gameWindow, 'purple', pygame.Rect(mousePosition[0], mousePosition[1], 10 * px, 10 * px), 3 * px)

    graveyardStructureTing.move(movementSpeed)
    graveyardStructureTing.draw()

    for i in graveyardHitBoxes:
        i.move(movementSpeed)
        i.draw()

    for i in projectiles:
        if i.xPos < 0 or i.xPos > screenWidth or i.yPos < 0 or i.yPos > screenHeight:
            projectiles.remove(i)
        i.move(movementSpeed)
        i.travel(centerX)
        i.draw()

    # Update game window
    pygame.display.flip()
