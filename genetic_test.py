import pygame
from bin_module import Bin
from items_module import Item
from button_module import Button

pygame.init()

screen = pygame.display.set_mode((800, 600))
num_of_bins = 2
speed = 6
reached_destination = False
run = True
clock = pygame.time.Clock()  # Correct initialization of clock

items = [Item(0, 50, 50, 4, 50), Item(1, 50, 100, 4, 100), Item(2, 50, 150, 4, 30), Item(3, 50,200, 4, 20)]
bins = [Bin(400, 50, 22, 100, (0, 0, 0), 0), Bin(450, 50, 22, 100, (0, 0, 0), 1)]
original_positions = {item.index: (item.x, item.y, item.width, item.height) for item in items}

def move_item(item, target_x, target_y):
    if not item.reached_destination:
        if item.x < target_x:
            item.x += speed
            if item.x > target_x:
                item.x = target_x
                item.y = target_y + item.width
                print(f"item.y{item.y},item.width{item.width}: target_y{target_y}")
                pygame.time.delay(200)
        elif item.x > target_x:
            item.x -= speed
            if item.x < target_x:
                item.x = target_x
                item.y = target_y + item.width
                print(f"item.y{item.y},item.width{item.width}: target_y{target_y}")
                pygame.time.delay(200)
        if item.y > target_y:
            item.y -= speed
            if item.y < target_y:
                item.y = target_y
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
            item.reached_destination = True

    pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))
    screen.blit(item.label_size, ((item.x + item.width // 2) - item.label_size.get_width() // 2,
                                  item.y + item.height // 2 - item.label_size.get_height() // 2))
    return item.reached_destination


def reset_item(item, original_position):
    item.x, item.y, item.width, item.height = original_position



def genetic_solve():
    pass


solve_img = pygame.image.load('assets/solve_btn.png')
solve_backtrack_button = Button(0, 400, solve_img, genetic_solve, 0.8)
while run:
    screen.fill((255, 255, 255))

    solve_backtrack_button.draw(screen)

    for item in items:
        pygame.draw.rect(screen, item.color, (item.x, item.y, item.width, item.height))
        screen.blit(item.label_size,
                    ((item.x + item.width // 2) - item.label_size.get_width() // 2,
                     item.y + item.height // 2 - item.label_size.get_height() // 2))

    for a_bin in bins:
        a_bin.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        solve_backtrack_button.handle_event(event)

    pygame.display.update()

pygame.quit()