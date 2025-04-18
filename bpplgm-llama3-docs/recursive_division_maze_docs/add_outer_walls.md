# add_outer_walls

    Purpose

    The purpose of this function is to create a 2D array representing an outer wall configuration, where walls are represented by the value 1 and empty spaces by the default value (usually 0).

```python
def add_outer_walls(level_map, size):
```

```python
for i in range(size):
    if i == 0 or i == size - 1:
        for j in range(size):
            level_map[i][j] = 1
    else:
        level_map[i][0] = 1
        level_map[i][size - 1] = 1
```
    Parameters

    ```python
def add_outer_walls(level_map: list[list[int]], size: int) -> None:
    """
    Creates a 2D array representing an outer wall configuration.

    Parameters:
        level_map (list[list[int]]): A 2D list of integers, where 1 represents walls and 0 represents empty spaces.
        size (int): The height of the 2D array. Must be greater than 1 to create a valid wall configuration.

    Description:
        This function creates an outer wall configuration for a given level map and size by setting all walls at the top and bottom edges to 1, and all other cells to 0.
    """
    
    # Parameters: 
    # level_map (list[list[int]]): The input level map. It must be initialized with valid values of either 0 or 1.
    # size (int): The height of the level map. It must be greater than 1 for an outer wall configuration to exist.

    # Loop through each row in the level map
    for i in range(size):
        
        # If this is the top edge, set all walls at this position to 1
        if i == 0 or i == size - 1:
            for j in range(size):
                level_map[i][j] = 1
                
        # Otherwise, set only the bottom and top cells to 1 (the edges of the outer wall)
        else:
            level_map[i][0] = 1
            level_map[i][size - 1] = 1
    Returns

    ```python
def add_outer_walls(level_map: list[list[int]], size: int) -> list[list[int]]:
    """
    Creates a 2D array representing an outer wall configuration, where walls are represented by the value 1 and empty spaces by the default value (usually 0).

    Args:
        level_map (list[list[int]]): A 2D array of integers representing the current state of the landscape.
        size (int): The size of the resulting wall configuration.

    Returns:
        list[list[int]]: A new 2D array where walls are represented by 1 and empty spaces are represented by 0.

    Description:
    This function iterates over each cell in the level map. If a cell is on one of the edges (i.e., row or column index is 0 or size - 1), it sets all cells in that row to wall type 1. Otherwise, it sets the first and last columns to wall type 1.

    Special cases:
    None
    """
```
    Examples

    ```python
def add_outer_walls(length, height):
    """
    Adds outer walls to a room based on its length and height.

    Args:
        length (float): The length of the room in meters.
        height (float): The height of the room in meters.

    Returns:
        dict: A dictionary containing the updated dimensions with outer walls.
    """

    # Explanation
    code

```
    Docstring

    """```python
def add_outer_walls(level_map, size):
    """
    Adds outer walls to a 2D level map at specified boundaries.

    Args:
        level_map (list of lists): The input 2D level map.
        size (int): The width and height of the level map.

    Returns:
        None

    Examples:
        >>> level_map = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> add_outer_walls(level_map, 3)
        [[0, 0, 1], [0, 2, 0], [0, 0, 1]]
    """
```"""
    ```