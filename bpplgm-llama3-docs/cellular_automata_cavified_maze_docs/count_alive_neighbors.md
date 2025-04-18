# count_alive_neighbors

    Purpose

    ### Purpose

This Python function counts the number of alive neighbors in a given live map at the specified coordinates (x, y).

### Description

The function takes as input a `live_map` representing a grid of living cells and two coordinates `(x, y)`, where `x` and `y` are the indices of the top-left corner of the cell. It then iterates over all possible adjacent cells within a 3x3 neighborhood (including the center cell), checks if each alive neighbor is also alive, and increments the counter whenever it finds one.

### Parameters

*   `live_map`: A 2D list representing the live map.
*   `x`: The x-coordinate of the top-left corner of the current grid cell.
*   `y`: The y-coordinate of the top-left corner of the current grid cell.
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given live map at the specified coordinates (x, y).

    Parameters
    ----------
    live_map : list[list[int]]
        A 2D list representing the live map.
    x : int
        The x-coordinate of the top-left corner of the current grid cell.
    y : int
        The y-coordinate of the top-left corner of the current grid cell.

    Returns
    -------
    int
        The number of alive neighbors in the specified coordinates.

    Example
    --------
    >>> live_map = [[1, 0, 1], [0, 1, 0]]
    >>> count_alive_neighbors(live_map, 1, 1)
    2
    """

    # Get the total number of cells in the live map
    num_cells = len(live_map)

    # Check if the coordinates are within the valid range
    if x < 0 or y < 0 or x >= num_cells or y >= num_cells:
        raise IndexError("Coordinates out of range")

    # Initialize a counter for alive neighbors
    alive_neighbor_count = 0

    # Define the possible directions to check adjacent cells
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Iterate over all possible adjacent cells within the neighborhood
    for dx, dy in directions:
        # Calculate the coordinates of the adjacent cell
        adj_x, adj_y = x + dx, y + dy

        # Check if the adjacent cell is alive and within the live map boundaries
        if 0 <= adj_x < num_cells and 0 <= adj_y < num_cells and live_map[adj_x][adj_y]:
            # Increment the counter for alive neighbors
            alive_neighbor_count += 1

    return alive_neighbor_count
```
    Returns

    ### return_value for 'count_alive_neighbors'

*   **Return Type:** `int`
*   **Description:** The function returns an integer representing the number of alive neighbors at the specified coordinates (x, y) on the live map.
*   **Special Cases:**
    - If the input coordinate is out of bounds or outside the live map, the function raises a ValueError with an informative error message.
    Examples

    ```python
# Basic usage
def count_alive_neighbors(grid):
    """
    Counts the number of alive neighbors for each cell in a given grid.

    Args:
        grid (list): A 2D list representing the grid, where 'L' and 'R' represent lives and '-' represents dead cells.

    Returns:
        int: The total number of alive neighbors.
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i > 0 and grid[i][j] == 'L') or (i < len(grid) - 1 and grid[i][j] == 'R') or \
               (j > 0 and grid[i][j] == 'L') or (j < len(grid[0]) - 1 and grid[i][j] == 'R'):
                count += 1
    return count

# Edge case: Empty grid with no alive neighbors
grid = [['-' for _ in range(10)] for _ in range(10)]
print(count_alive_neighbors(grid))  # Output: 0

# Advanced scenario (with isolated live cells)
grid = [
    ['L', 'R', 'L', '-'],
    ['-', '-', '-', 'R'],
    ['-'],  # This is an alive cell
    ['-', '-', '-', 'L']
]
print(count_alive_neighbors(grid))  # Output: 2

# Edge case (a single live cell in the middle of a grid with no alive neighbors)
grid = [
    ['-'], ['-', '-', '-'], ['-', '-', '-'],
    ['-'], ['-'], ['-'], ['R']   # This is an isolated live cell
]
print(count_alive_neighbors(grid))  # Output: 1
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given position in a live map.

    Args:
        live_map (list of lists): A 2D list representing the live map.
        x (int): The x-coordinate of the current position.
        y (int): The y-coordinate of the current position.

    Returns:
        int: The number of alive neighbors at the given position.

    Examples:
    >>> live_map = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    >>> count_alive_neighbors(live_map, 1, 1)
    3
    """
```"""
    ```