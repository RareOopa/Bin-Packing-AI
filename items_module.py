import pygame
import random

pygame.font.init()

class Item:
    item_font_size = 20
    item_font = pygame.font.Font(None, item_font_size)

    @staticmethod
    def generate_constant_colors(num_colors):
        return [
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(num_colors)
        ]

    def __init__(self, index, item_y_pos, num_items, size):
        self.index = index
        self.text = f"Item {index + 1}"
        self.label = Item.item_font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.label.get_rect(center=(50, item_y_pos + 10))
        self.rect = pygame.Rect(100, item_y_pos, size, 20)
        self.color = Item.CONSTANT_COLORS[index % num_items]


Item.CONSTANT_COLORS = Item.generate_constant_colors(9999)
