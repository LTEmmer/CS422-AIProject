# check_neighbors

    Purpose

    The `check_neighbors` function checks for neighboring cells in a 2D grid (`cell_array`) and returns an unvisited neighbor cell along with its direction from the current cell. If there are no unvisited neighbors, it returns `None` for both the cell and the direction. The directions are stored in `unvisited_directions` to track which directions have been checked and returned.
    Parameters

    ```python
def check_neighbors(self):
    """
    The `check_neighbors` function checks for neighboring cells in a 2D grid (`cell_array`) and returns an unvisited neighbor cell along with its direction from the current cell. If there are no unvisited neighbors, it returns `None` for both the cell and the direction.

    Returns:
        tuple: A tuple containing the cell and direction of an unvisited neighbor, or `None` if there is no such neighbor.
        
    Parameters:
        None
    """
    # Example usage:
    # Assuming 'self' refers to a class instance with attributes 'cell_array', 'unvisited_directions', etc.

    # Check for unvisited neighbors in all four directions (up, down, left, right)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    for dx, dy in directions:
        x, y = self.current_cell[0] + dx, self.current_cell[1] + dy
        if 0 <= x < len(self.cell_array) and 0 <= y < len(self.cell_array[x]) and self.cell_array[x][y].status != 'visited':
            # Found an unvisited neighbor, return it along with its direction from the current cell
            return (self.cell_array[x][y], directions.index((dx, dy)))
    
    # If no unvisited neighbors are found, return None for both the cell and the direction
    return (None, None)
```

This document describes the purpose of the `check_neighbors` function and its parameters as specified in the Google-style docstring conventions. The docstring includes a description of what the function does, its returns, and a brief example usage scenario assuming `self` refers to a class instance with relevant attributes.
    Returns

    ```python
def check_neighbors(cell_array, r, c, unvisited_directions):
    """
    Check for neighboring cells in a 2D grid and return an unvisited neighbor cell along with its direction from the current cell.

    Returns:
        tuple: A tuple containing:
            - The unvisited neighbor cell if found, otherwise None
            - The direction of the unvisited neighbor cell from the current cell

    Special Cases:
        - If all possible directions have been checked and no unvisited neighbors are found, returns (None, None).
        - If there are multiple unvisited neighbors in the same direction, returns one of them arbitrarily.
        - If a neighboring cell is out of bounds, it is considered an invalid neighbor.

    Args:
        cell_array: A 2D grid representing the maze or any other 2D structure.
        r (int): The row index of the current cell.
        c (int): The column index of the current cell.
        unvisited_directions (list of bools): A list indicating which directions have been checked and can be returned. Indices correspond to the cardinal directions: [up, right, down, left].
    """
    # List of possible directions
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # Iterate over each direction
    for i, (dr, dc) in enumerate(directions):
        nr, nc = r + dr, c + dc

        # Check if the new cell is within bounds and unvisited
        if 0 <= nr < len(cell_array) and 0 <= nc < len(cell_array[0]) and not unvisited_directions[i]:
            # Mark the direction as visited
            unvisited_directions[i] = True
            return (nr, nc), directions[i]

    # If no unvisited neighbors are found, return None for both cell and direction
    return None, None
```

This function checks each neighboring cell in a 2D grid to see if it is unvisited. It returns the first unvisited neighbor found along with its direction from the current cell. If all possible directions have been checked and no unvisited neighbors are found, it returns `None` for both the cell and the direction. The function marks visited directions using a list of booleans called `unvisited_directions`.
    Examples

    ```python
# Basic usage: Check if an element exists in a list and return its index
my_list = [1, 2, 3, 4, 5]
element_to_find = 3

index = check_neighbors(element_to_find, my_list)
if index is not None:
    print(f"Element {element_to_find} found at index: {index}")
else:
    print("Element not found in the list.")
```

```python
# Edge case: Check for an element that does not exist in a list
my_list = [1, 2, 3, 4, 5]
element_to_find = 6

index = check_neighbors(element_to_find, my_list)
if index is not None:
    print(f"Element {element_to_find} found at index: {index}")
else:
    print("Element not found in the list.")
```

```python
# Advanced scenario: Check for an element that exists in a list and perform additional checks
my_list = [1, 2, 3, 4, 5]
element_to_find = 3

index = check_neighbors(element_to_find, my_list)
if index is not None:
    if index > 0 and index < len(my_list) - 1:
        print(f"Element {element_to_find} found at index: {index}. It is a middle element.")
    else:
        print(f"Element {element_to_find} found at index: {index}. It is the first or last element.")
else:
    print("Element not found in the list.")
```
    Docstring

    """```python
def check_neighbors(self):
    """
    Check the neighboring cells for unvisited cells and randomly select one to move towards.

    This method determines which unvisited neighbors exist around the current cell. If any unvisited
    neighbors are found, it selects one at random to return both the neighbor and its direction from the 
    current cell.

    Args:
        self (Object): The object representing the current cell in a grid or maze environment.

    Returns:
        Tuple: A tuple containing the chosen neighbor and its direction. Returns None if no unvisited
              neighbors are found.

    Examples:
        >>> cell = Cell(x, y)
        >>> # Assuming index function is defined to get the cell at a specific position
        >>> cell_array[index(x + 1, y)]  # Check right
        >>> cell.check_neighbors()
        (cell_array[index(x + 1, y)], 'right')
    """
```"""
    ```