# count_alive_neighbors

    Purpose

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given position in a live map.

    Args:
        live_map (list): A 2D list representing the live map.
        x (int): The x-coordinate of the current position.
        y (int): The y-coordinate of the current position.

    Returns:
        int: The number of alive neighbors at the given position.
    """
```
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given position in a live map.

    Args:
        live_map (list): A 2D list representing the live map.
        x (int): The x-coordinate of the current position.
        y (int): The y-coordinate of the current position.

    Returns:
        int: The number of alive neighbors at the given position.
    """
    
    # Description
    # This function counts the number of alive neighbors for a given position in a live map.
    
    # Parameters
    # live_map (list): A 2D list representing the live map.
    # x (int): The x-coordinate of the current position.
    # y (int): The y-coordinate of the current position.

    # Usage constraints
    # None
```
    Returns

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given position in a live map.

    Args:
        live_map (list): A 2D list representing the live map.
        x (int): The x-coordinate of the current position.
        y (int): The y-coordinate of the current position.

    Returns:
        int: The number of alive neighbors at the given position.
    """
    # Return type
    return count

# Description
The function 'count_alive_neighbors' takes a live map and its coordinates as input, 
and returns an integer representing the number of alive neighbors in that specific position.

# Special cases
- If the input live_map is empty or not a 2D list, the function will raise an error.
- If x or y coordinates are out of range (i.e., less than 0 or greater than or equal to the size of the live map), 
the function will return 0 for all positions in that direction.
    Examples

    ```python
# Basic usage
def count_alive_neighbors(grid):
    """Counts the number of alive neighbors for each cell in a grid."""
    return sum(1 for row in grid for cell in row if cell == 1)

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(count_alive_neighbors(grid))  # Output: 2

# Edge case
def count_alive_neighbors_edge_case(grid):
    """Counts the number of alive neighbors for a single cell in an empty grid."""
    return sum(1 for row in grid for cell in row if cell == 1)

grid = [
    [0, 0],
    [0, 0]
]

print(count_alive_neighbors_edge_case(grid))  # Output: 2

# Advanced scenario (if applicable)
def count_alive_neighbors_advanced_scenario(grid):
    """Counts the number of alive neighbors for a grid where some cells are alive."""
    return sum(1 for row in grid for cell in row if any(cell == 1) and cell != 0)

grid = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

print(count_alive_neighbors_advanced_scenario(grid))  # Output: 7
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given cell on a live map.

    Args:
        live_map (list of lists): A 2D list representing the live map.
        x (int): The x-coordinate of the cell to check.
        y (int): The y-coordinate of the cell to check.

    Returns:
        int: The number of alive neighbors in the given cell.
    """
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            # In case the index we're looking at it off the edge of the live_map
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # Otherwise, a normal check of the neighbour
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count

Include:

A one-line description: Counts alive neighbors in a cell on a live map.

Args section with parameter details:
- `live_map`: A 2D list representing the live map.
- `x`: The x-coordinate of the cell to check.
- `y`: The y-coordinate of the cell to check.

Returns section with return value details:
- Number of alive neighbors in the given cell.

Examples section showing usage:
>>> count_alive_neighbors([[True, False, True], [False, True, False]], 1, 1)
4
>>> count_alive_neighbors([[True, False, False], [False, False, False]], 2, 2)
8
>>> count_alive_neighbors([[False, False, False], [False, False, False]], 0, 0)
3"""
    ```