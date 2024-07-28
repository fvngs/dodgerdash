import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        else:
            self.x += self.speed
        

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, [self.x, self.y, self.width, self.height])
