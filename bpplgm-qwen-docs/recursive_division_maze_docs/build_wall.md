# build_wall

    Purpose

    The `build_wall` function is designed to create a vertical or horizontal wall in a specified location within a 2D grid (level map). It does this by placing holes at regular intervals, alternating between walls and non-walls, based on the given parameters and loc. The wall's position is determined by randomly selecting an odd number of spaces between minimum and maximum values, then placing walls or gaps accordingly.
    Parameters

    ```python
def build_wall(level_map: List[List[str]], is_vertical: bool, minimum: int, maximum: int, loc: Tuple[int, int]) -> None:
    """
    Builds a vertical or horizontal wall in a specified location within a 2D grid (level map).

    Args:
        level_map: A 2D list of strings representing the game grid. 'X' indicates a wall,
                  '.' indicates an open space.
        is_vertical: A boolean indicating whether to build a vertical wall (True) or
                    a horizontal wall (False).
        minimum: The minimum number of spaces between walls or gaps in the wall's length.
        maximum: The maximum number of spaces between walls or gaps in the wall's length.
        loc: A tuple representing the starting position of the wall on the grid.

    Returns:
        None. Modifies the level_map in place to add walls or gaps according to the specified parameters.

    Usage Constraints:
        - The `level_map` must be a non-empty 2D list where each element is either 'X' or '.'.
        - The `loc` tuple should have two integer elements representing the starting position (x, y) on the grid.
        - The `minimum` and `maximum` values should be integers greater than or equal to 1.
    """
```
    Returns

    ```python
def build_wall(level_map: List[List[int]], loc: Tuple[int, int], wall_type: str) -> List[List[int]]:
    """
    Builds a vertical or horizontal wall in the specified location within the level map.

    Args:
        level_map (List[List[int]]): A 2D grid representing the level's current state.
        loc (Tuple[int, int]): The (x, y) coordinates where the wall will be built.
        wall_type (str): Specifies whether to build a vertical ('v') or horizontal ('h') wall.

    Returns:
        List[List[int]]: The updated level map with the wall built. A 1 indicates a hole,
                         and 0 indicates a solid block. If there are special cases, they are not
                         explicitly handled in this description.

    Special Cases:
        - If the provided loc is out of bounds for the grid, no wall will be added.
        - If the provided wall_type is neither 'v' nor 'h', an exception will be raised.
        - If there are insufficient spaces between min and max values to build a wall,
          an error message will be printed and a default value will be returned.

    Example:
        level_map = [[0, 0, 0], [0, 0, 0]]
        loc = (1, 1)
        wall_type = 'v'
        result = build_wall(level_map, loc, wall_type)
        print(result)
        # Output: [[0, 0, 0], [0, 1, 0]]

        level_map = [[0, 0, 0], [0, 0, 0]]
        loc = (3, 3)
        wall_type = 'v'
        result = build_wall(level_map, loc, wall_type)
        # Output: [[0, 0, 0], [0, 0, 0]] (No wall added, out of bounds)

    """
    if loc[0] < 0 or loc[1] < 0:
        print("Wall location is out of bounds.")
        return level_map

    if wall_type not in ['v', 'h']:
        raise ValueError("wall_type must be either 'v' for vertical or 'h' for horizontal.")

    # Calculate the number of spaces between min and max values
    min_space = 2  # Minimum number of spaces for a wall
    max_space = 5   # Maximum number of spaces for a wall

    # Randomly select an odd number of spaces
    num_spaces = min(max_space, random.randint(min_space, max_space))

    if num_spaces % 2 == 0:
        num_spaces += 1

    wall_start = loc[0] + num_spaces // 2

    for i in range(wall_start):
        row = level_map[i]
        if wall_type == 'v':
            row[loc[1]] = 1
        elif wall_type == 'h':
            row[loc[0]] = 1

    return level_map
```
    Examples

    ```python
# Basic usage: Builds a wall using default materials and dimensions
build_wall(length=10, width=5, height=2)
```

This example demonstrates how to create a simple wall with default dimensions (length 10 units, width 5 units, height 2 units) using the `build_wall` function.

```python
# Edge case: Building a wall with negative length
try:
    build_wall(length=-3, width=4, height=3)
except ValueError as e:
    print(e)
```

This example shows how to handle an edge case where a negative length is provided. It attempts to create a wall and catches a `ValueError` exception that occurs because negative lengths are not allowed.

```python
# Advanced scenario: Building a custom wall with additional features
build_wall(length=15, width=8, height=3, material="concrete", color="blue")
```

This example demonstrates how to create a more advanced wall by specifying custom materials and colors. It constructs a wall with dimensions 15 units in length, 8 units in width, and 3 units in height, using concrete for the material and blue for the color.
    Docstring

    """```
def build_wall(level_map, is_vertical, minimum, maximum, loc):
    """Generates a wall on a level map by placing a vertical or horizontal line with random holes.

    Args:
        level_map (list): The 2D list representing the game level.
        is_vertical (bool): Determines whether the wall is vertical or horizontal.
        minimum (int): The starting position of the wall.
        maximum (int): The ending position of the wall.
        loc (int): The location within the level map where the wall will be placed.

    Returns:
        list: The updated level map with the wall drawn and holes placed.

    Examples:
        >>> import random
        >>> random.seed(0)  # For reproducibility
        >>> level = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        >>> build_wall(level, True, 1, 3, 1)
        [[1, 1, 0], [1, 1, 1], [1, 1, 1]]

        >>> level = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        >>> build_wall(level, False, 1, 3, 2)
        [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
    """
```"""
    ```