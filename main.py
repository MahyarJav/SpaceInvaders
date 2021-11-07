import pygame as pg
import random

def main():
    # Game Title and Icon
    pg.display.set_caption('Space Invaders')
    GameIcon = pg.image.load(r'SpaceInvaders\Images\space-invaders.png')
    pg.display.set_icon(GameIcon)
    # Player load
    playerImg = pg.image.load(r'SpaceInvaders\Images\player.png')
    playerX = 580
    playerY = 640
    playerX_move = 0

    # Enemy load
    # Enemy 1
    enemyOneImg = pg.image.load(r'SpaceInvaders\Images\enemy1.png')
    e1X = random.randint(20, 1215)
    e1Y = random.randint(50, 280)
    e1X_change = 0
    e1Y_change = 0
    # Enemy 2
    enemyTwoImg = pg.image.load(r'SpaceInvaders\Images\enemy2.png')
    e2X = random.randint(120, 1215)
    e2Y = random.randint(50, 280)
    e2X_change = 0
    e2Y_change = 0
    # Enemy 3
    enemyThreeImg = pg.image.load(r'SpaceInvaders\Images\enemy3.png')
    e3X = random.randint(220, 1215)
    e3Y = random.randint(50, 280)
    e3X_change = 0
    e3Y_change = 0
    # Player boundaries
    boundariesX_min = 0
    boundariesX_max = 1215
    bxMin = boundariesX_min
    bxMax = boundariesX_max

    # Loads in player image
    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemyOne(x, y):
        screen.blit(enemyOneImg, (x, y))

    def enemyTwo(x, y):
        screen.blit(enemyTwoImg, (x, y))

    def enemyThree(x, y):
        screen.blit(enemyThreeImg, (x, y))
    # Creates game screen - half values - 640 x 360
    screen = pg.display.set_mode((1280, 720))

    # Game screen loop
    running = True
    while running:

        # RGB fill
        screen.fill((255, 255, 255))

        # Quit if window quit button is pushed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # Player movement via WSAD/Arrows
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    playerX_move = -2
                if (event.key == pg.K_d or event.key == pg.K_RIGHT):
                    playerX_move = 2
            if event.type == pg.KEYUP:
                if (event.key == pg.K_a or event.key == pg.K_RIGHT or
                        event.key == pg.K_d or event.key == pg.K_LEFT):
                    playerX_move = 0
            # if keys[pg.K_w] or keys[pg.K_UP]:
            #    shoot()
        # Boundaries to ensure player doersn't go off screen.
        if playerX < bxMin:
            playerX = bxMin
        elif playerX > bxMax:
            playerX = bxMax

        # Running player functions
        playerX += playerX_move
        player(playerX, playerY)
        enemyOne(e1X, e1Y)
        enemyTwo(e2X, e2Y)
        enemyThree(e3X, e3Y)
        pg.display.update()


if __name__ == '__main__':

    pg.init()
    main()
    pg.quit()
