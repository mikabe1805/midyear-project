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
        # self.play_breakout()

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
        bgmSound = pygame.mixer.Sound('voice_lines/'+self.character+'/happy.wav')
        bounceSound.set_volume(.2)
        loseSound.set_volume(.2)
        brickHitSound.set_volume(.2)
        brickHitSound.set_volume(.2)
        bgmSound.set_volume(.1)

        # lives and score
        self.lives = 3
        self.score = 0
        self.level = 1
        hss = False 
        self.pause = False

        with open("hiscore.txt", "r") as f:
            self.hiscore = f.read()
            
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
        class Paddle(pygame.sprite.Sprite):
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

            def moveLeft(self, pixels):
                self.x -= pixels
                # Check that you are not going too far (off the screen)
                if self.x < 0:
                    self.x = 0
                
            def moveRight(self, pixels):
                self.x += pixels
                # Check that you are not going too far (off the screen)
                if self.x > 700:
                    self.x = 700

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

        class Bomb(object):
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

        # power up
        class Power(object):
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
        class Brick(pygame.sprite.Sprite):
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
                
                self.ranNum = random.randint(0,10)
                if self.ranNum < 1:
                    self.explode = True
                else:
                    self.explode = False
                
                self.ranNum = random.randint(0,10)
                if self.ranNum < 1:
                    self.powerUp = True
                else:
                    self.powerUp = False

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
            self.player.draw(win)
            for ball in self.balls:
                ball.draw(win)
            for bomb in self.bombs:
                bomb.draw(win)
            for power in self.powers:
                power.draw(win)
            for b in bricks:
                b.draw(win)

            font = pygame.font.Font("SuperLegendBoy-4w8y.ttf", 30)
            font2 = pygame.font.Font("SuperLegendBoy-4w8y.ttf", 25)

            tLives = font2.render("Lives: " + str(self.lives), 1, (BLACK))
            win.blit(tLives, (12,500))
            tscore = font2.render("Score: " + str(self.score), 1, (BLACK))
            win.blit(tscore, (12,460))
            tHS = font2.render("HS: " + str(self.hiscore), 1, (RED))
            win.blit(tHS, (12,400))
            tLevel = font2.render("Level: " + str(self.level), 1, (BLUE))
            win.blit(tLevel, (12,250))

        # win
            if len(bricks) == 0 and self.score > 0:
                winText = font.render('Level ' +str(self.level)+' Complete', 1, (0, 255, 0))
                if self.level == 2:
                    win.blit(winText, ((sw//2 - winText.get_width()//2), sh//2 - 100 ))
                else:
                    win.blit(winText, ((sw//2 - winText.get_width()//2), sh//2 - winText.get_height()//2))
                playAgainText = font2.render("Press space to continue to the next level", 1, (178, 109, 71))
                win.blit(playAgainText, ((sw//2 - playAgainText.get_width()//2), sh//2 + 30 ))
                if self.level == 2:
                    bombText = font2.render("Introducing Bombs and Powerups!", 1, (brickColor))
                    win.blit(bombText, ((sw//2 - bombText.get_width()//2), sh//2 - 60 ))
                    bomb2Text = font2.render("Avoid the black balls and collect the green!", 1, (BLUE))
                    win.blit(bomb2Text, ((sw//2 - bomb2Text.get_width()//2), sh//2 - 30))


        # game over
            if self.lives == 0:
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

            if self.pause == True:
                pauseText = font.render("GAME PAUSED", 1, (BLUE))
                win.blit(pauseText, ((sw//2 - pauseText.get_width()//2), sh//2 - pauseText.get_height()//2))
                    
            pygame.display.update()


        def main(win):
            self.player = Paddle(sw/2 - 50, sh - 100, 125, 20, (bbColor))
            ball = Ball(sw/2 - 10, sh - 50, 20, 20, (bbColor))
            bomb = Bomb(sw/2 - 10, sh - 50, 20, 20, (BLACK))
            power = Power(sw/2 - 10, sh - 50, 20, 20, (0, 255, 0))
            self.bombs = [bomb]
            self.balls = [ball]
            self.powers = [power]
            sSpace = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                sSpace = True

            init()
        
            run = True
            while run:
                if self.lives > 0 and len(bricks) != 0 and self.pause == False:
                    redrawGameWindow()
                    clock.tick(100)
                    bgmSound.play()
                    for ball in self.balls:
                        ball.move()
                    for bomb in self.bombs:
                        bomb.move()
                    for power in self.powers:
                        power.move()
                        
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                        self.player.moveLeft(7)
                    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        self.player.moveRight(7)
    
                    for ball in self.balls:
                        if (ball.x >= self.player.x and ball.x <= self.player.x + self.player.w) or (ball.x + ball.w >= self.player.x and ball.x + ball.w <= self.player.x + self.player.w):
                            if ball.y + ball.h >= self.player.y and ball.y + ball.h <= self.player.y + self.player.h:
                                ball.yv *= -1
                                ball.y = self.player.y -ball.h -1
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
                            self.balls.pop(self.balls.index(ball))

                    for bomb in self.bombs:
                        if (bomb.x >= self.player.x and bomb.x <= self.player.x + self.player.w) or (bomb.x + bomb.w >= self.player.x and bomb.x + bomb.w <= self.player.x + self.player.w):
                            if bomb.y + bomb.h >= self.player.y and bomb.y + bomb.h <= self.player.y + self.player.h:
                                bomb.yv *= -1
                                bomb.y = self.player.y -bomb.h -1
                                self.balls.clear()
                                self.lives -= 1
                                self.bombs.clear()
                                self.balls.append(ball)
                        if bomb.x + bomb.w >= sw:
                            bomb.xv *= -1
                        if bomb.x < 0:
                            bomb.xv *= -1
                        if bomb.y <= 0:
                            bomb.yv *= -1
                        if bomb.y > sh:
                            self.bombs.pop(self.bombs.index(bomb))
                    
                    for power in self.powers:
                        if (power.x >= self.player.x and power.x <= self.player.x + self.player.w) or (power.x + power.w >= self.player.x and power.x + power.w <= self.player.x + self.player.w):
                            if power.y + power.h >= self.player.y and power.y + power.h <= self.player.y + self.player.h:
                                power.yv *= -1
                                power.y = self.player.y -power.h -1
                                self.balls.clear()
                                self.lives += 1
                                self.powers.clear()
                                self.balls.append(ball)
                        if power.x + power.w >= sw:
                            power.xv *= -1
                        if power.x < 0:
                            power.xv *= -1
                        if power.y <= 0:
                            power.yv *= -1
                        if power.y > sh:
                            self.powers.pop(self.powers.index(power))

                    for brick in bricks:
                        for ball in self.balls:
                            if (ball.x >= brick.x and ball.x <= brick.x + brick.w) or ball.x + ball.w >= brick.x and ball.x + ball.w <= brick.x + brick.w:
                                if (ball.y >= brick.y and ball.y <= brick.y + brick.h) or ball.y + ball.h >= brick.y and ball.y + ball.h <= brick.y + brick.h:
                                    brick.visible = False
                                    if brick.explode and self.level > 2:
                                        self.bombs.append(Bomb(brick.x, brick.y, 20, 20, (BLACK)))
                                    if brick.pregnant:
                                        self.balls.append(Ball(brick.x, brick.y, 20, 20, (bbColor)))
                                        if self.level > 1:
                                            ball.xv = 5
                                            ball.yv = 5
                                        if self.level > 2:
                                            ball.xv = 6
                                            ball.yv = 6
                                    if brick.powerUp and self.level > 2:
                                        self.powers.append(Power(brick.x, brick.y, 20, 20, (0, 255, 0)))
                                    ball.yv *= -1
                                    self.score += 1
                                    brickHitSound.play()
                                    break

                    for brick in bricks:
                        if brick.visible == False:
                            bricks.pop(bricks.index(brick))

                    if len(self.balls) == 0:
                        ball = Ball(sw/2 - 10, sh - 300, 20, 20, (bbColor))
                        self.lives -= 1
                        self.balls.append(ball)
                        if self.level > 1:
                            ball.xv = 5
                            ball.yv = 5
                        if self.level > 2:
                            ball.xv = 6
                            ball.yv = 6

                    if self.lives == 0:
                        bgmSound.stop()
                        loseSound.play()

                keys = pygame.key.get_pressed()
                if self.lives == 0:
                    if self.score > int(self.hiscore):
                        self.hiscore = self.score
                        hss = True
                    with open("hiscore.txt", "w") as f:
                        f. write(str(self.hiscore))
                    sSpace = True
                    if keys[pygame.K_SPACE]:
                        loseSound.stop()
                        self.lives = 3
                        self.score = 0
                        self.level = 1
                        ball = Ball(sw/2 - 10, sh - 200, 20, 20, (bbColor))
                        self.player = Paddle(sw/2 - 50, sh - 100, 125, 20, (bbColor))
                        if len(self.balls) == 0:
                            self.balls.append(ball)
                        bricks.clear()
                        for i in range(5):
                            for j in range(10):
                                bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))
                if len(bricks) == 0:
                    sSpace = True
                    if keys[pygame.K_SPACE]:
                        ball = Ball(sw/2 - 10, sh - 200, 20, 20, (bbColor))
                        self.player = Paddle(sw/2 - 50, sh - 100, 125, 20, (bbColor))
                        self.balls.clear()
                        self.balls.append(ball)
                        if self.score > 1:
                            self.level += 1
                        if self.level > 1:
                            if self.level == 2:
                                self.lives += 1
                            ball.xv = 5
                            ball.yv = 5
                        if self.level > 2:
                            ball.xv = 6
                            ball.yv = 6
                            for i in range(6):
                                for j in range(10):
                                    bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))
                        else:
                            for i in range(5):
                                for j in range(10):
                                    bricks.append(Brick(10 + j * 79, 50 + i * 35, 70, 25, (brickColor)))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                        run = False
                    if keys[pygame.K_w]:
                        self.lives += 1
                    if keys[pygame.K_s]:
                        self.lives -= 1
                    if keys[pygame.K_q]:
                        bricks.clear()
                        self.score += 50
                    if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        if sSpace == True:
                            sSpace = False
                        else:
                            self.pause = not self.pause
                        
                redrawGameWindow()

        def main_menu(win):
            run = True
            while run:
                win.fill((0, 0, 0))
                font = pygame.font.Font("SuperLegendBoy-4w8y.ttf", 30)
                textt = font.render("Click any key to begin", 1, (RED))
                win.blit(textt, ((sw//2 - textt.get_width()//2), sh//2 - textt.get_height()//2))
                pygame.display.update()
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                        run = False
                        self.callback()
                        # maybe bring it back to game select over here
                        # pygame.display.quit()
                    if event.type == pygame.KEYDOWN:
                        main(win)

            pygame.display.quit()
    
        main_menu(win)  # start game

        self.callback()

      