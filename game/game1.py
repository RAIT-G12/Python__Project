

import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('Chubs.mp3')
pygame.mixer.music.play()
pygame.init()


# Colors
brown = (153 ,76 ,0)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
dblue=(0,102,102)
grey =(128,128,128)
orange=(255,128,0)
venom=(0,153,76)
# Creating window
screen_width = 600
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))


bgimg = pygame.image.load("snake1.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha() 

bgimg1 = pygame.image.load("gover.jpg")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()

bgimg2 = pygame.image.load("ground2.jpg")
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30 )


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        gameWindow.blit(bgimg, (0, 0))
        text_screen("*****Welcome to Snakes World*****", white, 135, 250)
        text_screen("------------Press Space Bar To Play-------------", red, 100, 450)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                

                if event.key == pygame.K_SPACE:
                    
                    gameloop()
        pygame.display.update()
        clock.tick(30)                

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(10, screen_width/2)
    food_y = random.randint(10, screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 20
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg1, (0, 0))
            
            text_screen("Game Over! Press Enter To Continue",dblue , 110, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('Chubs.mp3')
                        pygame.mixer.music.play()
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:
                
                score +=10
                food_x = random.randint(10, screen_width/2)
                food_y = random.randint(10, screen_height/2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(brown)
            gameWindow.blit(bgimg2, (0, 0))
            
            text_screen("Score: " + str(score) + "                                                       High score: "+str(hiscore), white,20, 20)
            pygame.draw.rect(gameWindow, orange, [food_x, food_y,snake_size/1.4,snake_size/1.4])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('govver.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('govver.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()