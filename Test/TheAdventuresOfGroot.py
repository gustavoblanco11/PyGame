import pygame

pygame.init()       #Always needed to initialize pygame

S_Width = 1500      #Screen size in pixels
S_Height = 800

screen = pygame.display.set_mode((S_Width, S_Height))

groot = pygame.image.load('Grooty.png') #Uploading Groot avatar 
groot_width = 150                       #Groot size in bits
groot_height = 150
groot = pygame.transform.scale(groot, (groot_width, groot_height))  #Changes Groot into a usable entitity

floor = S_Height - 100  #Raise or lower the floor by increasing if needed

player = groot.get_rect()
player.center = (S_Width // 13, floor - groot.get_height() // 2)  #Start Groot above the floor

background = pygame.image.load('background.png')    #Uploading Super Mario background
background = pygame.transform.scale(background, (S_Width, S_Height))

# Custom font for the main menu title
title_font = pygame.font.Font('33713_SerpentineBoldItalic.ttf', 50)  #Uploading font and selecting size
sub_font = pygame.font.Font('33713_SerpentineBoldItalic.ttf', 40)

def main_menu():
    title = title_font.render("The Adventures of Groot", True, (0, 0, 0))        #Setting Title of game
    subtitle = sub_font.render("The quest for the Groot Norm", True, (0, 0, 0))    #Setting a subtitle for the game
    
    title_rect = title.get_rect(center=(S_Width // 2, S_Height // 4))
    subtitle_rect = subtitle.get_rect(center=(S_Width // 2, S_Height // 3))

    start_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5, 200, 50)
    quit_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5 + 70, 200, 50)

    while True:     #Always boots up and displays the main menu until Start or Quit button used
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:    #If mouse button if clicked
                if start_button.collidepoint(event.pos):    #Checks if start was clicked
                    return  
                if quit_button.collidepoint(event.pos):     #Checks if quit was clicked
                    pygame.quit()

        screen.fill((0, 0, 0))          #Setting the stage
        screen.blit(background, (0, 0))
        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)
        
        pygame.draw.rect(screen, (255, 0, 0), start_button)
        start_text = title_font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button.center)  #Drawing Start button and word "Start"
        screen.blit(start_text, start_text_rect)
        
        pygame.draw.rect(screen, (0, 255, 0), quit_button)
        quit_text = title_font.render("Quit", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=quit_button.center)  #Drawing Quit button and word "Quit"
        screen.blit(quit_text, quit_text_rect)
        
        pygame.display.update()

def game_loop():
    speed = 2
    gravity = 1
    jumping = False
    jump = 150

    run = True
    while run:              #Always must have a while loop with a variable that determines if the game is running or not
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #pygame.QUIT works by exiting the program that opens up
                run = False

        key = pygame.key.get_pressed()

        if key[pygame.K_a] and not key[pygame.K_d]:     #Setting up movement (left)
            player.move_ip(-speed, 0)
        elif key[pygame.K_d] and not key[pygame.K_a]:   #(right)
            player.move_ip(speed, 0)

        if (key[pygame.K_SPACE] or key[pygame.K_w]) and not key[pygame.K_s] and not jumping:    #Jump
            jumping = True
            player.move_ip(0, -jump)    #y axis is inverted

        player.move_ip(0, gravity)  #Apply gravity at all times

        if player.y >= floor - player.height:      #Makes sure that player never goes below the floor
            jumping = False
            player.y = floor - player.height
        
        if player.x == S_Width:     #Resets position if player reaches the end of the screen
            player.x = 0

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(groot, player)
        pygame.display.update()             #Refreshes the display; if not used, every moving object will leave an after image

main_menu()  # Game opens on main menu
game_loop()  # Transition from main menu to actual game
pygame.quit()   #pygame.quit() always needed!!!!!!!!!!!!!!!
