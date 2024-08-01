import pygame
import random
from player import Player
from obstacle import Obstacle
import constants
import json

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dodger Dash")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, constants.FONT_SIZE)

def load_high_score():
    try:
        with open('high_score.json', 'r') as file:
            return json.load(file).get("high_score", 0)
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open('high_score.json', 'w') as file:
        json.dump({"high_score": score}, file)

def game_loop():
    running = True
    score = 0
    level = 1
    high_score = load_high_score()
    player = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT - constants.PLAYER_HEIGHT - 10, constants.PLAYER_WIDTH, constants.PLAYER_HEIGHT, constants.PLAYER_SPEED)
    obstacles = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.move("left")
        if keys[pygame.K_RIGHT] and player.x < constants.SCREEN_WIDTH - player.width:
            player.move("right")

        level = score // 1000 + 1
        adjusted_frequency = max(1, constants.OBSTACLE_FREQUENCY - (score // 200))

        if random.randint(1, adjusted_frequency) == 1:
            new_obstacle = Obstacle.create_random(constants.SCREEN_WIDTH, constants.OBSTACLE_WIDTH, constants.OBSTACLE_HEIGHT, constants.OBSTACLE_SPEED + level - 1)
            if not any(obstacle.intersects(new_obstacle) for obstacle in obstacles):
                obstacles.append(new_obstacle)

        for obstacle in obstacles[:]:
            obstacle.move()
            if obstacle.is_off_screen(constants.SCREEN_HEIGHT):
                obstacles.remove(obstacle)
            elif obstacle.has_collided(player):
                if score > high_score:
                    save_high_score(score)
                return show_loss_screen(score)

        score += 1

        screen.fill(constants.WHITE)
        player.draw(screen, constants.BLACK)
        for obstacle in obstacles:
            obstacle.draw(screen, constants.RED)
        score_text = font.render("Score: " + str(score), True, constants.BLACK)
        level_text = font.render("Level: " + str(level), True, constants.BLACK)
        high_score_text = font.render("High Score: " + str(high_score), True, constants.BLACK)
        screen.blit(score_text, [10, 10])
        screen.blit(level_text, [10, 40])
        screen.blit(high_score_text, [10, 70])

        pygame.display.flip()
        clock.tick(60)
    
    return False

def show_loss_screen(score):
    loss_screen = True
    high_score = load_high_score()
    while loss_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill(constants.WHITE)
        loss_text = font.render("You Lost!", True, constants.RED)
        score_text = font.render(f"Score: {score}", True, constants.BLACK)
        high_score_text = font.render(f"High Score: {high_score}", True, constants.BLACK)
        restart_text = font.render("Press R to Restart or Q to Quit", True, constants.BLACK)

        screen.blit(loss_text, (constants.SCREEN_WIDTH // 2 - loss_text.get_width() // 2, constants.SCREEN_HEIGHT // 3))
        screen.blit(score_text, (constants.SCREEN_WIDTH // 2 - score_text.get_width() // 2, constants.SCREEN_HEIGHT // 3 + 50))
        screen.blit(high_score_text, (constants.SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, constants.SCREEN_HEIGHT // 3 + 100))
        screen.blit(restart_text, (constants.SCREEN_WIDTH // 2 - restart_text.get_width() // 2, constants.SCREEN_HEIGHT // 3 + 150))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        if keys[pygame.K_q]:
            return False

        pygame.display.flip()
        clock.tick(60)

    return False

def main():
    while True:
        if not game_loop():
            break

main()
pygame.quit()
