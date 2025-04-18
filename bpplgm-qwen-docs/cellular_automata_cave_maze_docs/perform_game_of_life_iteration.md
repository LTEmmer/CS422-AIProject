# perform_game_of_life_iteration

    Purpose

    The `perform_game_of_life_iteration` function takes an existing map (represented as a 2D list of boolean values where `True` indicates a "wall" and `False` indicates an "empty" cell) and simulates the next iteration of Conway's Game of Life rules. It determines the number of live neighbors for each tile in the current state and updates the new map based on these counts, applying the rules to determine whether each tile should remain empty, become a wall, or stay as it is.
    Parameters

    ### perform_game_of_life_iteration Function Documentation

**Function Purpose:**
The `perform_game_of_life_iteration` function takes an existing map (represented as a 2D list of boolean values where `True` indicates a "wall" and `False` indicates an "empty" cell) and simulates the next iteration of Conway's Game of Life rules. It determines the number of live neighbors for each tile in the current state and updates the new map based on these counts, applying the rules to determine whether each tile should remain empty, become a wall, or stay as it is.

**Parameters:**

1. **`old_map` (List[List[bool]])**
    - **Type:** List of lists containing boolean values.
    - **Description:** A 2D list representing the current state of the game board, where `True` indicates a "wall" and `False` indicates an "empty" cell.
    - **Usage Constraints:** The function assumes that `old_map` is a valid 2D list with dimensions (rows x columns) greater than or equal to 1. Each element in the 2D list must be either `True` or `False`.

**Examples:**

```python
# Example 1:
current_map = [
    [False, True, False],
    [True, True, True],
    [False, False, False]
]

new_map = perform_game_of_life_iteration(current_map)
print(new_map)

# Output:
# [[False, False, False], 
#  [True, True, True], 
#  [False, False, False]]
```

In this example, the `perform_game_of_life_iteration` function updates the map based on the rules of Conway's Game of Life. The first tile in the first row becomes a wall because it has three live neighbors (two walls and one empty cell), which triggers a wall formation rule.

```python
# Example 2:
current_map = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

new_map = perform_game_of_life_iteration(current_map)
print(new_map)

# Output:
# [[False, True, False], 
#  [False, False, False], 
#  [False, True, False]]
```

In this example, the middle tile in the first row becomes an empty cell because it has two live neighbors (one wall and one empty cell), which triggers a cell death rule.
    Returns

    ### perform_game_of_life_iteration Documentation

**Purpose**: The `perform_game_of_life_iteration` function simulates the next iteration of Conway's Game of Life rules on a given map. It updates the map based on the number of live neighbors for each tile.

**Return Type**: `List[List[bool]]`

**Description**: The function takes an existing 2D list of boolean values representing the current state of the game board, where `True` indicates a "wall" and `False` indicates an "empty" cell. It calculates the number of live neighbors for each tile (8 potential neighbors in a square grid) and updates the map according to the following rules:
- A cell becomes alive if it is currently empty (`False`) and has exactly 3 live neighbors.
- A cell remains alive if it is currently occupied (`True`) and has 2 or 3 live neighbors.
- All other cells die or remain unchanged.

**Special Cases**:
- If a tile is out of bounds (e.g., on the edge or corner), it is considered to have no live neighbors, regardless of its value in the current map.
- The function returns a new map that represents the updated state after one iteration of the Game of Life simulation.
    Examples

    ```python
# Basic usage: Perform one iteration of Conway's Game of Life on a 3x3 board.
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1]
]

# Apply the game logic to update the board
perform_game_of_life_iteration(board)

print("Updated Board:")
for row in board:
    print(row)
```

```python
# Edge case: A dead cell with exactly three live neighbors becomes a live cell (birth).
board = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]

# Apply the game logic to update the board
perform_game_of_life_iteration(board)

print("Updated Board:")
for row in board:
    print(row)
```

```python
# Advanced scenario: A live cell with more than three or less than two live neighbors dies.
board = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# Apply the game logic to update the board
perform_game_of_life_iteration(board)

print("Updated Board:")
for row in board:
    print(row)
```
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """
    Perform one iteration of the Game of Life on the given grid.

    Args:
        old_map (list of lists): A 2D list representing the current state of the game grid,
                                   where True represents a living cell and False represents an empty cell.

    Returns:
        list of lists: A new 2D list representing the updated state of the game grid after one iteration.
    """
    # Initialize the new map with all cells set to False (dead)
    new_map = [[False for _ in range(len(old_map[0]))] for _ in range(len(old_map))]

    # Loop over each cell in the old map
    for x in range(len(old_map)):
        for y in range(len(old_map[0])):
            live_neighbor_count = count_alive_neighbors(old_map, x, y)

            if old_map[x][y]:
                # Check if the cell should die or remain alive
                if live_neighbor_count < DEATH_LIMIT:
                    new_map[x][y] = False
                else:
                    new_map[x][y] = True
            else:
                # Check if the cell should be born
                if live_neighbor_count > BIRTH_LIMIT:
                    new_map[x][y] = True

    return new_map

# Example usage
WIDTH, HEIGHT = 5, 5  # Assuming WIDTH and HEIGHT are defined elsewhere
DEATH_LIMIT = 2
BIRTH_LIMIT = 3

initial_map = [
    [False, False, True, False, False],
    [True, True, False, True, True],
    [False, True, True, False, False],
    [True, False, False, False, True],
    [False, True, False, True, False]
]

updated_map = perform_game_of_life_iteration(initial_map)
for row in updated_map:
    print(row)
```

This function iterates over each cell in the provided `old_map` and determines its state for the next iteration based on the rules of the Game of Life. It calculates the number of live neighbors for each cell and updates the corresponding cell in the `new_map`. The example usage demonstrates how to call the function with an initial map and print the updated map after one iteration."""
    ```