# perform_game_of_life_iteration

    Purpose

    The purpose of this function is to iterate over each cell in the given map, updating its state based on the current rules for a game of Life.
    Parameters

    ## `perform_game_of_life_iteration` Function

### Parameters

*   `old_map`: The current state of the game board map. This parameter represents a 2D list where each cell in the list is either `0` (dead) or `1` (alive).
*   Description: Updates the given game board map based on the current rules for a game of Life.
*   Usage constraints:
    *   The input `old_map` should be a valid 2D list representing the current state of the game board.

### Return Value

None
Description: This function modifies the input `old_map` in-place, thus it does not return any value.
    Returns

    ```python
def perform_game_of_life_iteration(map: list[list[int]]) -> list[list[int]]:
    """
    Iterates over each cell in the given map, updating its state based on the current rules for a game of Life.

    Args:
        map (list[list[int]]): A 2D list representing the game board, where 0 represents empty cells and 1 represents living cells.

    Returns:
        list[list[int]]: The updated game board after each iteration.
    """

    # Check if the input map is a square (i.e., all rows have the same number of columns)
    if not all(len(row) == len(map[0]) for row in map):
        raise ValueError("Input map must be a square")

    # Initialize an empty list to store the updated game board
    new_map = [[cell for cell in row] for row in map]

    # Iterate over each cell in the input map
    for i in range(len(map)):
        for j in range(len(map[0])):
            # Count the number of living neighbors for the current cell
            live_neighbors = 0
            for x in range(max(0, i-1), min(i+2, len(map))):
                for y in range(max(0, j-1), min(j+2, len(map[0]))):
                    if (x, y) != (i, j) and map[x][y] == 1:
                        live_neighbors += 1

            # Apply the rules of the game of Life to update the current cell's state
            if map[i][j] == 1:  # Cell is alive
                new_map[i][j] = 1 if live_neighbors in [2, 3] else 0  # Survival or reproduction based on neighbor counts

    return new_map
```
    Examples

    ```python
# Basic usage
def perform_game_of_life_iteration(grid):
    """
    Performs one iteration of the Game of Life on a given grid.

    Args:
        grid (list[list[int]]): A 2D list representing the grid, where each cell is either 0 (dead) or 1 (alive).

    Returns:
        None
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a copy of the original grid to store the next generation
    next_grid = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    
    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Count the number of alive neighbors
            alive_neighbors = 0
            for r in range(max(0, row-1), min(rows, row+2)):
                for c in range(max(0, col-1), min(cols, col+2)):
                    if (r != row or c != col) and grid[r][c] == 1:
                        alive_neighbors += 1
            
            # Apply the rules of the Game of Life
            if grid[row][col] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                next_grid[row][col] = 0
            elif grid[row][col] == 0 and alive_neighbors == 3:
                next_grid[row][col] = 1
    
    # Update the original grid with the next generation
    grid[:] = next_grid

# Edge case: Grid with a single cell
def perform_game_of_life_iteration_single_cell(grid):
    """
    Performs one iteration of the Game of Life on a given grid containing a single cell.

    Args:
        grid (list[list[int]]): A 2D list representing the grid, where each cell is either 0 (dead) or 1 (alive).

    Returns:
        None
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a copy of the original grid to store the next generation
    next_grid = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    
    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Count the number of alive neighbors
            alive_neighbors = 0
            for r in range(max(0, row-1), min(rows, row+2)):
                for c in range(max(0, col-1), min(cols, col+2)):
                    if (r != row or c != col) and grid[r][c] == 1:
                        alive_neighbors += 1
            
            # Apply the rules of the Game of Life
            if grid[row][col] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                next_grid[row][col] = 0
            elif grid[row][col] == 0 and alive_neighbors == 3:
                next_grid[row][col] = 1
    
    # Update the original grid with the next generation
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = next_grid[row][col]

# Advanced scenario: Two-player game
def perform_game_of_life_iteration_two_player(grid):
    """
    Performs two iterations of the Game of Life on a given grid.

    Args:
        grid (list[list[int]]): A 2D list representing the grid, where each cell is either 0 (dead) or 1 (alive).

    Returns:
        None
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a copy of the original grid to store the next generation for player 1
    player_1_next_grid = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    
    # Iterate over each cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Count the number of alive neighbors for player 1
            alive_neighbors = 0
            for r in range(max(0, row-1), min(rows, row+2)):
                for c in range(max(0, col-1), min(cols, col+2)):
                    if (r != row or c != col) and grid[r][c] == 1:
                        alive_neighbors += 1
            
            # Apply the rules of the Game of Life for player 1
            if grid[row][col] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                player_1_next_grid[row][col] = 0
            elif grid[row][col] == 0 and alive_neighbors == 3:
                player_1_next_grid[row][col] = 1
    
    # Update the original grid with the next generation for player 1
    grid[:] = player_1_next_grid

# Example usage (Basic usage)
grid = [[0,0,0],[0,1,0],[0,0,0]]
print("Original Grid:")
for row in grid:
    print(row)

perform_game_of_life_iteration(grid.copy())

# Edge case: Grid with a single cell
grid_single_cell = [[1]]
print("\nGrid with Single Cell:")
for row in grid_single_cell:
    print(row)

perform_game_of_life_iteration_single_cell(grid_single_cell.copy())

# Advanced scenario (Two-player game)
player_1_grid = [[0,0],[0,0]]
print("\nPlayer 1 Grid:")
for row in player_1_grid:
    print(row)

perform_game_of_life_iteration_two_player(player_1_grid.copy())
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """
    Performs an iteration of the Game of Life algorithm on the given level map.

    Creates a new level map based on the live_neighbor_count for each tile in the old map.
    If a cell has less than DEATH_LIMIT live neighbors, it dies and becomes an open space.
    Otherwise, it remains as a wall unless it is more than BIRTH_LIMIT alive neighbors.
    """
    new_map = [[False for i in range(WIDTH)] for j in range(HEIGHT)]
    # Loop over each row and column of the level_map
    for x in range(len(old_map)):
        for y in range(len(old_map[0])):
            live_neighbor_count = count_alive_neighbors(old_map, x, y)

            if old_map[x][y] is True:
                # See if it should die and become open
                if live_neighbor_count < DEATH_LIMIT:
                    new_map[x][y] = False
                # Otherwise keep it as a wall
                else:
                    new_map[x][y] = True
            # If the tile is currently empty
            else:
                # See if it should become a wall
                if live_neighbor_count > BIRTH_LIMIT:
                    new_map[x][y] = True
                else:
                    new_map[x][y] = False
    return new_map

Args:
    old_map (list of lists): The current level map, where each cell is either True (alive) or False (dead)

Returns:
    list of lists: The updated level map after the Game of Life iteration

Examples:
    >>> game_of_life_iteration([
    ...     [True, False, False],
    ...     [False, True, False],
    ...     [False, False, True]
    ... ])
    [[False, False, False], [False, True, False], [False, False, False]]
    >>> game_of_life_iteration([
    ...     [True, True, False],
    ...     [False, True, True],
    ...     [False, False, True]
    ... ])
    [[False, False, False], [False, True, True], [False, False, True]]"""
    ```