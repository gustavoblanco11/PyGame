# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:00:13 2023

@author: gusta
"""

import pygame

pygame.init()

S_Width = 800  # screen width in pixels
S_Height = 800

screen = pygame.display.set_mode((S_Width, S_Height))

# Load the Groot image
groot = pygame.image.load('bigGroot.png')

# Resize Groot to the desired size (e.g., 100x100 pixels)
desired_width = 200
desired_height = 300
groot = pygame.transform.scale(groot, (desired_width, desired_height))

player = groot.get_rect()
player.center = (S_Width // 2, S_Height // 2)  # Start Groot at the center of the screen

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    screen.blit(groot, player)      #blit = drawing Groot onto the background

    pygame.display.update()

pygame.quit()

