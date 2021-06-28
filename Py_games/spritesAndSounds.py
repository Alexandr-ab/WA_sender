import pygame, time
from pygame.locals import *
from random import randint

# pygame set up
pygame.init()
mainClock = pygame.time.Clock()

# window set up
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

# color set up
WHITE = (255, 255, 255)

# Set up the player and food data structures
player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('sofia.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('heart.png')
foodStretchImage = pygame.transform.scale(foodImage, (20, 20))
headImage = pygame.image.load('head.png')
headStretchImage = pygame.transform.scale(headImage, (50, 50))

foods = []
for i in range(20):
    foods.append(pygame.Rect(randint(0, WINDOWWIDTH - 20), randint(0, WINDOWHEIGHT - 20), 20, 20))
foodCounter = 0
NEWFOOD = 20
heads = []
headCounter = 0
NEWHEAD = 300

# Create moves variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

# Music setup
pickUpSound = pygame.mixer.Sound('pick_up.wav')
pygame.mixer.music.load('roach.mp3')
pygame.mixer.music.play(-1, 0.0)
headSound = pygame.mixer.Sound('head.wav')
musicPlaying = True

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
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
    foodCounter += 1
    headCounter += 1
    if player.height <= WINDOWHEIGHT:
        if foodCounter >= NEWFOOD:
            # add new 'food'
            foodCounter = 0
            foods.append(pygame.Rect(randint(0, WINDOWWIDTH - 20), randint(0, WINDOWHEIGHT - 20), 20, 20))
        if headCounter >= NEWHEAD:
            headCounter = 0
            heads.append(pygame.Rect(randint(0, WINDOWWIDTH - 50), randint(0, WINDOWHEIGHT - 50), 50, 50))
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
    windowSurface.blit(playerStretchedImage, player)

    # check the crossing of the player and the food
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                pickUpSound.play()
    for head in heads[:]:
        if player.colliderect(head):
            heads.remove(head)
            player = pygame.Rect(player.left, player.top, player.width + 20, player.height + 20)
            playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
            if musicPlaying:
                headSound.play()

    # Draw the food
    for food in foods:
        windowSurface.blit(foodStretchImage, food)
    for head in heads:
        windowSurface.blit(headStretchImage, head)

    # Display the window
    pygame.display.update()
    mainClock.tick(40)