import pygame
import os
import time
import random
pygame.font.init()

width = 750
height = 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Danganronpa Space Invaders")

# Loading our Images (Temporary. I'm going to be using Danganronpa Characters)
red_space_player = pygame.image.load(os.path.join("assets", "pixel_player_red_small.png"))
green_space_player = pygame.image.load(os.path.join("assets", "pixel_player_green_small.png"))
blue_space_player = pygame.image.load(os.path.join("assets", "pixel_player_blue_small.png"))

# Player player
yellow_space_player = pygame.image.load(os.path.join("assets", "pixel_player_yellow.png"))

# Lasers
red_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
green_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blue_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellow_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
# Test
background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (width, height))

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.Ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.player_img = yellow_space_player
        self.laser_img = yellow_lasers
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health

def main():
    run = True
    fps = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    player_vel = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()

    def drawing_window():
        window.blit(background, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        window.blit(lives_label, (10, 10))
        window.blit(level_label, (width - level_label.get_width() - 10, 10))

        player.draw(window)

        pygame.display.update()

    while run == True:
        clock.tick(fps)
        drawing_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x + player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + 50 < width: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + 50 < height: # down
            player.y += player_vel

main()
    
