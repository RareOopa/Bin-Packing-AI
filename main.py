import pygame
import sys
import math
from input_box_module import InputBox
from items_module import Item
from button_module import Button
from bin_module import Bin
from backtraking_module import bin_packing_backtracking

pygame.init()

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 785

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bin Packing AI', )
clock = pygame.time.Clock()

inputBox_font = pygame.font.Font(None, 32)

items = []
item_y_pos = 50

num_items_input = InputBox(50, 610, 140, 32, inputBox_font)
num_bins_input = InputBox(250, 610, 140, 32, inputBox_font)
bin_height_input = InputBox(450, 610, 140, 32, inputBox_font)
size_items_input = InputBox(650, 610, 140, 32, inputBox_font)

num_items, size_items = 0, []
start_x = SCREEN_WIDTH // 2
start_y = 30
bin_height = 0
num_of_bins = 0
bin_width = 20
bin_margin = 10


def create_items_and_bins():
    global num_items, size_items, start_x, start_y, bin_height, num_of_bins, bins
    num_items = int(num_items_input.text)if num_items_input.text.isdigit() else 0
    size_items = list(map(int, size_items_input.text.split()))if num_items_input.text.isdigit() else 0
    num_of_bins = int(num_bins_input.text) if num_bins_input.text.isdigit() else 0
    bin_height = int(bin_height_input.text) if bin_height_input.text.isdigit() else 0


def backtrack_solve():
    bin_capacity = [bin_height] * num_of_bins

    solution, num_used_bins = bin_packing_backtracking(size_items, bin_capacity, num_of_bins)

    # Print used bins and their items
    print("Used Bins:")
    for bin_index in range(num_used_bins):
        bin_items = [size for item, (location, size) in solution.items() if location == bin_index]
        print(f"Bin {bin_index}: {bin_items}")

    # Print the number of used bins
    if num_used_bins <= 0:
        print("You can't fit it all!")
    else:
        print("Number of Bins Used:", num_used_bins)


def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return text, textRect


start_img = pygame.image.load('./assets/start_btn.png')
solve_backtrack_button = pygame.image.load('./assets/solve_backtrack_btn.png')

create_button = Button(50, 650, start_img, create_items_and_bins, 0.8)
solve_backtrack_button = Button(650, 650, solve_backtrack_button, backtrack_solve, 0.8)

num_items_text = set_text("Number of Items", 100, 595, 20)
num_of_bins_text = set_text("Number of Bins", 300, 595, 20)
bin_height_text = set_text("Bins Capacity", 500, 595, 20)
size_items_text = set_text("Size of Items", 700, 595, 20)

run = True

while run:
    screen.fill((202, 228, 241))

    num_items_input.update()
    num_items_input.draw(screen)

    size_items_input.update()
    size_items_input.draw(screen)

    num_bins_input.update()
    num_bins_input.draw(screen)

    bin_height_input.update()
    bin_height_input.draw(screen)

    create_button.draw(screen)
    solve_backtrack_button.draw(screen)

    screen.blit(num_items_text[0], num_items_text[1])
    screen.blit(size_items_text[0], size_items_text[1])
    screen.blit(num_of_bins_text[0], num_of_bins_text[1])
    screen.blit(bin_height_text[0], bin_height_text[1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        num_items_input.handle_event(event)
        size_items_input.handle_event(event)
        num_bins_input.handle_event(event)
        bin_height_input.handle_event(event)
        if len(size_items) > 0 and bin_height > 0 and num_of_bins > 0:
            create_button.handle_event(event)
            solve_backtrack_button.handle_event(event)

    items = []
    if 0 < num_items == len(size_items):
        items = [Item(i, 100, item_y_pos + i * 30, num_items, size_items[i]) for i in range(min(num_items, 21))]

    for item in items:
        pygame.draw.rect(screen, item.color, item.rect)
        screen.blit(item.label, item.text_rect.topleft)

    bins = []
    for row in range(math.ceil(num_of_bins / 25)):
        for col in range(min(num_of_bins - (row * 25), 25)):
            bins.append(
                Bin(start_x + (col * (bin_width + bin_margin)), 50 + row * (bin_height + bin_margin), 20, bin_height, 0,
                    (0, 0, 0)))

    for a_bin in bins:
        a_bin.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
