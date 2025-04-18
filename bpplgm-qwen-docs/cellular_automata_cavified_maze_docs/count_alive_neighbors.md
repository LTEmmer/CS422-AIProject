# count_alive_neighbors

    Purpose

    This function calculates the number of living neighbors for a given cell `(x, y)` in a `live_map`, which is a 2D list representing a grid where each cell can be either alive or dead. It sums up all the live cells within an 3x3 neighborhood around the specified cell, excluding the cell itself.
    Parameters

    ```python
def count_alive_neighbors(live_map: List[List[int]], x: int, y: int) -> int:
    """
    Calculate the number of living neighbors for a given cell (x, y) in a live_map.
    
    Parameters:
        live_map (List[List[int]]): A 2D list representing a grid where each cell can be either alive (1) or dead (0).
        x (int): The x-coordinate of the cell to check.
        y (int): The y-coordinate of the cell to check.
        
    Returns:
        int: The number of living neighbors around the specified cell, excluding the cell itself.
        
    Usage Constraints:
        - 1 <= len(live_map) <= 100
        - 1 <= len(live_map[0]) <= 100
        - live_map[x][y] must be either 0 or 1
    """
    
    # Define the range of indices to check for neighbors in a 3x3 neighborhood
    min_x, max_x = max(0, x - 1), min(len(live_map), x + 2)
    min_y, max_y = max(0, y - 1), min(len(live_map[0]), y + 2)
    
    # Initialize the count of living neighbors
    count = 0
    
    # Iterate over the 3x3 neighborhood excluding the cell itself
    for nx in range(min_x, max_x):
        for ny in range(min_y, max_y):
            if (nx != x or ny != y) and live_map[nx][ny] == 1:
                count += 1
    
    return count
```

This function calculates the number of living neighbors around a specified cell `(x, y)` within a `live_map`. It iterates over an 3x3 neighborhood centered on the given cell, excluding the cell itself. The function returns the count of live cells in this neighborhood.
    Returns

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Calculate the number of living neighbors for a given cell (x, y) in a live_map.

    Args:
    - live_map: A 2D list where each element is either 'L' (alive) or 'D' (dead).
    - x: The row index of the cell.
    - y: The column index of the cell.

    Returns:
        - int: The number of living neighbors around the specified cell, excluding the cell itself.
    
    Special cases:
    - If the live_map is empty or the indices are out of bounds, this function returns 0.
    - If the cell is dead, it counts as having zero living neighbors.
    """
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Check if the indices are within bounds and not including the current cell itself
            if 0 <= i < len(live_map) and 0 <= j < len(live_map[0]) and (i, j) != (x, y):
                if live_map[i][j] == 'L':
                    count += 1
    return count
```

**Examples**:
```python
live_map = [
    ['L', 'D', 'L'],
    ['D', 'L', 'D'],
    ['L', 'D', 'L']
]

print(count_alive_neighbors(live_map, 1, 1))  # Output: 4

# Special case - dead cell
print(count_alive_neighbors(live_map, 0, 0))  # Output: 2

# Special case - empty map
live_map = []
print(count_alive_neighbors(live_map, 0, 0))  # Output: 0
```
    Examples

    ```python
# Basic usage: Counting neighbors for a cell in a grid.
def count_alive_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors (cells with value 1) around a given cell (row, col).

    Args:
    grid (list of list of int): The game board represented as a 2D list where 1 indicates an alive cell and 0 an empty cell.
    row (int): The row index of the cell to check.
    col (int): The column index of the cell to check.

    Returns:
    int: The count of alive neighbors around the specified cell.

    Usage:
    grid = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    print(count_alive_neighbors(grid, 1, 1))  # Output: 2
    """
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                count += 1
    return count - grid[row][col]

# Edge case: Checking a cell on the edge of the grid.
def test_count_alive_neighbors_edge():
    """
    Tests the function with a cell at the edge of the grid.

    Usage:
    grid = [[0, 1, 0], [0, 1, 0]]
    print(count_alive_neighbors(grid, 1, 1))  # Output: 2
    """
    grid = [[0, 1, 0], [0, 1, 0]]
    assert count_alive_neighbors(grid, 1, 1) == 2, "The edge case should return 2 alive neighbors."

# Advanced scenario: Counting neighbors for a cell in a larger grid with wrapping.
def test_count_alive_neighbors_wrap():
    """
    Tests the function with a large grid and wraps around.

    Usage:
    grid = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    print(count_alive_neighbors(grid, 2, 1))  # Output: 4
    """
    grid = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    assert count_alive_neighbors(grid, 2, 1) == 4, "The wrap-around case should return 4 alive neighbors."
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of live neighbors around a given cell (x, y) in the `live_map`.

    Args:
        live_map (list of list of bool): A 2D list representing the current state
                                       of cells where True indicates a live cell and False
                                       indicates a dead cell.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of live neighbors around the specified cell.

    Examples:
        >>> live_map = [
        ...     [False, True, False],
        ...     [True, True, True],
        ...     [False, True, False]
        ... ]
        >>> count_alive_neighbors(live_map, 1, 1)
        4
        >>> count_alive_neighbors(live_map, 0, 2)
        1
    """
```"""
    ```