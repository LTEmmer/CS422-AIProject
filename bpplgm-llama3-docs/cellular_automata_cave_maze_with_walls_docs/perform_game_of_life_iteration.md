# perform_game_of_life_iteration

    Purpose

    ## Purpose of the Code

The `perform_game_of_life_iteration` function takes an existing 2D map representing a game of Life and iteratively updates it according to the rules of Conway's Game of Life, updating dead cells with walls and alive cells without walls.

## Functionality Documentation

### Parameters

*   `old_map`: A 2D list representing the current state of the game of Life.
*   `WIDTH` and `HEIGHT`: Constants representing the width and height of the game board (not defined in this snippet).

### Loop Structure

The function iterates over each cell in the input map, updating its status based on the presence or absence of live neighbors.

#### Iteration Steps

1.  It counts the number of alive neighbors for a given cell.
2.  Based on the cell's current state and neighbor count, it determines whether to update the cell's status (dead → open wall; alive → alive).

### Return Value

The function returns the updated `new_map` representing the next state of the game.

### Notes

*   The function assumes a rectangular grid with `WIDTH` rows and `HEIGHT` columns.
*   The `count_alive_neighbors` function is not defined in this snippet, but it's assumed to be implemented elsewhere.
    Parameters

    ```python
def perform_game_of_life_iteration(old_map: list[list[int]], WIDTH: int, HEIGHT: int) -> list[list[int]]:
    """
    Iteratively updates a 2D map representing Conway's Game of Life based on its current state.

    Args:
        old_map (list[list[int]]): The current state of the game of Life.
        WIDTH (int): The width of the game board in pixels.
        HEIGHT (int): The height of the game board in pixels.

    Returns:
        list[list[int]]: The updated map representing the next state of the game.

    Notes:
        This function assumes a rectangular grid with `WIDTH` rows and `HEIGHT` columns.
        It counts the number of alive neighbors for each cell, updating its status accordingly.

    Examples:

    >>> old_map = [
    ...     [0, 1, 0],
    ...     [0, 1, 0],
    ...     [0, 0, 0]
    ... ]
    >>> perform_game_of_life_iteration(old_map, WIDTH=5, HEIGHT=5)
    [[0, 1, 0, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]
    """

    # Define the function parameters with Google-style documentation
    def count_alive_neighbors(cell: list[int]) -> int:
        """
        Counts the number of alive neighbors for a given cell.

        Args:
            cell (list[int]): The current state of the game of Life cell.

        Returns:
            int: The number of alive neighbors.
        """
        # This function is assumed to be implemented elsewhere and should not be modified
        raise NotImplementedError("Count_alive_neighbors must be implemented")

    # Define the loop structure with Google-style documentation
    for y in range(HEIGHT):
        for x in range(WIDTH):
            cell = old_map[y][x]
            alive_neighbors = count_alive_neighbors(cell)
            if cell == 1 and (alive_neighbors < 2 or alive_neighbors > 3):  # underpopulation or overpopulation
                new_cell = 0  # open wall
            elif cell == 1 and alive_neighbors == 3:  # stable
                new_cell = 1  # alive
            else:
                new_cell = cell  # alive

            old_map[y][x] = new_cell

    return old_map
```
    Returns

    ```python
def perform_game_of_life_iteration(old_map: list[list[str]], WIDTH: int, HEIGHT: int) -> list[list[str]]:
    """
    Iteratively updates a 2D game of Life map according to Conway's Game of Life rules.

    Args:
        old_map (list[list[str]]): The current state of the game of Life.
        WIDTH (int): The width of the game board.
        HEIGHT (int): The height of the game board.

    Returns:
        list[list[str]]: The updated 2D map representing the next state of the game.

    Notes:
        This function assumes a rectangular grid with WIDTH rows and HEIGHT columns.
    """
    # Count the number of alive neighbors for each cell
    def count_alive_neighbors(cell):
        """Returns the number of alive neighbors for a given cell."""
        # Special cases for border cells
        if (cell[0] == 0 or cell[1] == 0) and old_map[cell][cell] != 'W':
            return 3
        elif cell[0] >= WIDTH or cell[1] >= HEIGHT:
            return 2
        else:
            # Count live neighbors for adjacent cells
            alive_neighbors = 0
            for x, y in [(cell-1, cell), (cell+1, cell), (cell-1, y+1), (cell+1, y)]:
                if 0 <= x < WIDTH and 0 <= y < HEIGHT and old_map[x][y] == 'L':
                    alive_neighbors += 1
            return alive_neighbors

    # Iterate over each cell in the input map
    new_map = [[('W' if (cell[0] == 0 or cell[1] == 0) and count_alive_neighbors(cell) == 3 else cell) for cell in old_map]
    
    return new_map
```

