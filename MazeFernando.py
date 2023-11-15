# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:55:30 2023

@author: gusta
"""
import pygame
import sys
import os

resolution = (800,600)

def main_menu():
    pygame.init()
    S_Width = 800
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
        



def game():
    frame_folder = r'C:\Users\gusta\Desktop\Fall 2023\Programming\PyGame\Stick figure'
    #Load in the images to create a "gif" of sorts
    frames = []
    leftframes=[]
    for i in range(1, 5):
        frame_path = os.path.join(frame_folder, f'Running{i}.png')
        frame = pygame.image.load(frame_path)
        desired_width = 100 //2
        desired_height = 100 // 2
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
    # player.center = 75, 75
    moving = False
    left = False
    
    maze = [ 
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    pygame.init()
    # screen.fill(255,255,255)
    height = 675
    width = 675
    window = pygame.display.set_mode((675, 675))
    pygame.display.set_caption("Maze Game !!!!!!!")
    
    square_size = 75
        
    food = pygame.image.load('food.png').convert_alpha()
    food = pygame.transform.scale(food, (square_size - 10, square_size - 10))
    foodrect = food.get_rect()
    foodrect.topleft = 7 * square_size, 7 * square_size
    # window.blit(food, foodrect)
    def upgrade():
        if player.collidepoint(foodrect.center):
            return True
        return False
    run = True
    speed = 5
    while run:
        window.blit(food, foodrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        playerx,playery = player.center
        
        key = pygame.key.get_pressed()
        
        new_player_rect = player.move(0, 0)

        if key[pygame.K_a] and playerx > 0 and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x -= speed
            left = True
            moving = True
        elif key[pygame.K_d] and playerx < width and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x += speed
            moving = True
            left = False
        elif key[pygame.K_w] and upgrade and playery > 0 and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y -= speed
            moving = True
            left = False
        elif key[pygame.K_s] and playery < height and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y += speed
            moving = True
            left = False
        else:
            moving = False
        
        # Check for collision with walls
        collision = False
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == 1:
                    wall_rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
                    if new_player_rect.colliderect(wall_rect):
                        collision = True
                        break
        
        if not collision:
            player = new_player_rect
                
        
        window.fill((255,255,255))
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == 1:
                    pygame.draw.rect(window, (0,0,0), (x * square_size, y * square_size, square_size, square_size))
        
        if moving:
            current_frame = (current_frame + 1) % len(frames)  # Switch to the next frame
            if left:
                window.blit(leftframes[current_frame], player)  #Running left
            else:    
                window.blit(frames[current_frame], player)  # Running right
        else:
            window.blit(idle_frame, player)  # Show the idle png when not moving
            
        pygame.display.update()
        pygame.display.flip()

        pygame.time.Clock().tick(60)

main_menu()
game()
pygame.quit()
sys.exit()
