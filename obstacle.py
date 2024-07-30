import pygame
import random

class Obstacle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    @classmethod
    def create_random(cls, screen_width, obstacle_width, obstacle_height, speed):
        x = random.randint(0, screen_width - obstacle_width)
        return cls(x, -obstacle_height, obstacle_width, obstacle_height, speed)

    def move(self):
        self.y += self.speed

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, [self.x, self.y, self.width, self.height])

    def is_off_screen(self, screen_height):
        return self.y > screen_height

    def has_collided(self, player):
        return (self.y < player.y + player.height and
                self.y + self.height > player.y and
                self.x < player.x + player.width and
                self.x + self.width > player.x)

    def intersects(self, other):
        return not (self.x + self.width <= other.x or
                    self.x >= other.x + other.width or
                    self.y + self.height <= other.y or
                    self.y >= other.y + other.height)