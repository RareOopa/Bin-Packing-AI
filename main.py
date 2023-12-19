import pygame
import sys
import math
from input_box_module import InputBox
from items_module import Item
from button_module import Button
from menu_button_module import MenuBtn
from bin_module import Bin
from backtraking_module import bin_packing_backtracking

pygame.init()

SCREEN_WIDTH = 1530
SCREEN_HEIGHT = 785
MID_WIDTH = SCREEN_WIDTH / 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bin Packing AI', )
clock = pygame.time.Clock()

items = []
bins = []
item_y_pos = 50
num_items, size_items = 0, []
start_x = SCREEN_WIDTH // 2
start_y = 30
bin_height = 0
num_of_bins = 0
bin_width = 20
bin_margin = 10


def create_items_and_bins():
    global num_items, size_items, start_x, start_y, bin_height, num_of_bins, bins
    num_items = int(num_items_input.text) if num_items_input.text.isdigit() else 0
    size_items = list(map(int, size_items_input.text.split())) if num_items_input.text.isdigit() else []
    num_of_bins = int(num_bins_input.text) if num_bins_input.text.isdigit() else 0
    bin_height = int(bin_height_input.text) if bin_height_input.text.isdigit() else 0


def backtrack_solve():
    solution, num_used_bins = bin_packing_backtracking(items, bins, screen)

    print("Used Bins:")
    for bin_index, bin_capacity in enumerate(bins):
        bin_items = [size for item, (location, size) in solution.items() if location == bin_index]
        print(f"Bin {bin_index}: {bin_items}")

    # Print the number of used bins
    if num_used_bins <= 0:
        print("You can't fit it all!")
    else:
        print("Number of Bins Used:", num_used_bins)


def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return text, textRect


def get_font(size):
    return pygame.font.Font("assets/ka1.ttf", size)


inputBox_font = pygame.font.Font(None, 32)
start_img = pygame.image.load('./assets/start_btn.png')
solve_backtrack_img = pygame.image.load('./assets/solve_backtrack_btn.png')
backtrack_back_img = pygame.image.load('assets/back_btn.png')

num_items_input = InputBox(50, 610, 140, 32, inputBox_font)
num_bins_input = InputBox(250, 610, 140, 32, inputBox_font)
bin_height_input = InputBox(450, 610, 140, 32, inputBox_font)

size_items_input = InputBox(650, 610, 140, 32, inputBox_font)

create_button = Button(50, 650, start_img, create_items_and_bins, 0.8)

num_items_text = set_text("Number of Items", 100, 595, 20)
num_of_bins_text = set_text("Number of Bins", 300, 595, 20)
bin_height_text = set_text("Bins Capacity", 500, 595, 20)
size_items_text = set_text("Size of Items", 700, 595, 20)

background_img = pygame.image.load("assets/background.jpg")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
genetic_solve_img = pygame.image.load("assets/genetic_solve_menu_btn.png")
backtrack_solve_img = pygame.image.load("assets/backtrack_solve_menu_btn.png")
quit_image = pygame.image.load("assets/quit_menu_btn.png")


def main_menu():
    while True:
        screen.blit(background_img, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#873e23")
        MENU_RECT = MENU_TEXT.get_rect(center=(750, 100))

        genetic_solve_btn = MenuBtn(image=genetic_solve_img, pos=(750, 300),
                                    text_input=None, font=get_font(75), base_color="#d7fcd4", hovering_color="White",
                                    initial_scale=0.8, target_scale=0.9)
        backtrack_solve_btn = MenuBtn(image=pygame.image.load("assets/backtrack_solve_menu_btn.png"), pos=(750, 500),
                                      text_input=None, font=get_font(75), base_color="#d7fcd4",
                                      hovering_color="White", initial_scale=0.8, target_scale=0.9)
        exit_btn = MenuBtn(image=pygame.image.load("assets/exit_btn.png"), pos=(750, 670),
                           text_input=None, font=get_font(75), base_color="#d7fcd4", hovering_color="White",
                           initial_scale=0.85, target_scale=0.95)

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [genetic_solve_btn, backtrack_solve_btn, exit_btn]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if genetic_solve_btn.checkForInput(MENU_MOUSE_POS):
                    genetic_solve_screen()
                if backtrack_solve_btn.checkForInput(MENU_MOUSE_POS):
                    backtrack_solve_screen()
                if exit_btn.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


back_button = Button(1320, 650, backtrack_back_img, main_menu, 0.75)


def genetic_solve_screen():
    while True:
        GENETIC_SOLVE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        GENETIC_SOLVE_TEXT = get_font(45).render("This is the GENETIC_SOLVE screen.", True, "White")
        GENETIC_SOLVE_RECT = GENETIC_SOLVE_TEXT.get_rect(center=(MID_WIDTH, 260))
        screen.blit(GENETIC_SOLVE_TEXT, GENETIC_SOLVE_RECT)

        GENETIC_SOLVE_BACK = MenuBtn(image=quit_image, pos=(MID_WIDTH, 460),
                            text_input=None, font=get_font(75), base_color="White", hovering_color="Green",
                            initial_scale=1, target_scale=1)

        GENETIC_SOLVE_BACK.changeColor(GENETIC_SOLVE_MOUSE_POS)
        GENETIC_SOLVE_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GENETIC_SOLVE_BACK.checkForInput(GENETIC_SOLVE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def backtrack_solve_screen():
    solve_backtrack_button = Button(550, 650, solve_backtrack_img, backtrack_solve, 0.8)
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
        back_button.draw(screen)

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
            create_button.handle_event(event)
            solve_backtrack_button.handle_event(event)
            back_button.handle_event(event)

        items = []
        if 0 < num_items == len(size_items):
            items = [Item(i, 100, item_y_pos + i * 30, num_items, size_items[i]) for i in range(min(num_items, 21))]

        for item in items:
            pygame.draw.rect(screen, item.color, item.rect)
            screen.blit(item.label, item.text_rect.topleft)
            screen.blit(item.label_size, item.text_rect_size.center)

        bins = []
        idx = -1
        for row in range(math.ceil(num_of_bins / 25)):
            for col in range(min(num_of_bins - (row * 25), 25)):
                idx += 1
                bins.append(
                    Bin(start_x + (col * (bin_width + bin_margin)), 50 + row * (bin_height + bin_margin), 20,
                        bin_height,
                        (0, 0, 0), idx))

        for a_bin in bins:
            a_bin.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


main_menu()
