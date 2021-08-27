import pygame
import random
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

 
width = 500
height = 500
 
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_size = 10
snake_speed = 15

font = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 15)
 
def score(score):
    score = score_font.render("Score: " + str(score), True, white)
    window.blit(score, [0, 0])
 
def snake(snake_size, snake_list):
    for i in snake_list:
        pygame.draw.rect(window, green, [i[0], i[1], snake_size, snake_size])
 
def message(msg, color):
    mes = font.render(msg, True, color)
    window.blit(mes, [200, 250])
 
def game():
    over = False
    close = False
 
    x = width / 2
    y = height / 2
 
    x_change = 0
    y_change = 0
 
    snake_List = []
    snake_length = 1
 
    foodx = random.randrange(0, width)
    foody = random.randrange(0, height)
 
    while True:
 
        while close == True:
            window.fill(black)
            message("GAME OVER!", red)
            score(snake_length - 1)
            pygame.display.update()
 
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0
 
        if x >= width or x < 0 or y >= height or y < 0:
            close = True
        x += x_change
        y += y_change
        
        window.fill(black)
        pygame.draw.rect(window, white, (foodx, foody, snake_size, snake_size))

        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_length:
            del snake_List[0]
 
        for i in snake_List[:-1]:
            if i == snake_Head:
                close = True
 
        snake(snake_size, snake_List)
        score(snake_length - 1)
 
        pygame.display.update()
 
        if x == foodx and y == foody:
            foodx = random.randrange(0, width)
            foody = random.randrange(0, height)
            snake_length += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
game()



