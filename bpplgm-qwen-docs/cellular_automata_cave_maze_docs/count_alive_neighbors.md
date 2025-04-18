# count_alive_neighbors

    Purpose

    This function counts the number of alive neighbors for a given cell (x, y) in a live map. It checks all eight possible neighboring cells within the bounds of the live map and sums up the count of alive cells.

Example usage:
```python
live_map = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print(count_alive_neighbors(live_map, 1, 1))  # Output: 2
```
    Parameters

    ```python
def count_alive_neighbors(live_map: List[List[bool]], x: int, y: int) -> int:
    """
    Counts the number of alive neighbors for a given cell (x, y) in a live map.

    Parameters:
        live_map (List[List[bool]]): The current state of the game grid.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of alive neighbors for the cell at position (x, y).

    Example usage:
        live_map = [
            [True, False, True],
            [False, True, False],
            [True, False, True]
        ]

        print(count_alive_neighbors(live_map, 1, 1))  # Output: 2
    """
```
    Returns

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given cell (x, y) in a live map.

    Parameters:
    - live_map: A list of lists representing the live map where each cell is either True or False.
                 True indicates an alive cell, and False indicates a dead cell.
    - x: The row index of the cell to check.
    - y: The column index of the cell to check.

    Returns:
    An integer representing the number of alive neighbors for the given cell (x, y).

    Special Cases:
    - If the cell is on the edge or corner of the live map, it considers only the
      neighboring cells within its bounds.
    """

    # Define the eight possible directions to check
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    count = 0

    # Iterate over the eight directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Check if the new coordinates are within the bounds of the live map
        if 0 <= nx < len(live_map) and 0 <= ny < len(live_map[0]):
            # Add 1 to count if the neighboring cell is alive (True)
            if live_map[nx][ny]:
                count += 1

    return count
```
    Examples

    ```python
# Basic usage: Calculate alive neighbors for a cell in a 2D grid
grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

alive_neighbors = count_alive_neighbors(grid, (1, 1))
print(alive_neighbors)  # Output: 3

# Edge case: Calculate alive neighbors for a cell on the edge of the grid
grid_edge = [
    [1, 0],
    [0, 1]
]

alive_neighbors_edge = count_alive_neighbors(grid_edge, (0, 1))
print(alive_neighbors_edge)  # Output: 1

# Advanced scenario: Calculate alive neighbors for a cell with multiple neighbors
grid_complex = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

alive_neighbors_complex = count_alive_neighbors(grid_complex, (1, 1))
print(alive_neighbors_complex)  # Output: 5
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of live neighbors around a given cell in a 2D grid.

    Args:
        live_map (list of list of bool): The current state of the game board, where True represents a live cell and False represents a dead cell.
        x (int): The x-coordinate of the cell to check.
        y (int): The y-coordinate of the cell to check.

    Returns:
        int: The number of live neighbors around the specified cell.

    Examples:
        >>> live_map = [
            [False, True, False],
            [True, True, True],
            [False, False, False]
        ]
        >>> count_alive_neighbors(live_map, 1, 1)
        4
        >>> count_alive_neighbors(live_map, 0, 0)
        2
    """
```"""
    ```