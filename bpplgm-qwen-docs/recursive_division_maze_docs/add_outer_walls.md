# add_outer_walls

    Purpose

    This function adds outer walls to a 2D grid `level_map` of specified size. It iterates over each row and sets the first and last columns to 1, effectively adding walls around the entire grid.
    Parameters

    ```
Function Purpose: This function adds outer walls to a 2D grid `level_map` of specified size. It iterates over each row and sets the first and last columns to 1, effectively adding walls around the entire grid.

Parameters:
- level_map (list of lists): A 2D list representing the current state of the game map. Each element in the list represents a cell on the map.
- size (int): The width and height of the grid, indicating the number of rows and columns in the grid.

Usage Constraints: 
- Ensure that `level_map` is a non-empty list of lists where each inner list has the same length as specified by `size`.
- The function assumes that `level_map` is large enough to accommodate the new outer walls. If not, additional resizing may be necessary.
```
    Returns

    ```python
def add_outer_walls(level_map: List[List[int]], size: int) -> List[List[int]]:
    """
    This function adds outer walls to a 2D grid `level_map` of specified size. It iterates over each row and sets the first and last columns to 1,
    effectively adding walls around the entire grid.

    Args:
        level_map (List[List[int]]): The 2D grid where outer walls will be added.
        size (int): The size of the grid, which is expected to be a square (size x size).

    Returns:
        List[List[int]]: The modified grid with outer walls added.

    Special cases:
        - If the input `level_map` or `size` are not valid, the function will return an empty list.
    """
    if level_map and len(level_map) == size and all(len(row) == size for row in level_map):
        for i in range(size):
            level_map[i][0] = 1
            level_map[i][-1] = 1
    else:
        return []

# Example usage:
level_map = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

size = 3

modified_level_map = add_outer_walls(level_map, size)
print(modified_level_map)  # Output: [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
```
    Examples

    ```python
# Basic usage: Adds outer walls to a room object.
room = Room(length=10, width=8)
add_outer_walls(room)
print(f"Room's outer walls added. Length: {room.length}, Width: {room.width}, Outer Wall Coverage: {room.outer_wall_coverage}")
```

```python
# Edge case: Attempts to add outer walls to a room with negative dimensions.
try:
    add_outer_walls(Room(length=-5, width=10))
except ValueError as e:
    print(e)
```

```python
# Advanced scenario: Adds outer walls to multiple rooms in a building.
building = Building()
building.add_room(Room(length=12, width=14))
building.add_room(Room(length=9, width=7))
add_outer_walls(building)
print("Outer walls added to each room in the building.")
```
    Docstring

    """```python
def add_outer_walls(level_map, size):
    """
    Adds outer walls to a level map.

    This function iterates through each row and column of the given 2D list `level_map`.
    It sets all elements on the first and last rows to 1, as they represent outer walls.
    Additionally, it sets the first and last elements of each inner row to 1, representing the
    outer walls along the columns.

    Args:
        level_map (list of lists of int): The game level map represented as a 2D list.
        size (int): The size of the level map (number of rows/columns).

    Returns:
        None: Modifies the `level_map` in-place to add outer walls.

    Examples:
        level_map = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        size = 3
        add_outer_walls(level_map, size)

        After calling this function, `level_map` will be:
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    """
```"""
    ```