import pygame
import random
from tkinter import *
pygame.init()

class Breakout(Frame):
   """ breakout game """
   def __init__(self, master, character, callback_on_selected):
        super().__init__(master)
        self.callback = callback_on_selected
        self.character = character
        self.grid()
        self.play_breakout()

   def play_breakout(self):
        pygame.init()
        # game window
        sw = 800
        sh = 800
        win = pygame.display.set_mode((sw, sh))
        pygame.display.set_caption("Breakout")

        # sound effects
        brickHitSound = pygame.mixer.Sound("bullet.wav")
        bounceSound = pygame.mixer.Sound("hitGameSound.wav")
        loseSound = pygame.mixer.Sound("punishmentTime.wav")
        trashieSound = pygame.mixer.Sound("trashie.wav")
        bounceSound.set_volume(.2)
        loseSound.set_volume(.3)
        brickHitSound.set_volume(.2)
        brickHitSound.set_volume(.2)
        trashieSound.set_volume(.2)
        
        # lives and score
        lives = 3
        score = 0
        level = 1
        hss = False 

        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            
        # background
        bg = pygame.image.load('sprites/'+self.character+'.png').convert_alpha()

        # clock for fps
        clock = pygame.time.Clock()
        
        # define colors
        bbColor = (228, 0, 224)
        brickColor = (84, 22, 180)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BLUE = (0, 181, 236)
        if self.character == 'celestia':
            bbColor = (110, 18, 9)
            brickColor = (58, 52, 60)
        if self.character == 'chiaki':
            bbColor = (216, 165, 168)
            brickColor = (24, 43, 50) 
        if self.character == 'chihiro':
            bbColor = (73, 57, 43)
            brickColor = (68, 68, 37)
        if self.character == 'junko':
            bbColor = (161, 51, 60)
            brickColor = (226, 196, 193)
        if self.character == 'kazuichi':
            bbColor = (173, 73, 115)
            brickColor = (165, 153, 31)
        if self.character == 'nagito':
            bbColor = (91, 101, 92)
            brickColor = (127, 11, 8)
        if self.character == 'sakura':
            bbColor = (129, 16, 16)
            brickColor = (150, 82, 27)
        if self.character == 'taka':
            bbColor = (70, 55, 71)
            brickColor = (134, 18, 32)
        """ celestia = black(58, 52, 60) red(110, 18, 9)
        chiaki = green(24, 43, 50) light pink(216, 165, 168)
        chihiro = green(68, 68, 37) brown(73, 57, 43)
        junko = red(161, 51, 60) pink(226, 196, 193)
        kazuichi = pink(173, 73, 115) green(165, 153, 31)
        nagito = green(91, 101, 92) red(127, 11, 8)
        sakura = red(129, 16, 16) brown(150, 82, 27)
        taka = dark purple(70, 55, 71) red(134, 18, 32)
 """
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
                self.xv = random.choice([2, 3, 4, -2, -3, -4])
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

                self.ranNum = random.randint(0,8)
                if self.ranNum < 1:
                    self.pregnant = True
                else:
                    self.pregnant = False

            def draw(self, win):
                pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])

        bricks = []
        def init():
            global bricks
            bricks = []
            for i in range(5):
                for j in range(10):
                    bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))
       
        # main loop
        def redrawGameWindow():
            win.blit(bg, (0,0))
            player.draw(win)
            for ball in balls:
                ball.draw(win)
            for b in bricks:
                b.draw(win)

            font = pygame.font.Font("SuperLegendBoy-4w8y.ttf", 30)
            font2 = pygame.font.Font("SuperLegendBoy-4w8y.ttf", 25)

            tLives = font2.render("Lives: " + str(lives), 1, (BLACK))
            win.blit(tLives, (12,500))
            tscore = font2.render("Score: " + str(score), 1, (BLACK))
            win.blit(tscore, (12,460))
            tHS = font2.render("HS: " + str(hiscore), 1, (RED))
            win.blit(tHS, (12,400))
            tLevel = font2.render("Level: " + str(level), 1, (BLUE))
            win.blit(tLevel, (12,250))

        # win
            if len(bricks) == 0 and score > 0:
                winText = font.render("Level Complete", 1, (BLUE))
                win.blit(winText, ((sw//2 - winText.get_width()//2), sh//2 - winText.get_height()//2))
                playAgainText = font2.render("Press space to continue to the next level", 1, (178, 109, 71))
                win.blit(playAgainText, ((sw//2 - playAgainText.get_width()//2), sh//2 + 30 ))


        # game over
            if lives == 0:
                if hss == True:
                    hssText = font.render("NEW HIGH SCORE", 1, (RED))
                    win.blit(hssText, ((sw//2 - hssText.get_width()//2), sh//2 - hssText.get_height()//2))
                    slayText = font2.render("Why did you slay...", 1, (BLUE))
                    win.blit(slayText, ((sw//2 - slayText.get_width()//2), sh//2 + 30 ))
                    playAgainText = font2.render("Press space to play again", 1, (178, 109, 71))
                    win.blit(playAgainText, ((sw//2 - playAgainText.get_width()//2), sh//2 + 80 ))
                else: 
                    resText = font.render("You flopped asl...", 1, (BLUE))
                    win.blit(resText, ((sw//2 - resText.get_width()//2), sh//2 - resText.get_height()//2))
                    playAgainText = font2.render("Press space to play again", 1, (178, 109, 71))
                    win.blit(playAgainText, ((sw//2 - playAgainText.get_width()//2), sh//2 + 30 ))
    
            pygame.display.update()

        player = Paddle(sw/2 - 50, sh - 100, 125, 20, (bbColor))
        ball = Ball(sw/2 - 10, sh - 50, 20, 20, (bbColor))
        balls = [ball]
        init()
        
        run = True
        while run:
            clock.tick(100)
            if lives > 0 and len(bricks) != 0:
                for ball in balls:
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
                            bounceSound.play()
                    if ball.x + ball.w >= sw:
                        bounceSound.play()
                        ball.xv *= -1
                    if ball.x < 0:
                        bounceSound.play()
                        ball.xv *= -1
                    if ball.y <= 0:
                        bounceSound.play()
                        ball.yv *= -1
                    
                    if ball.y > sh:
                        balls.pop(balls.index(ball))
            
                for brick in bricks:
                    for ball in balls:
                        if (ball.x >= brick.x and ball.x <= brick.x + brick.w) or ball.x + ball.w >= brick.x and ball.x + ball.w <= brick.x + brick.w:
                            if (ball.y >= brick.y and ball.y <= brick.y + brick.h) or ball.y + ball.h >= brick.y and ball.y + ball.h <= brick.y + brick.h:
                                brick.visible = False
                                if brick.pregnant:
                                    balls.append(Ball(brick.x, brick.y, 20, 20, (bbColor)))
                                ball.yv *= -1
                                score += 1
                                brickHitSound.play()
                                break

                for brick in bricks:
                    if brick.visible == False:
                        bricks.pop(bricks.index(brick))

                if len(balls) == 0:
                    ball = Ball(sw/2 - 10, sh - 300, 20, 20, (bbColor))
                    balls.append(ball)
                    lives -= 1

                if lives == 0:
                    trashieSound.play()

                if level == 3 and lives == 1:
                    lives += 1

            keys = pygame.key.get_pressed()
            if lives == 0:
                if score > int(hiscore):
                    hiscore = score
                    hss = True
                with open("hiscore.txt", "w") as f:
                    f. write(str(hiscore))
                
                if keys[pygame.K_SPACE]:
                    trashieSound.stop()
                    lives = 3
                    score = 0
                    level = 1
                    ball = Ball(sw/2 - 10, sh - 200, 20, 20, (bbColor))
                    if len(balls) == 0:
                        balls.append(ball)
                    bricks.clear()
                    for i in range(5):
                        for j in range(10):
                            bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))
            if len(bricks) == 0:
                if keys[pygame.K_SPACE]:
                    ball = Ball(sw/2 - 10, sh - 200, 20, 20, (bbColor))
                    balls.clear()
                    balls.append(ball)
                    if score > 1:
                        level += 1
                    if level > 2:
                        ball.xv = 7
                        ball.yv = 7
                        for i in range(6):
                            for j in range(10):
                                bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))
                    else:
                        for i in range(5):
                            for j in range(10):
                                bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
            redrawGameWindow()

        self.callback()

      