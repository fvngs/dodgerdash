import pygame
import random
from player import Player
from obstacle import Obstacle
import constants

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dodger Dash")

clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.SysFont(None, constants.FONT_SIZE)

player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT - constants.PLAYER_HEIGHT - 10, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT, constants.PLAYER_SPEED)
obstacles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.move("left")
    if keys[pygame.K_RIGHT] and player.x < constants.SCREEN_WIDTH - player.width:
        player.move("right")

    if random.randint(1, constants.OBSTACLE_FREQUENCY) == 1:
        obstacles.append(Obstacle.create_random(constants.SCREEN_WIDTH, constants.OBSTACLE_WIDTH, constants.OBSTACLE_HEIGHT, constants.OBSTACLE_SPEED))

    for obstacle in obstacles[:]:
        obstacle.move()
        if obstacle.is_off_screen(constants.SCREEN_HEIGHT):
            obstacles.remove(obstacle)
        elif obstacle.has_collided(player):
            running = False

    score += 1

    screen.fill(constants.WHITE)
    player.draw(screen, constants.BLACK)
    for obstacle in obstacles:
        obstacle.draw(screen, constants.RED)
    text = font.render("Score: " + str(score), True, constants.BLACK)
    screen.blit(text, [10, 10])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
