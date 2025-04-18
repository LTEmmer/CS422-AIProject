# perform_game_of_life_iteration

    Purpose

    This function takes an existing map representing a game of life grid and generates a new map based on the rules of the game of life, which involves counting the number of alive neighbors for each cell and updating the cell's state accordingly. The function updates the new map by determining whether cells should be alive or dead based on their current state and the number of live neighbors around them.
    Parameters

    This function performs a single iteration of Conway's Game of Life on an existing map representation of the game grid. The function updates the state of each cell based on its current state and the number of live neighbors around it according to the standard rules of the game.

### Parameters

- `old_map (list of lists of bool)`: 
  - **Description**: A 2D list where each element is a boolean representing whether the corresponding cell in the grid is alive (`True`) or dead (`False`).
  - **Usage Constraints**: The `old_map` should be a square matrix, i.e., all rows and columns have the same length.
    Returns

    ```python
def perform_game_of_life_iteration(map):
    """
    Update a game of life map based on the rules of Conway's Game of Life.

    This function takes a 2D list `map` representing the current state of a grid where each cell can be alive (1) or dead (0). It applies the following rules to determine the new state for each cell:

    - A live cell with fewer than two live neighbors dies.
    - A live cell with exactly two live neighbors survives.
    - A live cell with more than three live neighbors dies.
    - A dead cell with exactly three live neighbors becomes alive.

    The function returns a new 2D list representing the updated game of life map.

    Returns:
        list: A 2D list representing the updated state of the game of life grid.

    Special Cases:
        - If the input map is empty, an empty list is returned.
        - If the input map has no live cells (0), the function returns a map with all dead cells (0).
    """
    # Implementation of the game of life iteration logic
```

### Description
The `perform_game_of_life_iteration` function processes a given 2D grid representing a cell state in a game of life. It updates each cell's state based on its current state and the number of live neighbors it has according to the rules of Conway's Game of Life. The function returns a new map reflecting these changes.

### Return Type
The function returns a `list` of lists (2D list) where each inner list represents a row in the grid, and each element within an inner list is either `0` or `1`, indicating whether a cell is alive (`1`) or dead (`0`).

### Special Cases
- If the input map is empty, the function returns an empty list.
- If there are no live cells (i.e., all elements in the grid are `0`), the function also returns a map with all dead cells, maintaining consistency and avoiding potential errors during further processing.
    Examples

    ### Basic Usage

The `perform_game_of_life_iteration` function is used to simulate one generation in a Conway's Game of Life. It takes a 2D list `board` representing the current state of the game, where each cell can be either alive (1) or dead (0). The function updates the board according to the rules of the Game of Life.

```python
# Explanation: This example demonstrates the basic usage of perform_game_of_life_iteration.
# It initializes a 3x3 board with some live and dead cells, then simulates one iteration.
from game_of_life import perform_game_of_life_iteration

# Initialize the board
board = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

# Perform one iteration of the Game of Life
perform_game_of_life_iteration(board)

# Print the updated board after one iteration
print(board)
```

### Edge Case

This example shows how to handle a scenario where there are no live cells on the board. The `perform_game_of_life_iteration` function should not modify such a board, and it should return it unchanged.

```python
# Explanation: This example tests an edge case where all cells on the board are dead.
# The function should leave the board unmodified in this scenario.
from game_of_life import perform_game_of_life_iteration

# Initialize a 3x3 board with no live cells
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform one iteration of the Game of Life
perform_game_of_life_iteration(board)

# Print the unchanged board
print(board)
```

### Advanced Scenario

This example demonstrates a more complex scenario where the board has live cells that will remain alive or die based on multiple iterations. The function should simulate several generations to observe changes.

```python
# Explanation: This example shows an advanced scenario with multiple iterations of the Game of Life.
# It simulates five iterations and prints the updated board after each iteration.
from game_of_life import perform_game_of_life_iteration

# Initialize a 4x4 board with some live and dead cells
board = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# Simulate five iterations of the Game of Life
for _ in range(5):
    perform_game_of_life_iteration(board)
    print("Iteration", _ + 1)
    print(board)
```

These examples demonstrate basic usage, an edge case, and an advanced scenario for using the `perform_game_of_life_iteration` function in a Conway's Game of Life simulation.
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """
    Updates the current state of a 2D grid representing a Game of Life map based on the rules:
    
    - A living cell with fewer than DEATH_LIMIT live neighbors dies.
    - A dead cell with more than BIRTH_LIMIT live neighbors becomes alive.
    - Otherwise, the cell's state remains unchanged.

    Parameters:
        old_map (list of list of bool): The current state of the Game of Life grid.

    Returns:
        list of list of bool: The updated state of the Game of Life grid after one iteration.

    Examples:
        >>> perform_game_of_life_iteration([[True, False], [False, True]])
        [[False, False], [False, False]]

        >>> perform_game_of_life_iteration([[True, True], [False, False]])
        [[False, False], [True, True]]
    """
    new_map = [[False for i in range(WIDTH)] for j in range(HEIGHT)]

    for x in range(len(old_map)):
        for y in range(len(old_map[0])):
            live_neighbor_count = count_alive_neighbors(old_map, x, y)

            if old_map[x][y]:
                if live_neighbor_count < DEATH_LIMIT:
                    new_map[x][y] = False
                else:
                    new_map[x][y] = True
            else:
                if live_neighbor_count > BIRTH_LIMIT:
                    new_map[x][y] = True
                else:
                    new_map[x][y] = False

    return new_map
```"""
    ```