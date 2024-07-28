import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("fvngs/dodgerdash")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


player_width = 50
player_height = 60
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 7


obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []


clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.SysFont(None, 35)


def draw_player(x, y):
    pygame.draw.rect(screen, black, [x, y, player_width, player_height])


def draw_obstacles(obstacles_list):
    for obstacle in obstacles_list:
        pygame.draw.rect(screen, red, [obstacle[0], obstacle[1], obstacle_width, obstacle_height])


def display_score(count):
    text = font.render("Score: " + str(count), True, black)
    screen.blit(text, [10, 10])


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed


    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacles.append([obstacle_x, -obstacle_height])


    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]
    
    for obstacle in obstacles:
        if (player_y < obstacle[1] + obstacle_height and
                player_y + player_height > obstacle[1] and
                player_x < obstacle[0] + obstacle_width and
                player_x + player_width > obstacle[0]):
            running = False

    score += 1

    screen.fill(white)
    draw_player(player_x, player_y)
    draw_obstacles(obstacles)
    display_score(score)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
