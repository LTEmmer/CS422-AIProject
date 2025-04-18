# count_alive_neighbors

    Purpose

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given direction (up, down, left, right) 
    for each cell in the live map at position (x, y).

    Args:
        live_map: A 2D list representing the living cells.
        x: The current x-coordinate.
        y: The current y-coordinate.

    Returns:
        The total number of alive neighbors.
    """
```

```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given direction (up, down, left, right) 
    for each cell in the live map at position (x, y).

    Args:
        live_map: A 2D list representing the living cells.
        x: The current x-coordinate.
        y: The current y-coordinate.

    Returns:
        The total number of alive neighbors.
    """
    count = 0
    i = -1
    while i < 2:
        j = -1
        # Check all four directions (up, down, left, right) for each neighbor cell
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            
            # If we're at the center of the live map and don't want to count ourselves,
            # do nothing.
            if i == 0 and j == 0:  
                pass  
            # If the neighbor cell is out of bounds, increment the count.
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # If the neighbor cell is alive, increment the count.
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
```
    Parameters

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given direction (up, down, left, right) 
    for each cell in the live map at position (x, y).

    Args:
        live_map: A 2D list representing the living cells.
        x: The current x-coordinate.
        y: The current y-coordinate.

    Returns:
        The total number of alive neighbors.

    Examples:
    >>> live_map = [
    ...     [True, True, False],
    ...     [False, True, False],
    ...     [False, False, True]
    ...
    ]
    >>> count_alive_neighbors(live_map, 1, 0)
    2
    """

    # Initialize the count of alive neighbors to 0
    count = 0
    
    # Iterate over all possible directions (up, down, left, right)
    i = -1
    while i < 2:
        j = -1

        # Check all four directions for each neighbor cell
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            
            # If we're at the center of the live map and don't want to count ourselves,
            # do nothing.
            if i == 0 and j == 0:  
                pass  

            # If the neighbor cell is out of bounds, increment the count.
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # If the neighbor cell is alive, increment the count.
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        
        i += 1
    
    return count
```

```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given direction (up, down, left, right) 
    for each cell in the live map at position (x, y).

    Args:
        live_map: A 2D list representing the living cells.
        x: The current x-coordinate.
        y: The current y-coordinate.

    Returns:
        The total number of alive neighbors.

    Parameters
    ----------
    live_map : list
        A 2D list representing the living cells.
    x : int
        The current x-coordinate.
    y : int
        The current y-coordinate.

    Examples:
    >>> live_map = [
    ...     [True, True, False],
    ...     [False, True, False],
    ...     [False, False, True]
    ...
    ]
    >>> count_alive_neighbors(live_map, 1, 0)
    2
    """

    # Initialize the count of alive neighbors to 0
    count = 0
    
    # Iterate over all possible directions (up, down, left, right) 
    i = -1
    while i < 2:
        j = -1

        # Check all four directions for each neighbor cell
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            
            # If we're at the center of the live map and don't want to count ourselves,
            # do nothing.
            if i == 0 and j == 0:  
                pass  

            # If the neighbor cell is out of bounds, increment the count.
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # If the neighbor cell is alive, increment the count.
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        
        i += 1
    
    return count
```
    Returns

    ```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors in a given direction (up, down, left, right) 
    for each cell in the live map at position (x, y).

    Args:
        live_map: A 2D list representing the living cells.
        x: The current x-coordinate.
        y: The current y-coordinate.

    Returns:
        int: The total number of alive neighbors.
    """
    # Initialize count variable to store the total number of alive neighbors
    count = 0
    
    # Iterate over all possible directions (up, down, left, right)
    i = -1
    while i < 2:
        j = -1
        
        # Check all four directions for each neighbor cell
        while j < 2:
            # Calculate the neighbor's coordinates based on the current direction
            neighbor_x = x + i
            
            # If we're at the center of the live map and don't want to count ourselves,
            # do nothing.
            if i == 0 and j == 0:  
                pass  
            
            # Check if the neighbor cell is within the bounds of the live map
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                # If out of bounds, increment the count by 1
                count += 1
            
            # Check if the neighbor cell is alive and not ourselves (x, y)
            elif live_map[neighbor_x][neighbor_y] is True:
                # Increment the count by 1
                count += 1
            
            j += 1
        
        i += 1
    
    # Return the total number of alive neighbors
    return count

# Example usage
live_map = [
    [True, False, True],
    [False, True, False],
    [True, False, True]
]

x, y = 0, 0
result = count_alive_neighbors(live_map, x, y)
print(f"Number of alive neighbors at ({x}, {y}): {result}")
```
    Examples

    ```python
def count_alive_neighbors(grid):
    """
    Count the number of alive neighbors for each cell in a grid.

    Args:
        grid (list[list[int]]): A 2D list representing the grid, where 0 indicates an empty space and 1 indicates an alive cell.

    Returns:
        list[tuple[int, int]]: A list of tuples containing the row and column indices of all alive neighbors for each cell in the grid.
    """
    count = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check all alive neighbors
            alive_neighbors = 0
            for x in range(max(0, i-1), min(i+2, len(grid))):
                for y in range(max(0, j-1), min(j+2, len(grid[0]))):
                    if grid[x][y] == 1:
                        alive_neighbors += 1
            count.append((i, j))
            # Append only alive neighbors
    return count

# Basic usage
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(count_alive_neighbors(grid))  # [(0, 0), (0, 2)]

# Edge case: Grid with all alive cells
grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(count_alive_neighbors(grid))  # []

# Advanced scenario: Grid with some dead neighbors
grid = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0]
]
print(count_alive_neighbors(grid))  # [(0, 2)]
```
    Docstring

    """```python
def count_alive_neighbors(live_map, x, y):
    """
    Counts the number of alive neighbors for a given point on a live map.

    Args:
        live_map: A 2D list representing the live map.
        x (int): The x-coordinate of the current position.
        y (int): The y-coordinate of the current position.

    Returns:
        int: The total count of alive neighbors in the surrounding area.

    Examples:
        >>> live_map = [[True, True, False], [False, True, True]]
        >>> print(count_alive_neighbors(live_map, 0, 0))  # Output: 8
        >>> live_map = [[True, True, False], [False, True, True]]
        >>> print(count_alive_neighbors(live_map, 1, 1))  # Output: 7
```"""
    ```