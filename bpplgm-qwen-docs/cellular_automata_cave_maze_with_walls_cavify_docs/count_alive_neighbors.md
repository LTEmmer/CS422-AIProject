# count_alive_neighbors

    Purpose

    This function counts the number of alive neighbors around a given point `(x, y)` on a game board represented as `live_map`, where each cell can be either `True` (alive) or `False` (dead). The function checks all eight possible neighbor positions and increments the count if the neighboring cell is alive.
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Count the number of alive neighbors around a given point (x, y) on a game board.

    Parameters:
        live_map (list of list of bool): A 2D grid where each cell is either True (alive)
            or False (dead). The grid represents the current state of the game.
        
        x (int): The x-coordinate of the point to check. Must be within the bounds of the
            live_map, i.e., 0 <= x < len(live_map).
        
        y (int): The y-coordinate of the point to check. Must be within the bounds of the
            live_map, i.e., 0 <= y < len(live_map[0]).

    Returns:
        int: The number of alive neighbors around the given point (x, y).

    Usage Constraints:
        - `live_map` must be a non-empty 2D list.
        - The coordinates `(x, y)` must not exceed the bounds of the live_map.
    """
    # Define possible neighbor offsets
    offsets = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]
    
    # Initialize count of alive neighbors
    alive_count = 0
    
    # Iterate over all possible neighbor offsets
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        
        # Check if the neighboring cell is within bounds and alive
        if (nx >= 0) and (ny >= 0) and (nx < len(live_map)) and (ny < len(live_map[0])) and live_map[nx][ny]:
            alive_count += 1
    
    return alive_count
```

This code snippet provides a function `count_alive_neighbors` that counts the number of living cells around a specified point on a game board. It takes three parameters: `live_map`, which is the game board represented as a 2D list where each cell can be either True or False, indicating whether it is alive or dead; `x` and `y`, which are the coordinates of the point to check within the game board. The function returns an integer representing the number of living neighbors around the specified point.
    Returns

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors around a given point (x, y) on a game board.

    Parameters:
        live_map (list of list of bool): A 2D list representing the game board,
                                         where each cell is either True (alive) or False (dead).
        x (int): The row index of the current point.
        y (int): The column index of the current point.

    Returns:
        int: The count of alive neighbors around the given point. It ranges from 0 to 8,
             considering all eight possible neighbor positions in a 3x3 grid centered at (x, y).

    Special Cases:
        - If x or y is out of bounds of live_map, it is considered as an invalid position.
          The function will return 0 for such cases.
        - An empty live_map is not allowed; it should contain at least one row and one column.

    Example Usage:
        board = [[False, True, False],
                 [True, True, True],
                 [False, False, False]]

        print(count_alive_neighbors(board, 1, 1))  # Output: 3
        print(count_alive_neighbors(board, 0, 0))  # Output: 1
    """
```
    Examples

    ```python
# Explanation: This function counts the number of alive (1) neighbors around a given cell in a 2D grid.
# The function assumes the grid is represented as a list of lists where each element is either 0 or 1,
# indicating an empty space or an alive cell, respectively. The function uses basic arithmetic to
# determine the number of alive neighbors based on its current position.

# Basic usage:
grid = [
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]
cell_x, cell_y = 1, 1
print(count_alive_neighbors(grid, cell_x, cell_y))  # Output: 3

# Edge case:
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
cell_x, cell_y = 1, 1
print(count_alive_neighbors(grid, cell_x, cell_y))  # Output: 0

# Advanced scenario:
grid = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]
cell_x, cell_y = 1, 1
print(count_alive_neighbors(grid, cell_x, cell_y))  # Output: 4

# Additional explanation:
# - The function checks all eight possible directions around the given cell (up, down, left, right,
#   and diagonals).
# - It uses modulo operations to wrap around the grid boundaries, ensuring that cells on the edge
#   of the grid have neighbors on the opposite side.
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of live neighbors around a given cell (x, y) in the live_map.

    Args:
        live_map (list of list of bool): A 2D grid representing the current state of the game.
        x (int): The x-coordinate of the cell to check.
        y (int): The y-coordinate of the cell to check.

    Returns:
        int: The number of live neighbors around the specified cell.

    Examples:
        >>> live_map = [
            [False, False, False],
            [True,  True, False],
            [False, False, False]
        ]
        >>> count_alive_neighbors(live_map, 1, 1)
        2
        >>> count_alive_neighbors(live_map, 0, 0)
        1
        >>> count_alive_neighbors(live_map, 2, 2)
        0
    """
```"""
    ```