import math
import random

import pygame
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))


background = pygame.image.load('background.png')





pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
pImg = pygame.image.load('space-invaders.png')
pX = 370
pY = 480
pX_change = 0


eImg = []
eX = []
eY = []
eX_change = []
eY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    eImg.append(pygame.image.load('virus.png'))
    eX.append(random.randint(0, 736))
    eY.append(random.randint(50, 150))
    eX_change.append(4)
    eY_change.append(40)

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME END", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(pImg, (x, y))


def enemy(x, y, i):
    screen.blit(eImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(eX, eY, bulletX, bulletY):
    distance = math.sqrt(math.pow(eX - bulletX, 2) + (math.pow(eY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:


    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -5
            if event.key == pygame.K_RIGHT:
                pX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()

                    bulletX = pX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0



    pX += pX_change
    if pX <= 0:
        pX = 0
    elif pX >= 736:
        pX = 736


    for i in range(num_of_enemies):
        if eY[i] > 440:
            for j in range(num_of_enemies):
                eY[j] = 2000
            game_over_text()
            break

        eX[i] += eX_change[i]
        if eX[i] <= 0:
            eX_change[i] = 4
            eY[i] += eY_change[i]
        elif eX[i] >= 736:
            eX_change[i] = -4
            eY[i] += eY_change[i]

        collision = isCollision(eX[i], eY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 150)

        enemy(eX[i], eY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(pX, pY)
    show_score(textX, testY)
    pygame.display.update()