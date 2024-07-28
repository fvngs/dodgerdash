import pygame
import random
from player import Player
from obstacle import Obstacle

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Dash")

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

player = Player(player_x, player_y, player_width, player_height, player_speed)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.move("left")
    if keys[pygame.K_RIGHT] and player.x < screen_width - player.width:
        player.move_right("right")

    if random.randint(1, obstacle_frequency) == 1:
        obstacles.append(Obstacle.create_random(screen_width, obstacle_width, obstacle_height, obstacle_speed))

    for obstacle in obstacles[:]:
        obstacle.move()
        if obstacle.is_off_screen(screen_height):
            obstacles.remove(obstacle)
        elif obstacle.has_collided(player):
            running = False

    score += 1

    screen.fill(white)
    player.draw(screen, black)
    for obstacle in obstacles:
        obstacle.draw(screen, red)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [10, 10])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
