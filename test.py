def generate_combinations(objects, r, current_combination, start_index):
    """
    Recursively generates all combinations of 'r' objects from the 'objects' list.
    The order of elements in a combination does not matter.

    Args:
        objects (list): The list of distinct objects to choose from.
        r (int): The number of objects to select for each combination.
        current_combination (list): The list that stores the current combination being built.
        start_index (int): The index in the objects list to start the search from.
    """
    # Base Case: If the current combination has 'r' objects, we have found a valid combination.
    # Print it and return to the previous recursive call.
    if len(current_combination) == r:
        print("".join(current_combination))
        return

    # Recursive Step: Iterate through all available objects starting from 'start_index'.
    # This prevents duplicates and ensures the elements are always in ascending order
    # of their original index, effectively handling the "order does not matter" rule.
    for i in range(start_index, len(objects)):
        
        # --- Select the object ---
        obj = objects[i]
        current_combination.append(obj)

        # --- Recurse to find the next object ---
        # The recursive call now starts the search from the next index (i + 1)
        # to ensure we don't use the same object again or create reordered combinations.
        generate_combinations(objects, r, current_combination, i + 1)

        # --- Backtrack ---
        # After the recursive call returns, we "un-select" the current object
        # to allow other combinations to be formed.
        current_combination.pop()


# --- Initial Call (example) ---
# Your input distinct objects.
objects = ['A', 'B', 'C', 'D']
n = len(objects)

# The number of objects to choose at a time.
r = 2

# An empty list to build the current combination.
current_combination = []

# The starting index for the first recursive call.
start_index = 0

print(f"Generating all combinations of {n} objects taken {r} at a time from {objects}:\n")
generate_combinations(objects, r, current_combination, start_index)

# Example with a different r value
print("\n" + "="*30)
print("\nGenerating all combinations of 4 objects taken 3 at a time:")
objects_2 = ['A', 'B', 'C', 'D']
r_2 = 3
current_combination_2 = []
start_index_2 = 0
generate_combinations(objects_2, r_2, current_combination_2, start_index_2)
