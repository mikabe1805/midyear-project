import pygame
import random
from tkinter import *
pygame.init()

class Pong(Frame):
   """ pong game """
   def __init__(self, master, character, callback_on_selected):
        super().__init__(master)
        self.callback = callback_on_selected
        self.character = character
        self.grid()

   def play_pong(self):
        pygame.init()

        var = pygame.display.set_mode((750, 500))

        pygame.display.set_caption('Danganronpa Pong')

        brickColor = (128,0,128)
        bbColor = (255,20,147)
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
        
        hitSound = pygame.mixer.Sound("bullet.wav")
        bounceSound = pygame.mixer.Sound("hitGameSound.wav")
        hitSound.set_volume(.2)
        bounceSound.set_volume(.2)
        class Paddle(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface([20, 80])
                self.image.fill(bbColor)
                self.rect = self.image.get_rect()
                self.points = 0

        class Ball(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.Surface([15, 15])
                self.image.fill(bbColor)
                self.rect = self.image.get_rect()
                self.speed = 12
                self.dx = 1
                self.dy = 1

        paddle1 = Paddle()
        paddle1.rect.x = 25
        paddle1.rect.y = 225

        paddle2 = Paddle()
        paddle2.rect.x = 715
        paddle2.rect.y = 225

        pong = Ball()
        pong.rect.x = 375
        pong.rect.y = 250

        all_sprites = pygame.sprite.Group()
        all_sprites.add(paddle1, paddle2, pong)

        def redraw():
            background_image = pygame.image.load('sprites/'+self.character+'.png').convert_alpha()

            var.blit(background_image, [0,0])
            #Font for the title 
            font = pygame.font.Font("SuperLegendBoy-4w8Y.ttf", 30)
            font2 = pygame.font.Font("SuperLegendBoy-4w8Y.ttf", 50)
            text = font.render("Dangonronpa Pong", False, brickColor)
            textRect = text.get_rect()
            textRect.center = (750//2, 25)
            var.blit(text, textRect)

            #Score visual for Player 1
            player1_score = font.render(str(paddle1.points), False, brickColor)
            player1Rect = player1_score.get_rect()
            player1Rect.center = (50, 50)
            var.blit(player1_score, player1Rect)

            # Player 2 Score
            player2_score = font.render(str(paddle2.points), False, brickColor)
            player2Rect = player2_score.get_rect()
            player2Rect.center = (700, 50)
            var.blit(player2_score, player2Rect)

            win1Text = font2.render("Player 1 Wins!", False, brickColor)
            win2Text = font2.render("Player 2 Wins!", False, brickColor)
            win1Rect = win1Text.get_rect()
            win2Rect = win2Text.get_rect()
            replayText = font.render("Press Space To Play Again", False, brickColor)
            replayRect = replayText.get_rect()
            win1Rect.center = (375, 250)
            win2Rect.center = (375, 250)
            replayRect.center = (375, 320)
            if paddle1.points == 10:
                var.blit(win1Text, win1Rect)
                var.blit(replayText, replayRect)
            if paddle2.points == 10:
                var.blit(win2Text, win2Rect)

            all_sprites.draw(var)
            pygame.display.update()

        run = True

        while run:
            if paddle1.points < 10 and paddle2.points < 10:
                pygame.time.delay(25)
                if paddle1.rect.y > 390:
                    paddle1.rect.y = 390
                if paddle1.rect.y < 10:
                    paddle1.rect.y = 10
                if paddle2.rect.y > 390:
                    paddle2.rect.y = 390
                if paddle2.rect.y < 10:
                    paddle2.rect.y = 10

                key = pygame.key.get_pressed()
                if key[pygame.K_w]:
                    paddle1.rect.y += -20
                if key[pygame.K_s]:
                    paddle1.rect.y += 20
                if key[pygame.K_UP]:
                    paddle2.rect.y += -20
                if key[pygame.K_DOWN]:
                    paddle2.rect.y += 20

                pong.rect.x += pong.speed * pong.dx
                pong.rect.y += pong.speed * pong.dy


                if pong.rect.y > 490:
                    pong.dy = -1

                if pong.rect.x > 740:
                    pong.rect.x, pong.rect.y = 375, 250
                    pong.dx = -1
                    paddle1.points += 1

                if pong.rect.y < 15:
                    pong.dy = 1

                if pong.rect.x < 15:
                    pong.rect.x, pong.rect.y = 375, 250
                    pong.dx = 1
                    paddle2.points += 1

                if paddle1.rect.colliderect(pong.rect):
                    pong.dx = 1
                    bounceSound.play()

                if paddle2.rect.colliderect(pong.rect):
                    pong.dx = -1
                    bounceSound.play()

                redraw()

            keys = pygame.key.get_pressed()
            if paddle1.points == 10 or paddle2.points == 10:
                if keys[pygame.K_SPACE]:
                    paddle1.points = 0 
                    paddle2.points = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
        pygame.quit()

