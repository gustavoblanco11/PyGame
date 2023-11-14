# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:52:24 2023

@author: gusta
"""
import pygame
import os
from MazeTest import *

pygame.init()

import pyamaze
from pyamaze import maze 
from pyamaze import agent
from queue import PriorityQueue

def on_maze_solved():
    main_menu()
    print("Maze solved! Do something here.")

def pymaze():
    global m
    m = maze(10,10)
    m.CreateMaze()
    
    xinit = m.rows #swtiching x and y values !!
    yinit = m.cols
    beginposition = (m.rows, m.cols)
    robtot = {}
    gtotal = {}
    for eachvalue in m.grid:
        gtotal[eachvalue] = 89898989
    gtotal[beginposition] = 0 
    ftotal = {}
    for eachvalue1 in m.grid:
        ftotal[eachvalue1] = 89898989 
    htotalinitial = abs(xinit-1) + abs(yinit-1) #goal position is (1,1)   
    ftotal[beginposition] = htotalinitial + gtotal[beginposition]
    priototal = PriorityQueue() 
    priototal.put(((htotalinitial+0),htotalinitial,beginposition))
    
    while not priototal.empty():
        postot = priototal.get()[2]
        #print ('current pos:', postot)
        if postot == (1,1):
            break
        
        for direction in 'NSEW':
            if m.maze_map[postot][direction] == True: #with
                if direction == 'N':
                    posfinal = (postot[0]-1, postot[1])
                if direction == 'S':
                    posfinal = (postot[0]+1, postot[1])
                if direction == 'E':
                    posfinal = (postot[0], postot[1]+1)
                if direction == 'W':
                    posfinal = (postot[0], postot[1]-1)
    
                posfinaltotal = list(posfinal)           
                htotalnew = abs(posfinaltotal[0] - 1) + abs(posfinaltotal[1] - 1)
                newgtotal = gtotal[postot] + 1
                #print ('newgtotal:', newgtotal)
                newftotal = newgtotal + htotalnew
                #print ('newftotal:', newftotal)
                        
                if newftotal < ftotal[posfinal]:
                    gtotal[posfinal] = newgtotal
                    ftotal[posfinal] = newftotal
                    priototal.put((newftotal, htotalnew, posfinal))
                    robtot[posfinal] = postot
                    #print ('robot movement:', robtot)
    
    robfinal = {}
    goalcell = (1,1)
    while goalcell != beginposition:
        robfinal[robtot[goalcell]] = goalcell
        goalcell = robtot[goalcell]
    #print ('robot final:', robfinal)
    
    robot = agent(m)
    mainplayer = agent(m, color='red', shape='arrow')
    m.tracePath({robot:robfinal})
    m.enableArrowKey(mainplayer)
    
    m.run()


def main_menu():
    S_Width = 800
    S_Height = 600
    game_surface = pygame.Surface(RES)
    screen = pygame.display.set_mode((S_Width, S_Height))
    frame_folder = r'C:\Users\gusta\Desktop\Fall 2023\Programming\PyGame\Stick figure'
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
    
    current_frame = 0
    # background = pygame.image.load('controllerbackground.png')
    # Load the idle PNG
    idle_path = os.path.join(frame_folder, 'Idle.png')
    idle_frame = pygame.image.load(idle_path)
    # Resize the idle frame to the same size as the animated frames
    idle_frame = pygame.transform.scale(idle_frame, (200 // 4, 300 // 4))
    stick = idle_frame.get_rect()
    framey = idle_frame
    StickWidth = 20
    StickHeight = S_Height // 2
    # background = pygame.transform.scale(background, (S_Width, S_Height))
    # screen.fill((255, 255, 255))
    menu_font = pygame.font.SysFont('Impact', 50)
    epic_title = menu_font.render("Everything in Python is an OBJECT", True, (0, 0, 0))
    quest_subtitle = menu_font.render("Even this maze is an object", True, (0, 0, 0))
    
    title_rect = epic_title.get_rect(center=(S_Width // 2, S_Height // 6))
    subtitle_rect = quest_subtitle.get_rect(center=(S_Width // 2, S_Height // 4))
    # stickrect = stick.get_rect(center=(S_Width // 2, S_Height // 2))

    start_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5, 200, 50)
    quit_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5 + 70, 200, 50)
    move = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    move = True
                    # return  # Exit the main menu function to start the game
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
        
        screen.fill((255, 255, 255))
        # screen.blit(background, (0, 0))
        screen.blit(epic_title, title_rect)
        screen.blit(quest_subtitle, subtitle_rect)
        stick.center = StickWidth, StickHeight

        # screen.blit(stick)
        
        pygame.draw.rect(screen, (255, 0, 0), start_button)
        start_text = menu_font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button.center)  # Center the text on the button
        screen.blit(start_text, start_text_rect)
        
        pygame.draw.rect(screen, (0, 255, 0), quit_button)
        quit_text = menu_font.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=quit_button.center)  # Center the text on the button
        screen.blit(quit_text, quit_text_rect)
        
        screen.blit(framey, stick)
        
        if move:
            stick = frames[current_frame].get_rect()
            framey= frames[current_frame]
            current_frame = (current_frame + 1) % len(frames)  # Switch to the next frame
            StickWidth += 0.5
            stick.center = StickWidth, StickHeight
        else:
            framey = idle_frame
        if StickWidth == S_Width:
            return
        pygame.display.update()

def game_loop():
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
    
    
    game_surface = pygame.Surface(RES)
    surface = pygame.display.set_mode((WIDTH + 300, HEIGHT))
    
    S_Width = 800  # screen width in pixels
    S_Height = 600
    
    screen = pygame.display.set_mode((S_Width, S_Height))
    
    frame_folder = r'C:\Users\gusta\Desktop\Fall 2023\Programming\PyGame\Stick figure'
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
    bg_game = pygame.image.load('White_background.png').convert()
    bg = pygame.image.load('bg_main.jpg').convert()
    
    font = pygame.font.SysFont('Impact', 150)
    
    player.center = TILE // 2, TILE // 2
    direction = (0,0)
    moving = False
    left = False
    level = 1
    y = False
    while run:
        speed = 10
        surface.blit(bg, (WIDTH, 0))
        surface.blit(game_surface, (0, 0))
        screen.fill((255, 255, 255))
        game_surface = screen
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        # screen.fill((255, 255, 255))
    
        if eat_food():
            #new level
            # maze = generate_maze()
            # player.center = TILE // 2, TILE // 2
            # walls_collide_list = sum([cell.get_rects() for cell in maze], [])
            # y = True
            run = False
            pygame.quit()
            pymaze()
    
        if y:
            start_text = font.render("Level 2", True, (0, 255, 255))
            start_text_rect = start_text.get_rect(center=(S_Width // 2, S_Height // 4))
            screen.blit(start_text, start_text_rect)
    
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not is_collide(-speed, 0):
            player.move_ip(-speed, 0)
            direction = -speed, 0
            moving = True
            left = True
        elif key[pygame.K_RIGHT] and not is_collide(speed, 0):
            player.move_ip(speed, 0)
            direction = speed, 0
            moving = True
            left = False
        elif key[pygame.K_UP] and not is_collide(0, -speed):
            player.move_ip(0, -speed)
            direction = 0, -speed
            moving = True
    
        elif key[pygame.K_DOWN] and not is_collide(0, speed):
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

main_menu()
game_loop()    
pygame.quit()