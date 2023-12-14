import pygame
import sys
from input_box_module import InputBox
from items_module import Item
from button_module import Button

pygame.init()

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 785

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

inputBox_font = pygame.font.Font(None, 32)

# draw items
items = []
item_y_pos = 50
# draw items

input_box1 = InputBox(30, 685, 140, 32, inputBox_font)
input_box2 = InputBox(250, 685, 140, 32, inputBox_font)
input_box3 = InputBox(250, 685, 140, 32, inputBox_font)

def on_button_press():
    global num_items, size_items
    num_items = int(input_box1.text)
    size_items = list(map(int, input_box2.text.split()))

button = Button(30, 725, 100, 32, (0, 255, 0), "Create", inputBox_font, on_button_press)

num_items, size_items = 0, []

run = True

while run:
    screen.fill((255, 255, 255, 255))

    input_box1.update()
    input_box1.draw(screen)
    input_box2.update()
    input_box2.draw(screen)

    button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        input_box1.handle_event(event)
        input_box2.handle_event(event)
        button.handle_event(event)

    items = []
    if num_items > 0 and len(size_items) == num_items:
        items = [Item(i, item_y_pos + i * 30, num_items, size_items[i]) for i in range(min(num_items, 21))]

    for item in items:
        pygame.draw.rect(screen, item.color, item.rect)
        screen.blit(item.label, item.text_rect.topleft)

    pygame.display.update()

pygame.quit()
sys.exit()
