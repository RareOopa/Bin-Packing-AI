import pygame
from items_module import Item

speed = 6
reached_destination = False


def move_item(item, target_x, target_y, screen):
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

    pygame.draw.rect(screen, item.color, item)


def bin_packing_backtracking(items, bin_capacity, screen):
    def backtracking_util(current_bin, items):
        nonlocal best_solution, best_num_bins

        if not items:
            # All items have been packed
            if current_bin < best_num_bins:
                best_num_bins = current_bin
                best_solution.clear()
                best_solution.update(bin_assignment)
            return

        for a_bin in bin_capacity:
            if a_bin.height >= items[0].width:  # Check item size instead of item value
                # Try placing the item in the current bin
                a_bin.height -= items[0].width
                bin_assignment[items[0].index] = (a_bin.index, items[0].width)
                move_item(items[0], a_bin.rect.x, a_bin.rect.y, screen)

                backtracking_util(current_bin + 1, items[1:])

                # Backtrack
                a_bin.height += items[0].width
                bin_assignment.pop(items[0].index, None)  # Use pop to avoid KeyError

    # Initialization
    best_solution = {}
    best_num_bins = float('inf')
    bin_assignment = {}

    backtracking_util(0, items)

    # Animate the movement of items to the target bins
    for item_index, (bin_index, size) in best_solution.items():
        item = items[item_index - 1]
        target_bin = bin_capacity[bin_index]
        move_item(item, target_bin.rect.x, target_bin.rect.y, screen)

    # Wait for the final animation to finish
    pygame.display.flip()
    pygame.time.wait(1000)

    # Reset item positions and dimensions
    for item in items:
        item.x = 100  # Adjust this value based on your layout
        item.width, item.height = 20, item.width

    # Return the actual number of bins used and the items in each bin
    return best_solution, len(set(location for location, size in best_solution.values()))