```python
def perform_game_of_life_iteration(old_map: list[list[str]], WIDTH: int, HEIGHT: int) -> list[list[str]]:
    """
    Iteratively updates a 2D game of Life map according to Conway's Game of Life rules.

    Args:
        old_map (list[list[str]]): The current state of the game of Life.
        WIDTH (int): The width of the game board.
        HEIGHT (int): The height of the game board.

    Returns:
        list[list[str]]: The updated 2D map representing the next state of the game.

    Notes:
        This function assumes a rectangular grid with WIDTH rows and HEIGHT columns.
    """
    # Count the number of alive neighbors for each cell
    def count_alive_neighbors(cell):
        """Returns the number of alive neighbors for a given cell."""
        # Special cases for border cells
        if (cell[0] == 0 or cell[1] == 0) and old_map[cell][cell] != 'W':
            return 3
        elif cell[0] >= WIDTH or cell[1] >= HEIGHT:
            return 2
        else:
            # Count live neighbors for adjacent cells
            alive_neighbors = 0
            for x, y in [(cell-1, cell), (cell+1, cell), (cell-1, y+1), (cell+1, y)]:
                if 0 <= x < WIDTH and 0 <= y < HEIGHT and old_map[x][y] == 'L':
                    alive_neighbors += 1
            return alive_neighbors

    # Iterate over each cell in the input map
    new_map = [[('W' if (cell[0] == 0 or cell[1] == 0) and count_alive_neighbors(cell) == 3 else cell) for cell in old_map]
    
    return new_map
```
    Examples

    ```python
# Basic usage
def perform_game_of_life_iteration(board):
    """Simulate one iteration of the Game of Life.

    Args:
        board (list): A 2D list representing the game board, where True represents a live cell and False represents a dead cell.
            The outer square is considered alive, while the inner square is considered dead.
    """
    rows, cols = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r < 0 or r >= rows) or (c < 0 or c >= cols) or board[r][c]:
                    continue
                live_neighbors += 1
            
            # Apply the rules of the Game of Life
            if board[row][col] and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = False
            elif not board[row][col] and live_neighbors == 3:
                board[row][col] = True
    
    return board

# Edge case: A game board with a single cell that is alive but has only one live neighbor.
board = [
    [True],
    [False, False]
]

print(perform_game_of_life_iteration(board))
```
    Docstring

    """```python
def perform_game_of_life_iteration(old_map):
    """
    Performs a single iteration of the Game of Life on the given level map.

    Creates a new level map by checking each cell in the old map against its neighbors,
    determining whether it should be kept alive or die, and updating the new map accordingly.

    Args:
        old_map (list of lists): The current state of the game board.

    Returns:
        list of lists: A new representation of the game board with updated states.

    Examples:
        >>> old_map = [[True, True, False], [False, False, False], [True, False, False]]
        >>> new_map = perform_game_of_life_iteration(old_map)
        >>> print(new_map)
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

# Description of what this function currently does: Performs one iteration of the Game of Life on the given level map.
```

```python
"""
A simple implementation of a single Game of Life iteration.

This function takes an existing level map as input, updates it according to the rules of Conway's Game of Life,
and returns the updated map. The new map is also provided as output for reference.

Args:
    old_map (list of lists): The current state of the game board.

Returns:
    list of lists: A new representation of the game board with updated states.
"""
A one-line description

Args section with parameter details
-------------------------------
*   `old_map`: The current state of the game board.
    *   Type: `list of lists` (2D list)
    *   Description: The input level map.

Returns section with return value details
----------------------------------------
*   `new_map`: A new representation of the game board with updated states.
    *   Type: `list of lists` (2D list)
    *   Description: The output new game board."""
    ```