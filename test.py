import pygame
from bin_module import Bin
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bin Packing AI')
clock = pygame.time.Clock()

horz_rect = pygame.Rect(100, 200, 100, 30)
horz_rect2 = pygame.Rect(500, 300, 30, 100)
print (horz_rect.x, horz_rect.y)
target_x = 500
target_y = 300
speed = 6
num_of_bins = 10
bin_width = horz_rect.width
bin_margin = 5
bin_height = horz_rect.height * 2
start_x = SCREEN_WIDTH // 2
reached_destination = False


def move_item(item, target_x, target_y):
    global reached_destination
    if item.x < target_x:
        item.x += speed
        if item.x > target_x:
            item.x = target_x
    elif item.x > target_x:
        item.x -= speed
        if item.x < target_x:
            item.x = target_x

    if item.x == target_x:
        if item.y < target_y:
            item.y += speed
            if item.y > target_y:
                item.y = target_y
        elif item.y > target_y:
            item.y -= speed
            if item.y < target_y:
                item.y = target_y

    if item.x == target_x and not reached_destination:
        item.width, item.height = item.height, item.width
        reached_destination = True

    pygame.draw.rect(screen, (255, 0, 255), item)


run = True

while run:
    screen.fill((202, 228, 241))

    move_item(horz_rect, 500, 300)
    pygame.draw.rect(screen, (0, 0, 0), horz_rect2, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
