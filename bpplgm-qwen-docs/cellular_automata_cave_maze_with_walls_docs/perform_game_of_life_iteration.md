# perform_game_of_life_iteration

    Purpose

    This function simulates the rules of Conway's Game of Life on an existing map to generate a new map for the next iteration. It counts the number of live neighbors around each cell and updates the cell's state based on the rules (birth, survival, or death) of the game. The result is a new map that represents the next stage in the evolution of the cellular automaton.
    Parameters

    This function simulates one iteration of Conway's Game of Life on a given map. It takes a single argument:

- `old_map`: A 2D list representing the current state of the cellular automaton. Each cell in this list can be either 'L' for live (1) or 'D' for dead (0).

The function processes each cell in the `old_map` and updates its state based on the rules of the game:
- A live cell with fewer than two live neighbors dies.
- A live cell with two or three live neighbors survives.
- A live cell with more than three live neighbors dies.
- A dead cell with exactly three live neighbors becomes a live cell.

The function returns a new 2D list `new_map` that represents the updated state of the cellular automaton after one iteration.
    Returns

    **Function: `perform_game_of_life_iteration`**

- **Purpose**: This function simulates the rules of Conway's Game of Life on an existing map to generate a new map for the next iteration. It counts the number of live neighbors around each cell and updates the cell's state based on the rules (birth, survival, or death) of the game.
- **Return type**: The function returns a `List[List[int]]`, which represents the new map after applying the Game of Life rules to the current map.
- **Description**:
  - For each cell in the current map:
    - Count the number of live neighbors (cells with value `1`).
    - If a cell is alive (`current_map[i][j] == 1`):
      - Apply the survival rule: Cell survives if it has exactly 2 or 3 live neighbors.
      - Otherwise, apply the death rule: Cell dies due to underpopulation or overcrowding.
    - If a cell is dead (`current_map[i][j] == 0`):
      - Apply the birth rule: Cell comes alive if it has exactly 3 live neighbors.
  - The function generates a new map based on these rules and returns it.
- **Special cases**:
  - If there are no live cells in the current map, the function should return a new map with all cells dead (`[0] * len(current_map) for _ in range(len(current_map))`).
  - The function assumes that the input `current_map` is well-formed and consists of lists of integers where each integer represents the state of a cell (0 for dead, 1 for alive).
    Examples

    ```python
# Basic usage: Demonstrates a simple iteration in the Game of Life.
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0]
]

result_board = perform_game_of_life_iteration(board)
print(result_board)
```

```python
# Edge case: An empty board should return an empty board.
empty_board = []
result_empty_board = perform_game_of_life_iteration(empty_board)
print(result_empty_board)  # Output: []

# Advanced scenario: Demonstrates the transition from a stable pattern to chaos.
chaotic_board = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

for _ in range(5):
    chaotic_board = perform_game_of_life_iteration(chaotic_board)
    print(chaotic_board)
```
These examples demonstrate the basic functionality of `perform_game_of_life_iteration` by iterating over a game board and applying the Game of Life rules. The first example shows how to use the function with a typical starting configuration. The second example handles an edge case where the input is an empty board. The third example illustrates the progression of a chaotic pattern through several iterations, showcasing how the function can simulate more complex behavior over time.
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """
    Iterates through the current game state (old_map) and updates the game to its next state according to the rules of Conway's Game of Life.

    Parameters:
        old_map (list): The current state of the game map, represented as a 2D list where True indicates a live cell and False indicates an open cell.

    Returns:
        list: The updated game state (new_map) after one iteration of the Game of Life rules.
    """
    new_map = [[False for i in range(WIDTH)] for j in range(HEIGHT)]

    # Loop over each row and column in the old_map
    for x in range(len(old_map)):
        for y in range(len(old_map[0])):
            live_neighbor_count = count_alive_neighbors(old_map, x, y)

            if old_map[x][y]:
                # Check if the cell should die (underpopulation)
                if live_neighbor_count < DEATH_LIMIT:
                    new_map[x][y] = False
                else:
                    new_map[x][y] = True
            else:
                # Check if the cell should be born (overcrowding)
                if live_neighbor_count > BIRTH_LIMIT:
                    new_map[x][y] = True

    return new_map

# Example usage:
# Define constants WIDTH, HEIGHT, DEATH_LIMIT, and BIRTH_LIMIT as necessary for your specific use case
# old_map = [[True, False, True], [False, True, False], [True, True, True]]
# new_map = perform_game_of_life_iteration(old_map)
```

This function updates the state of a game map according to the rules of Conway's Game of Life. The function takes a 2D list `old_map` as input, representing the current state of the game, and returns a new 2D list `new_map` representing the next state. The function iterates over each cell in the old map, counts its alive neighbors, and applies the rules to determine if the cell should become live or die."""
    ```