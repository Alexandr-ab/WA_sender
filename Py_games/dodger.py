import pygame
from random import randint
from pygame.locals import *
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 60
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 15
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Press esc = quit
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# setup pygame, window and cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# fonts setup
font = pygame.font.SysFont(None, 35)

# Sounds setup
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('roach.mp3')

# images setup
playerImage = pygame.image.load('sofia.png')
playerStrachedImage = pygame.transform.scale(playerImage, (60, 60))
playerRect = playerStrachedImage.get_rect()
baddieImage = pygame.image.load('head.png')

# Draw starting screen
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press Enter to start', font, windowSurface, (WINDOWWIDTH / 5) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()

topScore = 0
while True:
    # Initial setup
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    while True: # The game cicle is repeating while the game is going
        score += 1 # Increase score points
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = True
                    moveLeft = False
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft == False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight == False
                if event.key == K_UP or event.key == K_w:
                    moveUp == False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown == False

            if event.type == MOUSEMOTION:
                # if mouse is mooving - move the player to the cursor
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]

        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(randint(0, WINDOWHEIGHT - baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                         'speed': randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(baddieImage,(baddieSize, baddieSize))}
            baddies.append(newBaddie)

        # Move the player on the window
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # move the baddies down
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # remove the baddies who falls under bottom
        for b in baddies[:]:
            if b['rect'].top> WINDOWHEIGHT:
                baddies.remove(b)

        # draw onto the surface
        windowSurface.fill(BACKGROUNDCOLOR)

        # draw the score and best score
        drawText(f'Score: {score}', font, windowSurface, 10, 0)
        drawText(f'Best Score: {topScore}', font, windowSurface, 10, 40)

        #draw surface
        windowSurface.blit(playerStrachedImage, playerRect)

        # draw baddies
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check the collisions
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # setup new top score
            break

        mainClock.tick(FPS)

    # draw gamw and text 'gameover'
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('The game is over!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press any button to start new game', font, windowSurface, (WINDOWWIDTH / 3) - 120, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
    gameOverSound.stop()


