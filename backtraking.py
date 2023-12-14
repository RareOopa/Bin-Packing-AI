class BinPackingSolver:
    def __init__(self, bin_capacity):
        self.bin_capacity = bin_capacity
        self.best_solution = None

    def pack_items(self, items):
        self.best_solution = None
        self.backtrack([], items)
        return self.best_solution

    def backtrack(self, current_solution, remaining_items):
        if not remaining_items:
            if self.is_feasible(current_solution):
                self.update_best_solution(current_solution)
            return

        current_item = remaining_items[0]

        # Try placing the current item in each bin
        for i, bin_items in enumerate(current_solution):
            new_solution = current_solution[:]
            new_solution[i] = bin_items + [current_item]
            self.backtrack(new_solution, remaining_items[1:])

        # Try placing the current item in a new bin
        new_solution = current_solution + [[current_item]]
        self.backtrack(new_solution, remaining_items[1:])

    def is_feasible(self, solution):
        for bin_items in solution:
            if sum(bin_items) > self.bin_capacity:
                return False
        return True

    def update_best_solution(self, solution):
        if self.best_solution is None or len(solution) < len(self.best_solution):
            self.best_solution = solution


# Example usage with user input:
num_items = int(input("Enter the number of items: "))
items = [int(input(f"Enter the size of item {i + 1}: ")) for i in range(num_items)]

bin_capacity = int(input("Enter the capacity of each bin: "))

solver = BinPackingSolver(bin_capacity)
solution = solver.pack_items(items)

if solution:
    used_bins = len(solution)

    print(f"Used bins: {used_bins}")

    # Print the items in each bin
    for i, bin_items in enumerate(solution):
        print(f"Bin {i + 1}:", bin_items)
else:
    print("No available solutions.")