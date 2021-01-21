import pygame
import random
import math
from pygame import mixer
# to inatilatiz pygame
pygame.init()

# creat a screen
screen = pygame.display.set_mode((800, 600))

# changing the name of game/windos
pygame.display.set_caption('alien invader')

# changing the icon of windos/game
icon = pygame.image.load('abc.png')
pygame.display.set_icon(icon)

# changing the color of background
background_color = (0, 0, 0)
background = pygame.image.load('background.png.png')

# player display
playerimg = pygame.image.load('spaceship.png')
spaceshipX = 370
spaceshipY = 480
spaceshipX_change = 0


# number of enimies
enimiesimg = []
enimiesX = []
enimiesY = []
enimiesX_change = []
enimiesY_change = []
no_of_enimies = 6

# enimies display
for i in range(no_of_enimies):
    enimiesimg.append(pygame.image.load('enemies.png'))
    enimiesX.append(random.randint(0, 800))
    enimiesY.append(random.randint(50, 150))
    enimiesX_change.append(0.3)
    enimiesY_change.append(40)


# bullet display
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.3
bullet_state = 'ready'
# displaying score in windos
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render('score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def spaceship(x, y):
    screen.blit(playerimg, (x, y))


def enimies(x, y, i):
    screen.blit(enimiesimg[i], (x, y))


def iscollision(enimiesX, enimiesY, bulletx, bulletY):
    distance = math.sqrt(math.pow(enimiesX - bulletX, 2)) + \
        (math.pow(enimiesY - bulletY, 2))

    if distance < 27:
        return True
    else:
        return False


# quiting the screen when wanted
running = True
while running:
    screen.fill(background_color)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if key strock is pressed check weather right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceshipX_change = -0.3
            if event.key == pygame.K_RIGHT:
                spaceshipX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('bullet sound.wav')
                    bullet_sound.play()
                    bulletX = spaceshipX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                spaceshipX_change = 0
            if event.key == pygame.K_RIGHT:
                spaceshipX_change = 0

    # checking the boundry of spaceship so that it doesnt go off bound

    spaceshipX += spaceshipX_change  # not understand

    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 770:
        spaceshipX = 770
    for i in range(no_of_enimies):

        enimiesX[i] += enimiesX_change[i]  # not understand

        if enimiesX[i] <= 0:
            enimiesX_change[i] = 0.3  # moving enimies side
            enimiesY[i] += enimiesY_change[i]  # moving enimies down

        elif enimiesX[i] >= 770:
            enimiesX_change[i] = -0.3  # moving enimies side
            enimiesY[i] += enimiesY_change[i]  # moving enimies down

         # collision
        collision = iscollision(enimiesX[i], enimiesY[i], bulletX, bulletY)
        if collision:

            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enimiesX[i] = random.randint(0, 800)
            enimiesY[i] = random.randint(50, 150)

        enimies(enimiesX[i], enimiesY[i], i)

        # bullet movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = 'ready'

        if bullet_state == 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

    show_score(textX, textY)
    spaceship(spaceshipX, spaceshipY)
    pygame.display.update()
