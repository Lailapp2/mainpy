import pygame

class Ball:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.radius = 25
        self.color = (255, 0, 0)
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, dx, dy):
        if self.radius <= self.x + dx <= self.screen_width - self.radius:
            self.x += dx
        if self.radius <= self.y + dy <= self.screen_height - self.radius:
            self.y += dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)