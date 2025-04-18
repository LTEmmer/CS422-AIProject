# check_neighbors

    Purpose

    The purpose of this function is to determine the neighboring cells of a given cell in an 8-cell grid and randomly select one of them for further processing.

*   It takes no arguments.
*  
*   The existing functionality can be described as follows:

    *   It initializes several variables, including `neighbors`, `unvisited_directions` (which stores relative directions to unvisited neighboring cells), and a counter (`direction_key`) that keeps track of the number of available directions to unvisited cells.
    *   It checks each neighboring cell by indexing into the `cell_array` at specific coordinates (top-left, top-right, bottom-right, bottom-left).
    *   If a neighboring cell exists on the grid, it stores the relative direction (up, right, down, left) and assigns it to the corresponding key in `unvisited_directions`.
    *  
*   Examples using the existing code:

    ```python
import random

# Assuming 'cell_array' is defined elsewhere
array_size = 8
x = 2  # Example x-coordinate
y = 1  # Example y-coordinate

# Get neighboring cells and their directions
neighbors, unvisited_directions = check_neighbors(cell_array, x, y)

if neighbors:
    print(f"Selected neighbor: {neighbors[0]} direction: {unvisited_directions}")
else:
    print("No neighbors found.")
```
    Parameters

    ```python
def check_neighbors(
    cell_array: list[list[str]],  # The input 8-cell grid array
    x: int,  # X-coordinate of the current cell
    y: int  # Y-coordinate of the current cell
) -> tuple[list[tuple[int, str]], dict[int, str]]:
    """
    This function determines the neighboring cells of a given cell in an 8-cell grid 
    and randomly selects one of them for further processing.

    Parameters:
    cell_array (list[list[str]]): The input 8-cell grid array.
    x (int): The X-coordinate of the current cell.
    y (int): The Y-coordinate of the current cell.

    Returns:
    tuple[list[tuple[int, str]], dict[int, str]]: A tuple containing a list of neighboring cells 
    and their directions, along with a dictionary mapping each direction to its unvisited neighbors.
    """

    # Initialize variables
    neighbors = []  # List to store the selected neighbor's cell coordinates
    unvisited_directions = {}  # Dictionary mapping relative directions to unvisited neighboring cells
    direction_key = None  # Counter for available directions

    # Check each neighboring cell by indexing into the `cell_array` at specific coordinates
    top_left = (x - 1, y - 1)  # Top-left corner of the grid
    top_right = (x + 1, y - 1)
    bottom_right = (x + 1, y + 1)
    bottom_left = (x - 1, y + 1)

    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        neighbor = cell_array[top_left] if top_left != bottom_left else cell_array[bottom_right]
        
        # Store the relative direction and assign it to the corresponding key in `unvisited_directions`
        unvisited_directions[(direction_key := direction)] = neighbor
        
    return neighbors, unvisited_directions
```
    Returns

    ```python
def check_neighbors(cell_array: list[list[int]], x: int, y: int) -> tuple[str, list[tuple]]:
    """
    This function determines the neighboring cells of a given cell in an 8-cell grid and randomly selects one of them for further processing.

    Args:
        cell_array (list[list[int]]): The 2D array representing the grid.
        x (int): The x-coordinate of the current cell.
        y (int): The y-coordinate of the current cell.

    Returns:
        tuple[str, list[tuple]]: A tuple containing the direction of an unvisited neighbor cell and a list of tuples storing relative directions to unvisited neighboring cells. If no neighbors are found, returns ('No neighbors found', None).

    Description:
        Initializes several variables to store the number of available directions.
        Iterates over each neighboring cell by indexing into the `cell_array` at specific coordinates (top-left, top-right, bottom-right, bottom-left).
        Stores the relative direction and assigns it to the corresponding key in `unvisited_directions`.
    """

    # Initialize variables
    neighbors = []
    unvisited_directions = {}

    # Check each neighboring cell
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        # Ensure the neighboring cell is within the grid boundaries
        if 0 <= nx < len(cell_array) and 0 <= ny < len(cell_array[0]):
            # Store the relative direction
            unvisited_directions[(nx, ny)] = (dx, dy)

    return 'return the direction of an unvisited neighbor cell', neighbors
    Examples

    ```python
def check_neighbors(grid, x, y):
    """
    Check if there are any neighbors with a value less than the current cell's value.

    Args:
        grid (list): A 2D list representing the game board.
        x (int): The row index of the current cell.
        y (int): The column index of the current cell.

    Returns:
        bool: True if there are any neighbors with a value less than the current cell's value, False otherwise.
    """
    # Check the neighbor to the left
    if x > 0 and grid[x-1][y] < grid[x][y]:
        return True

    # Check the neighbor to the right
    if x < len(grid) - 1 and grid[x+1][y] < grid[x][y]:
        return True

    # Check the neighbor above
    if y > 0 and grid[x][y-1] < grid[x][y]:
        return True

    # Check the neighbor below
    if y < len(grid[0]) - 1 and grid[x][y+1] < grid[x][y]:
        return True

    return False


# Example usage for basic usage
print(check_neighbors([
    [5, 3, 8],
    [4, 2, 7],
    [1, 9, 10]
], 0, 0))  # Output: True (neighbor to the right)


# Example edge case - empty grid
grid = []
x, y = 0, 0
print(check_neighbors(grid, x, y))  # Output: False


# Example advanced scenario - multiple neighbors with values less than the current cell's value
grid = [
    [10, 8, 5],
    [4, 2, 7],
    [1, 9, 10]
]
x, y = 0, 0
print(check_neighbors(grid, x, y))  # Output: True (multiple neighbors with values less than the current cell's value)
```
    Docstring

    """```python
def check_neighbors(self):
    """
    Retrieves a random direction and corresponding neighbor for unvisited neighboring cells on the cell_array.

    Returns:
        tuple: A pair containing the randomly selected unvisited neighbor cell and its relative direction ('up', 'right', 'down', or 'left') if any.
    """
    # ... (rest of the function remains the same)
```

A one-line description

```python
Checks for unvisited neighboring cells on the cell_array and returns a random direction to that cell, if any.
```"""
    ```