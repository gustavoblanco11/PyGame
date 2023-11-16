# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:57:46 2023

@author: Fernando Lasso
"""
import pygame
import sys

maze = [ 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

pygame.init()

window = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Maze Game !!!!!!!")

square_size = 50
positionx = 12
positiony = 13

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and positiony < len(maze) - 1 and maze[positiony + 1][positionx] == 0:
        positiony = positiony + 1
    elif keys[pygame.K_LEFT] and positionx > 0 and maze[positiony][positionx - 1] == 0:
        positionx = positionx - 1
    elif keys[pygame.K_RIGHT] and positionx < len(maze[0]) - 1 and maze[positiony][positionx + 1] == 0:
        positionx = positionx + 1

    elif keys[pygame.K_UP] and positiony > 0 and maze[positiony - 1][positionx] == 0:
       positiony = positiony - 1
    
    print (positionx, positiony)

    window.fill((255,255,255))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(window, (0,0,0), (x * square_size, y * square_size, square_size, square_size))

    pygame.draw.rect(window, (255, 0, 0), (positionx * square_size, positiony * square_size, square_size, square_size))
    
    #this bellow is for level 2 !!!!!
    pygame.draw.rect(window, (255, 255, 0), (0 * square_size, 3 * square_size, square_size, square_size))
    pygame.draw.rect(window, (0, 255, 0), (0 * square_size, 0 * square_size, square_size, square_size))
    pygame.draw.rect(window, (0, 0, 255), (4 * square_size, 0 * square_size, square_size, square_size))
    pygame.draw.rect(window, (0, 0, 255), (5 * square_size, 7 * square_size, square_size, square_size))
    
    if (positionx == 0 and positiony == 3):
        positionx = 12
        positiony = 13
        
    if (positionx == 4 and positiony == 0):
         positionx = 5
         positiony = 7
    
    #bellow is original !!
    pygame.display.flip()
    pygame.time.Clock().tick(10)

  
    

pygame.quit()
sys.exit()