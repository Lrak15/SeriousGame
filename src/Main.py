
# Import libraries
from GameObjects import GameObject
from GameObjects import Structure
from GameObjects import HitBox
import pygame
pygame.init()

# Set frames per second
fps = 69
timer = pygame.time.Clock()

# Set up game window
screenWidth, screenHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
gameWindow = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption('placeholder title')

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


Running = True

while Running:
    timer.tick(fps)

    gameWindow.fill('blue')

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

    mousePosition = pygame.mouse.get_pos()
    pygame.draw.rect(gameWindow, 'purple', pygame.Rect(mousePosition[0], mousePosition[1], 10 * px, 10 * px), 3 * px)

    movementSpeed = 2
    graveyardStructureTing.move(movementSpeed)
    graveyardStructureTing.draw()

    graveyardHitBox1.move(movementSpeed)
    graveyardHitBox2.move(movementSpeed)
    graveyardHitBox3.move(movementSpeed)
    graveyardHitBox4.move(movementSpeed)

    graveyardHitBox1.draw()
    graveyardHitBox2.draw()
    graveyardHitBox3.draw()
    graveyardHitBox4.draw()

    # Update game window
    pygame.display.flip()
