# count_alive_neighbors

    Purpose

    **Function Purpose**

The `count_alive_neighbors` function calculates the number of alive neighbors for a given cell in a life simulation grid, considering a specific offset in both x and y directions.

**Documentation**

```python
def count_alive_neighbors(live_map, x, y):
    """
    Calculate the number of alive neighbors for a given cell in a life simulation grid.

    Args:
        live_map (list): A 2D list representing the grid.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of alive neighbors for the given cell.
    """
```

**Examples**

```python
# Example usage:
live_map = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print(count_alive_neighbors(live_map, 1, 0))  # Output: 2 (alive neighbors in the top-left)
print(count_alive_neighbors(live_map, 3, 5))  # Output: 2 (alive neighbors in the bottom-right)
```
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Calculate the number of alive neighbors for a given cell in a life simulation grid.

    Args:
        live_map (list): A 2D list representing the grid.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of alive neighbors for the given cell.

    Examples
    --------
    >>> live_map = [
    ...     [True, False, True],
    ...     [False, True, False],
    ...     [True, False, True]
    ...
    ]
    >>> print(count_alive_neighbors(live_map, 1, 0))  # Output: 2 (alive neighbors in the top-left)
    >>> print(count_alive_neighbors(live_map, 3, 5))  # Output: 2 (alive neighbors in the bottom-right)
    """
```
    Returns

    Here is the documented code:

```python
def count_alive_neighbors(live_map, x, y):
    """
    Calculate the number of alive neighbors for a given cell in a life simulation grid.

    Args:
        live_map (list): A 2D list representing the grid.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of alive neighbors for the given cell.
    """
    # Return type
    return count  # Return a single value

# Description
**Function Purpose**

The `count_alive_neighbors` function calculates the number of alive neighbors for a given cell in a life simulation grid. It takes into account the specific offset in both x and y directions when determining the number of alive neighbors.

Special cases:

* If the input arguments are outside the valid range for the live_map, an error will be raised.
```

```python
# Example usage:
live_map = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

print(count_alive_neighbors(live_map, 1, 0))  # Output: 2 (alive neighbors in the top-left)
print(count_alive_neighbors(live_map, 3, 5))  # Output: 2 (alive neighbors in the bottom-right)
```
    Examples

    ```python
# Basic usage
def count_alive_neighbors(grid):
    """
    Counts the number of alive neighbors for each cell in the grid.

    Args:
        grid (list): A 2D list representing the grid, where 0 represents an alive cell and 1 represents a dead cell.

    Returns:
        int: The total number of alive neighbors.
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
    return count

# Edge case: Grid with no alive cells
grid = [[0]*10 for _ in range(10)]
print(count_alive_neighbors(grid))  # Output: 0

# Advanced scenario: Grid with a small island
grid = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(count_alive_neighbors(grid))  # Output: 5
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given cell on a live map.

    Args:
        live_map (list): A 2D list representing the live map.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of alive neighbors for the given cell.
    """
    # Initialize a counter for alive neighbors
    count = 0
    
    # Loop through possible directions (up, down, left, right)
    i = -1
    while i < 2:
        j = -1
        # Skip the current cell itself if it's at the center
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            
            # If this is the middle point, don't add ourselves to the count
            if i == 0 and j == 0:
                pass
                
            # Check if we're off the edge of the live map or if it's not a valid cell
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
                
            # If this is an alive neighbor, add it to the counter
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            
            j += 1
        
        i += 1
    
    return count
```"""
    ```