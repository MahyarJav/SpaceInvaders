import pygame as pg
import random


def main():
    # Game Title and Icon
    pg.display.set_caption('Space Invaders')
    GameIcon = pg.image.load('Images/space-invaders.png')
    pg.display.set_icon(GameIcon)
    # Game background load
    backgroundImg = pg.image.load('Images/background.jpg')
    # Player load
    playerImg = pg.image.load('Images/player.png')
    playerX = 580
    playerY = 640
    playerX_move = 0

    # Enemy load
    # Enemy 1
    enemyOneImg = pg.image.load('Images/enemy1.png')
    E1x = random.randint(20, 1215)
    E1y = random.randint(50, 280)
    E1x_change = 0.5
    E1y_change = 25
    # Enemy 2
    enemyTwoImg = pg.image.load('Images/enemy2.png')
    E2x = random.randint(120, 1215)
    E2y = random.randint(50, 280)
    E2x_change = 0.5
    E2y_change = 25
    # Enemy 3
    enemyThreeImg = pg.image.load('Images/enemy3.png')
    E3x = random.randint(220, 1215)
    E3y = random.randint(50, 280)
    E3x_change = 0.5
    E3y_change = 25

    # Player boundaries
    boundariesX_min = 0
    boundariesX_max = 1215
    bxMin = boundariesX_min
    bxMax = boundariesX_max

    # Bullet load
    bulletImg = pg.image.load("Images/bullet.png")
    # unused
    # bulletX = 1
    bulletY = 640
    bulletY_change = 100
    # not used yet
    # bulletX_change = 1
    bullet_state = 12

    # Loads in images (Player, Bullets and Enemies)
    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemyOne(x, y):
        screen.blit(enemyOneImg, (x, y))

    def enemyTwo(x, y):
        screen.blit(enemyTwoImg, (x, y))

    def enemyThree(x, y):
        screen.blit(enemyThreeImg, (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = True
        if bullet_state is True:
            bullet_state = False
        screen.blit(bulletImg, (x, y))
        print(bullet_state)
    # Creates game screen - half values - 640 x 360
    screen = pg.display.set_mode((1280, 720))

    # Game screen loop
    running = True
    while running:
        # RGB fill
        screen.fill((255, 255, 255))

        # Background loop
        screen.blit(backgroundImg, (0, 0))

        # Quit if window quit button is pushed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Player movement via W&D/Arrows
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    playerX_move = -2
                if (event.key == pg.K_d or event.key == pg.K_RIGHT):
                    playerX_move = 2
                if (event.key == pg.K_SPACE or event.key == pg.K_w or
                        event.key == pg.K_UP):
                    fire_bullet(playerX, bulletY)
            if event.type == pg.KEYUP:
                if (event.key == pg.K_a or event.key == pg.K_RIGHT or
                        event.key == pg.K_d or event.key == pg.K_LEFT):
                    playerX_move = 0
        # Boundaries to ensure player & Enemies doersn't go off screen.
        if playerX <= bxMin:
            playerX = bxMin
        elif playerX >= bxMax:
            playerX = bxMax
        # Enemy movement

        # Enemy 1
        E1x += E1x_change

        if E1x <= bxMin:
            E1x_change = 0.5
            E1y += E1y_change
        elif E1x >= bxMax:
            E1x_change = -0.5
            E1y += E1y_change

        # Enemy 2
        E2x += E2x_change

        if E2x <= bxMin:
            E2x_change = 0.5
            E2y += E2y_change
        elif E2x >= bxMax:
            E2x_change = -0.5
            E2y += E2y_change
        # Enemy 3
        E3x += E3x_change

        if E3x <= bxMin:
            E3x_change = 0.5
            E3y += E3y_change
        elif E3x >= bxMax:
            E3x_change = -0.5
            E3y += E3y_change

        if bullet_state is True:
            fire_bullet(playerX, bulletY)
            bulletY -= bulletY_change

        # Running player functions
        playerX += playerX_move
        player(playerX, playerY)
        enemyOne(E1x, E1y)
        enemyTwo(E2x, E2y)
        enemyThree(E3x, E3y)
        pg.display.update()


if __name__ == '__main__':

    pg.init()
    main()
    pg.quit()
