# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:45:14 2023

@author: gusta
"""
import pygame

pygame.init()

S_Width = 1500
S_Height = 800

screen = pygame.display.set_mode((S_Width, S_Height))

groot = pygame.image.load('Grooty.png')
desired_width = 150
desired_height = 150
groot = pygame.transform.scale(groot, (desired_width, desired_height))

# Raise the floor by increasing the floor_position value
floor_position = S_Height - 100  # Adjust the value as needed

player = groot.get_rect()
player.center = (S_Width // 13, floor_position - groot.get_height() // 2)  # Start Groot above the floor

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (S_Width, S_Height))

# Custom font for the main menu title
menu_font = pygame.font.Font('33713_SerpentineBoldItalic.ttf', 50)  # Replace 'your_font.ttf' with the path to your chosen font file

def main_menu():
    epic_title = menu_font.render("The Adventures of Groot", True, (0, 0, 0))
    quest_subtitle = menu_font.render("The quest for the Groot Norm", True, (0, 0, 0))
    
    title_rect = epic_title.get_rect(center=(S_Width // 2, S_Height // 4))
    subtitle_rect = quest_subtitle.get_rect(center=(S_Width // 2, S_Height // 2))

    start_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5, 200, 50)
    quit_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5 + 70, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return  # Exit the main menu function to start the game
                if quit_button.collidepoint(event.pos):
                    pygame.quit()

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(epic_title, title_rect)
        screen.blit(quest_subtitle, subtitle_rect)
        
        pygame.draw.rect(screen, (255, 0, 0), start_button)
        start_text = menu_font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button.center)  # Center the text on the button
        screen.blit(start_text, start_text_rect)
        
        pygame.draw.rect(screen, (0, 255, 0), quit_button)
        quit_text = menu_font.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=quit_button.center)  # Center the text on the button
        screen.blit(quit_text, quit_text_rect)
        
        pygame.display.update()

def game_loop():
    character_speed = 2
    gravity = 1
    jumping = False
    jump_strength = 120

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and not key[pygame.K_d]:
            player.move_ip(-character_speed, 0)
        elif key[pygame.K_d] and not key[pygame.K_a]:
            player.move_ip(character_speed, 0)

        if key[pygame.K_SPACE] and not key[pygame.K_s] and not jumping:
            jumping = True
            player.move_ip(0, -jump_strength)

        player.move_ip(0, gravity)  # Apply gravity

        # Check for collisions with the new floor position
        if player.y >= floor_position - player.height:
            jumping = False
            player.y = floor_position - player.height
        
        if player.x == S_Width:
            player.x = 0

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(groot, player)
        pygame.display.update()

main_menu()  # Start with the epic main menu
game_loop()  # Transition to the game loop when the player clicks "Start"
pygame.quit()
