import pygame


class Bin:
    def __init__(self, x, y, width, height, capacity, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.capacity = capacity
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
