import pygame
import random
pygame.init()

# game window
sw = 800
sh = 800
win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Breakout: Danganronpa Edition")

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKPURPLE = (84, 22, 180)
MAGENTA = (228, 0, 224)

# background
bg = pygame.image.load('hopespeak.png')

# clock for fps
clock = pygame.time.Clock()

# game over
gameover = False

# paddle
class Paddle(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xx = self.x + self.w
        self.yy = self.y + self.h
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])

# ball
class Ball(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xv = 5
        self.yv = 5
        self.xx = self.x + self.w
        self.yy = self.y + self.h

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])    

    def move(self):
        self.x += self.xv
        self.y += self.yv

# brick
class Brick(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.visible = True
        self.xx = self.x + self.w
        self.yy = self.y + self.h


    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])

bricks = []
def init():
    global bricks
    bricks = []
    for i in range(4):
        for j in range(10):
            bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (DARKPURPLE)))

# main loop
def redrawGameWindow():
    win.blit(bg, (0,0))
    player.draw(win)
    for ball in balls:
        ball.draw(win)
    for b in bricks:
        b.draw(win)

    font = pygame.font.SysFont('comicsans', 50)

# game over
    if gameover:
        if len(bricks) == 0:
            resText = font.render("Why did you slay..", 1, (MAGENTA))
        else:
            resText = font.render("You flopped asl...", 1, (MAGENTA))
        win.blit(resText, ((sw//2 - resText.get_width()//2), sh//2 - resText.get_height()//2))
        playAgainText = font.render("Press Space to Play Again", 1, (MAGENTA))
        win.blit(playAgainText, ((sw//2 - playAgainText.get_width()//2), sh//2 + 30 ))

    pygame.display.update()

player = Paddle(sw/2 - 50, sh - 100, 125, 20, (MAGENTA))
ball = Ball(sw/2 - 10, sh - 50, 20, 20, (MAGENTA))
balls = [ball]
init()

run = True
while run:
    clock.tick(100)
    if not gameover:
        ball.move()
        if pygame.mouse.get_pos()[0] - player.w//2 < 0:
            player.x = 0
        elif pygame.mouse.get_pos()[0] + player.w//2 > sw:
            player.x = sw - player.w
        else:
            player.x = pygame.mouse.get_pos()[0] - player.w //2

        
        for ball in balls:
            if (ball.x >= player.x and ball.x <= player.x + player.w) or (ball.x + ball.w >= player.x and ball.x + ball.w <= player.x + player.w):
                if ball.y + ball.h >= player.y and ball.y + ball.h <= player.y + player.h:
                    ball.yv *= -1
                    ball.y = player.y -ball.h -1

        if ball.x + ball.w >= sw:
            ball.xv *= -1
        if ball.x < 0:
            ball.xv *= -1
        if ball.y <= 0:
            ball.yv *= -1
        
        if ball.y > sh:
            balls.pop(balls.index(ball))

        for brick in bricks:
            if (ball.x >= brick.x and ball.x <= brick.x + brick.w) or ball.x + ball.w >= brick.x and ball.x + ball.w <= brick.x + brick.w:
                if (ball.y >= brick.y and ball.y <= brick.y + brick.h) or ball.y + ball.h >= brick.y and ball.y + ball.h <= brick.y + brick.h:
                    brick.visible = False
                    bricks.pop(bricks.index(brick))
                    ball.yv *= -1

        if ball.y > sh:
            gameover = True

    keys = pygame.key.get_pressed()
    if len(bricks) == 0:
        won = True
        gameover = True
    if gameover:
        if keys[pygame.K_SPACE]:
            gameover = False
            won = False
            ball = Ball(sw/2 - 10, sh - 200, 20, 20, (MAGENTA))
            if len(balls) == 0:
                balls.append(ball)

            bricks.clear()
            for i in range(4):
                for j in range(10):
                    bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (DARKPURPLE)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawGameWindow()

pygame.quit()
