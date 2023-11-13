# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:52:24 2023

@author: gusta
"""
import pygame
import os
from MazeTest import *

class Food:
    def __init__(self):
        self.img = pygame.image.load('food.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (TILE - 10, TILE - 10))
        self.rect = self.img.get_rect()
        self.set_pos()

    def set_pos(self):
        self.rect.topleft = randrange(cols) * TILE + 5, randrange(rows) * TILE + 5

    def draw(self):
        game_surface.blit(self.img, self.rect)

def is_collide(x, y):
    tmp_rect = player.move(x, y)
    if tmp_rect.collidelist(walls_collide_list) == -1:
        return False
    return True

def eat_food():
    for food in food_list:
        if player.collidepoint(food.rect.center):
            food.set_pos()
            return True
    return False

pygame.init()

game_surface = pygame.Surface(RES)
surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))

S_Width = 600  # screen width in pixels
S_Height = 600

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

clock = pygame.time.Clock()

run = True
moving = False  #Game begins with player still

# get maze
maze = generate_maze()

# food settings
food_list = [Food() for i in range(3)]

# collision list
walls_collide_list = sum([cell.get_rects() for cell in maze], [])

# images
bg_game = pygame.image.load('White background.jpg').convert()
# bg = pygame.image.load('bg_main.jpg').convert()

font = pygame.font.SysFont('Impact', 150)

player.center = TILE // 2, TILE // 2
direction = (0,0)
moving = False
left = False
level = 1
y = False
while run:
    speed = 10
    # surface.blit(bg, (WIDTH, 0))
    surface.blit(game_surface, (0, 0))
    screen.fill((255, 255, 255))
    game_surface = screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # screen.fill((255, 255, 255))

    if eat_food():
        #new level
        maze = generate_maze()
        player.center = TILE // 2, TILE // 2
        walls_collide_list = sum([cell.get_rects() for cell in maze], [])
        y = True

    if y:
        start_text = font.render("Level 2", True, (0, 255, 255))
        start_text_rect = start_text.get_rect(center=(S_Width // 2, S_Height // 4))
        screen.blit(start_text, start_text_rect)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and not is_collide(-speed, 0):
        player.move_ip(-speed, 0)
        direction = -speed, 0
        moving = True
        left = True
    elif key[pygame.K_d] and not is_collide(speed, 0):
        player.move_ip(speed, 0)
        direction = speed, 0
        moving = True
        left = False
    elif key[pygame.K_w] and not is_collide(0, -speed):
        player.move_ip(0, -speed)
        direction = 0, -speed
        moving = True

    elif key[pygame.K_s] and not is_collide(0, speed):
        direction = 0, speed
        player.move_ip(0, speed)
        moving = True

    else:
        moving = False


    if moving:
        if left:
            game_surface.blit(leftframes[current_frame], player)  #Running left
        else:    
            game_surface.blit(frames[current_frame], player)  # Running right
    else:
        game_surface.blit(idle_frame, player)  # Show the idle png when not moving

    # draw maze
    [cell.draw(game_surface) for cell in maze]
    
    [food.draw() for food in food_list]

    pygame.display.update()

    if moving:
        current_frame = (current_frame + 1) % len(frames)  # Switch to the next frame
    pygame.display.flip()
    clock.tick(13)  #Frame rate (13 frames per second)

pygame.quit()
