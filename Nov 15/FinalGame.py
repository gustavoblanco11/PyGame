import pygame
import sys
import os
from pyamaze import maze 
from pyamaze import agent
from queue import PriorityQueue

resolution = (800,600)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,50)

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
    if robfinal == goalcell:
        print("finished")
    robot = agent(m)
    mainplayer = agent(m, color='red', shape='arrow')
    m.tracePath({robot:robfinal})
    m.enableArrowKey(mainplayer)
    
    m.run()

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
        desired_width = 200 // 2
        desired_height = 300 // 2
        frame = pygame.transform.scale(frame, (desired_width, desired_height))
        frames.append(frame)
        leftframe = pygame.transform.flip(frame, True, False)
        leftframes.append(leftframe)
    
    current_frame = 0
    sleep_frame = 0
    sleep_folder = r'C:\Users\gusta\Desktop\Fall 2023\Programming\PyGame\Stick figure\sleeping'
    sleeps = []
    for i in range(1, 5):
        sleep_path = os.path.join(sleep_folder, f'Sleeping{i}.png')
        sleep = pygame.image.load(sleep_path)
        desired_width = 200 // 1.5
        desired_height = 300 // 1.5
        sleep = pygame.transform.scale(sleep, (desired_width, desired_height))
        sleeps.append(sleep)
    
    stick = sleeps[sleep_frame].get_rect()
    framey= sleeps[sleep_frame]
    
    StickWidth = 50
    StickHeight = S_Height // 2
    
    menu_font = pygame.font.SysFont('Impact', 50)
    title = menu_font.render("Is this maze an object?", True, (0, 0, 0))
    
    title_rect = title.get_rect(center=(S_Width // 2, S_Height // 6))

    start_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5, 200, 50)
    quit_button = pygame.Rect(S_Width // 2 - 100, S_Height // 1.5 + 70, 200, 50)
    move = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    move = True

                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    run = False
        
        screen.fill((255, 255, 255))
        screen.blit(title, title_rect)
        stick.center = StickWidth, StickHeight
        
        pygame.draw.rect(screen, (0, 255, 0), start_button)
        start_text = menu_font.render("Yes", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button.center)  # Center the text on the button
        screen.blit(start_text, start_text_rect)
        
        pygame.draw.rect(screen, (255, 0, 0), quit_button)
        quit_text = menu_font.render("No", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=quit_button.center)  # Center the text on the button
        screen.blit(quit_text, quit_text_rect)
        
        screen.blit(framey, stick)
        
        if move:
            stick = frames[current_frame].get_rect()
            framey= frames[current_frame]
            current_frame = (current_frame + 1) % len(frames)  # Change to next frame
            StickWidth += 5
            stick.center = StickWidth, StickHeight
            pygame.time.Clock().tick(60)    #FPS
        else:
            stick = sleeps[sleep_frame].get_rect()
            framey= sleeps[sleep_frame]
            sleep_frame = (sleep_frame + 1) % len(frames)
            pygame.time.Clock().tick(5)    
        if StickWidth == S_Width:
            return
        pygame.display.update()
        

def level1():
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
    
    #Load the idle image (stick standing)
    idle_path = os.path.join(frame_folder, 'Idle.png')
    idle_frame = pygame.image.load(idle_path)
    idle_frame = pygame.transform.scale(idle_frame, (desired_width, desired_height))
    current_frame = 0
    player = frames[current_frame].get_rect()
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
    height = 675
    width = 675
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game !!!!!!!")
    
    square_size = 75
        
    food = pygame.image.load('food.png').convert_alpha()
    food = pygame.transform.scale(food, (square_size - 10, square_size - 10))
    foodrect = food.get_rect()
    foodrect.topleft = 7 * square_size, 7 * square_size
    
    finish = pygame.Rect(7*square_size, 3 * square_size, square_size, square_size)
    
    upgrade = False
    run = True
    speed = 5
    while run:
        if player.colliderect(foodrect):
            food = pygame.transform.scale(food, (0,0))
            upgrade = True
        if player.colliderect(finish):
        # Do something when the player reaches the finish line
            print("Player reached the finish line!")
            run = False
            level2()
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        playerx,playery = player.center
        key = pygame.key.get_pressed()
        
        new_player_rect = player.move(0, 0)
        if key[pygame.K_LEFT] and playerx > 0 and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x -= speed
            left = True
            moving = True
        elif key[pygame.K_RIGHT] and playerx < width and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x += speed
            moving = True
            left = False
        elif key[pygame.K_UP] and upgrade and playery > 0 and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y -= speed
            moving = True
        elif key[pygame.K_DOWN] and playery < height and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y += speed
            moving = True
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
        
        
        window.blit(food, foodrect)

        pygame.draw.rect(window, (0, 255, 0), finish)

        pygame.display.update()
        pygame.display.flip()

        pygame.time.Clock().tick(60)    #60=FPS
    
def level2():
    frame_folder = r'C:\Users\gusta\Desktop\Fall 2023\Programming\PyGame\Stick figure'
    #Load in the images to create a "gif" of sorts
    frames = []
    leftframes=[]
    for i in range(1, 5):
        frame_path = os.path.join(frame_folder, f'Running{i}.png')
        frame = pygame.image.load(frame_path)
        desired_width = 75 //2
        desired_height = 75 // 2
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
    moving = False
    left = False
    
    maze = [ 
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1,0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1,0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1,0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1,0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1,0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1,0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1,0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1,0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

        
    pygame.init()
    height = 750
    width = 750
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game !!!!!!!")
    
    square_size = 50
        
    food = pygame.image.load('food.png').convert_alpha()
    food = pygame.transform.scale(food, (square_size - 10, square_size - 10))
    foodrect = food.get_rect()
    foodrect.topleft = 1 * square_size, 4 * square_size
    
    tri = pygame.image.load('red_arrow.png').convert_alpha()
    tri = pygame.transform.scale(tri, (square_size - 10, square_size - 30))
    trirect = tri.get_rect()
    trirect.topleft = 1.15 * square_size, 1.25 * square_size
    
    finish = pygame.Rect(1*square_size, 1 * square_size, square_size, square_size)
    run = True
    speed = 5
    start = True
    while run:
        if start:
            player.topleft=(650, 700)
            start = False
        
        if player.colliderect(foodrect):
            food = pygame.transform.scale(food, (0,0))
            # run = False
            main_menu()
            # pygame.display.quit()
        if player.colliderect(finish):
            print("Player reached the finish line!")
            run = False
            pygame.display.quit()
            pymaze()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        playerx,playery = player.center
        px = playerx // square_size
        py = playery // square_size
        key = pygame.key.get_pressed()
        
        new_player_rect = player.move(0, 0)
        if key[pygame.K_LEFT] and playerx > 0 and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x -= speed
            left = True
            moving = True
        elif key[pygame.K_RIGHT] and playerx < width and maze[playery // square_size][playerx // square_size ] == 0:
            new_player_rect.x += speed
            moving = True
            left = False
        elif key[pygame.K_UP] and playery > 0 and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y -= speed
            moving = True
        elif key[pygame.K_DOWN] and playery < height and maze[playery // square_size ][playerx // square_size] == 0:
            new_player_rect.y += speed
            moving = True
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
        
            #this bellow is for level 2 !!!!!
        # pygame.draw.rect(window, (255, 255, 0), (1 * square_size, 4 * square_size, square_size, square_size))#yellow  
        # pygame.draw.rect(window, (0, 255, 0), (1 * square_size, 1 * square_size, square_size, square_size)) #green
        pygame.draw.rect(window, (0, 0, 255), (5 * square_size, 1 * square_size, square_size, square_size)) #blue
        pygame.draw.rect(window, (0, 0, 255), (6 * square_size, 8 * square_size, square_size, square_size)) #blue
        
        if (px == 0 and py == 3):
            px = 12
            playerx = px*square_size
            py = 13
            playery = py*square_size
            player.topleft=(playerx, playery)
            
        if (px == 4 and py == 0):
             px = 5
             playerx = px*square_size
             py = 7
             playery = py*square_size
             player.topleft=(playerx, playery)
        
        if player.colliderect(foodrect):
            # food = pygame.transform.scale(food, (0,0))
            player.topleft=(650, 700)   #Trap
        if player.colliderect((5 * square_size, 1 * square_size, square_size, square_size)):
            # food = pygame.transform.scale(food, (0,0))
            player.topleft=(6 * square_size, 8 * square_size)   #Trap 2    
        if player.colliderect(trirect):
        # Do something when the player reaches the finish line
            print("Player reached the finish line!")
            run = False
            pymaze()
            return
        
        window.blit(food, foodrect)

        # pygame.draw.rect(window, (0, 255, 0), finish)
        window.blit(tri, trirect)

        pygame.display.update()
        pygame.display.flip()

        pygame.time.Clock().tick(60)    #60=FPS


main_menu()
level1()
pygame.quit()
sys.exit()
