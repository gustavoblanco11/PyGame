# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:19:52 2023

@author: gusta
"""
import pygame
import os
# from MazeTest import *

pygame.init()

S_Width = 700  # screen width in pixels
S_Height = 700

screen = pygame.display.set_mode((S_Width, S_Height))

frame_folder = r'C:\Users\Sidne\Documents\Python Scripts\PyGame\Maze\First Attempt'

#Load in the images to create a "gif" of sorts
frames = []
leftframes=[]
for i in range(1, 5):
    frame_path = os.path.join(frame_folder, f'Running{i}.png')
    frame = pygame.image.load(frame_path)
    desired_width = 200 // 4
    desired_height = 300 // 4
    frame = pygame.transform.scale(frame, (desired_width, desired_height))
    frames.append(frame)
    leftframe = pygame.transform.flip(frame, True, False)
    leftframes.append(leftframe)

# Load the idle PNG
idle_path = os.path.join(frame_folder, 'Idle.png')
idle_frame = pygame.image.load(idle_path)
# Resize the idle frame to the same size as the animated frames
idle_frame = pygame.transform.scale(idle_frame, (desired_width, desired_height))

current_frame = 0

player = frames[current_frame].get_rect()
player.center = (S_Width // 2, S_Height // 2)  # Start the animation at the center of the screen

clock = pygame.time.Clock()

run = True
moving = False  #Game begins with player still
while run:
    speed = 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-speed, 0)
        moving = True
        left = True
    elif key[pygame.K_d]:
        player.move_ip(speed, 0)
        moving = True
        left = False
    elif key[pygame.K_w]:
        player.move_ip(0, -speed)
        moving = True
    elif key[pygame.K_s]:
        player.move_ip(0, speed)
        moving = True
    else:
        moving = False

    if moving:
        if left:
            screen.blit(leftframes[current_frame], player)  #Running left
        else:    
            screen.blit(frames[current_frame], player)  # Running right
    else:
        screen.blit(idle_frame, player)  # Show the idle png when not moving

    
    pygame.display.update()

    if moving:
        current_frame = (current_frame + 1) % len(frames)  # Switch to the next frame
    clock.tick(13)  #Frame rate (13 frames per second)

pygame.quit()
