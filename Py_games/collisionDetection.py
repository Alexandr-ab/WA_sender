import pygame
from pygame.locals import *
from random import randint

# pygame set up
pygame.init()
mainClock = pygame.time.Clock()

# window set up
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection')

# color set up
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(randint(0, WINDOWWIDTH - FOODSIZE), randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Create moves variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

# Start game cicle
while True:
    # Event listening
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            # Change keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = randint(0, WINDOWHEIGHT - player.height)
                player.left = randint(0, WINDOWHEIGHT - player.width)
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new 'food'
        foodCounter = 0
        foods.append(pygame.Rect(randint(0, WINDOWWIDTH - FOODSIZE), randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background
    windowSurface.fill(WHITE)

    # Move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the player onto the surface
    pygame.draw.rect(windowSurface, BLACK, player)

    # check the crossing of the player and the food
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
    # Draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Display the window
    pygame.display.update()
    mainClock.tick(40)