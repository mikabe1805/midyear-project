import pygame
import os
import time
import random

width = 750
height = 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Danganronpa Space Invaders")

# Loading our Images (Temporary. I'm going to be using Danganronpa Characters)
red_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
green_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
blue_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player Ship
yellow_space_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
red_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
green_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blue_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellow_lasers = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
# Test
background = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
    run = True
    fps = 60
    clock = pygame.time.Clock()

    while run == True:
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
