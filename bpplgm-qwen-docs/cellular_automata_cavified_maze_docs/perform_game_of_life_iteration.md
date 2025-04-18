# perform_game_of_life_iteration

    Purpose

    This function implements the rules of Conway's Game of Life, updating an existing game map based on the number of live neighbors each cell has. It creates a new map by iterating over each tile in the current map and determining whether it should remain open or become a wall based on the specified death and birth limits.
    Parameters

    ```python
def perform_game_of_life_iteration(old_map):
    """
    This function implements the rules of Conway's Game of Life to update an existing game map.

    Parameters:
    old_map (list): A 2D list representing the current state of the game board. Each cell in the board can be either '1' (open) or '0' (wall).

    Returns:
    list: A new 2D list representing the updated state of the game board after applying Conway's Game of Life rules.
    """

# Example usage:
old_map = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 0]
]

new_map = perform_game_of_life_iteration(old_map)
print(new_map)
```

**Explanation:**
The function `perform_game_of_life_iteration` takes a 2D list `old_map` as input, which represents the current state of a game board. Each cell in the board is represented by either '1' (open) or '0' (wall). The function iterates over each cell in the `old_map`, counts the number of live neighbors (cells with value '1') around it, and then determines whether the cell should remain open ('1') or become a wall ('0') based on the specified death and birth limits. This process is used to update the game board according to the rules of Conway's Game of Life, which govern how cells come alive or die in response to their neighbor counts. The function returns a new 2D list representing the updated game board state.
    Returns

    The `perform_game_of_life_iteration` function returns a new map that represents the state of Conway's Game of Life after applying the rules to each cell in the current game map. The function iterates over each cell, counts its live neighbors, and then determines if the cell should remain open or become a wall based on predefined death and birth limits. Here is how the function operates:

- **Return Type**: `list[list[int]]`
  - This indicates that the function returns a new game map, which is a 2D list of integers representing different states (open or closed).

- **Description**:
  - The function processes each cell in the current game map.
  - For each cell, it calculates the number of live neighbors it has. A live neighbor is considered any adjacent cell that is currently open (represented by the value 1).
  - Based on this count, the function decides whether to keep the cell open or close it:
    - If a cell has more than the death limit (`death_limit`), it becomes closed.
    - If a cell has fewer than the birth limit (`birth_limit`), it becomes open.

- **Special Cases**:
  - The function handles edge cases, such as cells on the border of the map where some neighbors are out of bounds. In these cases, the function assumes the neighboring cells are not live.
  - The death and birth limits are used to determine when a cell should change its state, ensuring that the rules of Conway's Game of Life are applied correctly.

Here is an example usage of the `perform_game_of_life_iteration` function:

```python
# Example input game map: [[1, 0], [1, 1]]
current_map = [
    [1, 0],
    [1, 1]
]

# Death limit: 2, Birth limit: 3
death_limit = 2
birth_limit = 3

# Perform the iteration to get the new game map
new_map = perform_game_of_life_iteration(current_map, death_limit, birth_limit)

# Output the new game map
print(new_map)
```

In this example, the `perform_game_of_life_iteration` function will iterate over each cell in the `current_map`, count its live neighbors, and apply the rules to determine if it should remain open or close. The resulting `new_map` will be printed, showing the updated state of the game map after one iteration.
    Examples

    ```python
# Basic usage: Simulate a simple game of life iteration on a 3x3 grid with initial conditions.
# This function takes a 2D list representing the current state of the grid and returns the new state after one iteration.
grid = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
new_grid = perform_game_of_life_iteration(grid)
print(new_grid)  # Expected output: [[0, 1, 0], [1, 0, 1], [0, 1, 1]]

# Edge case: A single cell in the middle of a grid that is surrounded by other cells.
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
new_grid = perform_game_of_life_iteration(grid)
print(new_grid)  # Expected output: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

# Advanced scenario: A more complex grid with cells that can survive indefinitely due to their pattern.
grid = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
new_grid = perform_game_of_life_iteration(grid)
print(new_grid)  # Expected output: [[1, 1, 0], [0, 1, 0], [0, 0, 1]]  # The grid remains unchanged as the cells survive indefinitely.
```
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """Perform one iteration of Conway's Game of Life based on the current state of the old map.

    Args:
        old_map (list): A 2D list representing the grid of cells in the game, where `True` indicates a live cell and `False` indicates an open cell.

    Returns:
        list: A new 2D list representing the updated grid after one iteration of the Game of Life rules.

    Examples:
        # Initial state
        old_map = [
            [True, False, True],
            [False, True, False],
            [True, False, True]
        ]

        # New state after one iteration
        new_map = perform_game_of_life_iteration(old_map)
        print(new_map)
        # Output: [[True, False, True], [False, False, False], [True, False, True]]
    """
```
Note: The `WIDTH` and `HEIGHT`, as well as the `DEATH_LIMIT` and `BIRTH_LIMIT`, are assumed to be defined elsewhere in the code or should be provided by the caller."""
    ```