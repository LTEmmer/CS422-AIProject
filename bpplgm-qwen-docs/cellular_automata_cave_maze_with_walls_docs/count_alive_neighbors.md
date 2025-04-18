# count_alive_neighbors

    Purpose

    This function counts the number of alive neighbors around a given cell `(x, y)` in a `live_map`, where each cell can be either live (True) or dead (False). It iterates over all possible neighbor positions and increments the count for each live neighbor.
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors around a given cell (x, y) in a live_map.

    Parameters:
        live_map (list of list of bool): A 2D grid where True represents an alive cell and False represents a dead cell.
        x (int): The row index of the cell to check.
        y (int): The column index of the cell to check.

    Returns:
        int: The number of live neighbors around the cell at position (x, y).

    Usage Constraints:
        - All cells in `live_map` must be either True or False.
        - The indices `x` and `y` must be within the bounds of the `live_map`.
    """
    
    # Initialize count of alive neighbors
    neighbor_count = 0
    
    # Define the possible directions for neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Iterate over all four possible directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # Check if the neighboring cell is within bounds and alive
        if 0 <= nx < len(live_map) and 0 <= ny < len(live_map[0]) and live_map[nx][ny]:
            neighbor_count += 1
    
    return neighbor_count

# Example usage:
live_map = [
    [True, False, True],
    [False, True, False],
    [True, True, False]
]

print(count_alive_neighbors(live_map, 1, 1))  # Output: 2
```
    Returns

    ### Function: `count_alive_neighbors`

#### Purpose:
This function counts the number of alive neighbors around a given cell `(x, y)` in a `live_map`, where each cell can be either live (True) or dead (False). It iterates over all possible neighbor positions and increments the count for each live neighbor.

#### Return Type:
- **int**: The total number of live neighbors around the specified cell `(x, y)`.

#### Description:
The function takes a tuple `(x, y)` representing the coordinates of the center cell and returns an integer indicating how many of its eight neighboring cells are also live. Neighbors are defined as those within one row and column distance from the center cell, excluding the center cell itself.

#### Special Cases:
- If `x` is at the top edge of the map (`0`), it only checks neighbors in the bottom row.
- If `y` is at the left edge of the map (`0`), it only checks neighbors in the right column.
- If `x` is at the bottom edge of the map (equal to or greater than the height minus one), it only checks neighbors in the top row.
- If `y` is at the right edge of the map (equal to or greater than the width minus one), it only checks neighbors in the left column.

### Examples

#### Example 1:
```python
live_map = [
    [False, False, True],
    [True, False, False],
    [False, True, False]
]

result = count_alive_neighbors((1, 1))
print(result)  # Output: 2 (alive neighbors are at positions (0, 1) and (1, 2))
```

#### Example 2:
```python
live_map = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]

result = count_alive_neighbors((1, 1))
print(result)  # Output: 4 (all neighbors are live)
```

#### Example 3:
```python
live_map = [
    [False, False, False],
    [False, False, False],
    [False, False, False]
]

result = count_alive_neighbors((1, 1))
print(result)  # Output: 0 (no neighbors are live)
```

#### Example 4:
```python
live_map = [
    [True, True, True],
    [True, True, True],
    [False, False, False]
]

result = count_alive_neighbors((0, 1))
print(result)  # Output: 3 (alive neighbors are at positions (0, 2), (1, 1), and (2, 1))
```
    Examples

    ```python
# Basic usage: Counts the number of alive neighbors for a cell at position (x, y) in a grid where 0 represents an empty cell and 1 represents an alive cell.
def count_alive_neighbors(x, y):
    pass

# Example 1:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(count_alive_neighbors(1, 1))  # Output: 3
```

```python
# Edge case: Counts the number of alive neighbors for a cell at position (2, 2) in an empty grid.
def count_alive_neighbors(x, y):
    pass

# Example 2:
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(count_alive_neighbors(2, 2))  # Output: 0
```

```python
# Advanced scenario: Counts the number of alive neighbors for a cell at position (1, 1) in a grid with complex rules for neighbor counting.
def count_alive_neighbors(x, y):
    pass

# Example 3:
grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(count_alive_neighbors(1, 1))  # Output: 4
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of live neighbors around a given cell in a 2D grid.

    Parameters:
        live_map (list of lists of bool): The current state of the grid, where True indicates an alive cell.
        x (int): The x-coordinate of the cell to check.
        y (int): The y-coordinate of the cell to check.

    Returns:
        int: The number of live neighbors around the specified cell.

    Examples:
        >>> count_alive_neighbors([[False, True, False], [True, False, True], [False, True, False]], 1, 1)
        3
        >>> count_alive_neighbors([[False, False, False], [False, False, False], [False, False, False]], 0, 0)
        0
    """
```"""
    ```