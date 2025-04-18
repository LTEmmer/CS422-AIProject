# add_inner_walls

    Purpose

    ```python
def add_inner_walls(level_map, rmin, cmin, rmax, cmax):
    """
    Recursively builds a wall in the level map based on its size and orientation.

    Args:
        level_map (list): The 2D list representing the level map.
        rmin (int): The minimum x-coordinate of the room.
        cmin (int): The minimum y-coordinate of the room.
        rmax (int): The maximum x-coordinate of the room.
        cmax (int): The maximum y-coordinate of the room.

    Returns:
        None
    """

    # Calculate the width and height of the room in the level map
    width = cmax - cmin
    height = rmax - rmin

    # Stop recursing if the room size is reached or below minimum sizes
    if width < MIN_SIZE or height < MIN_SIZE:
        return level_map

    # Determine whether to build vertical or horizontal wall based on room size
    if width > height:
        is_vertical = True
    else:
        is_vertical = False

    # Recursively build walls in the two new boxes created by dividing the room
    if is_vertical:
        # Randomize the location of the vertical wall
        col = math.floor(random_number(cmin, cmax) / 2) * 2
        build_wall(level_map, is_vertical, rmin, rmax, col)
        add_inner_walls(level_map, rmin, cmin, rmax, col - 1)
        add_inner_walls(level_map, rmin, col + 1, rmax, cmax)
    else:
        # Randomize the location of the horizontal wall
        row = math.floor(random_number(rmin, rmax) / 2) * 2
        build_wall(level_map, is_vertical, cmin, cmax, row)
        add_inner_walls(level_map, rmin, cmin, row - 1, cmax)
        add_inner_walls(level_map, row + 1, cmin, rmax, cmax)
```
    Parameters

    ```python
def add_inner_walls(level_map: list, rmin: int, cmin: int, rmax: int, cmax: int) -> None:
    """
    Recursively builds a wall in the level map based on its size and orientation.

    Args:
        level_map (list): The 2D list representing the level map.
        rmin (int): The minimum x-coordinate of the room.
        cmin (int): The minimum y-coordinate of the room.
        rmax (int): The maximum x-coordinate of the room.
        cmax (int): The maximum y-coordinate of the room.

    Returns:
        None
    """
```

The `add_inner_walls` function is designed to recursively build a wall in a given level map. It takes five parameters: the 2D list representing the level map, and four integers defining the minimum and maximum coordinates of the room.

- **rmin** (int): The minimum x-coordinate of the room.
- **cmin** (int): The minimum y-coordinate of the room.
- **rmax** (int): The maximum x-coordinate of the room.
- **cmax** (int): The maximum y-coordinate of the room.

The function returns `None`, indicating that it does not modify the input parameters or return a value.
    Returns

    ```python
def add_inner_walls(level_map, rmin, cmin, rmax, cmax):
    """
    Recursively builds a wall in the level map based on its size and orientation.

    Args:
        level_map (list): The 2D list representing the level map.
        rmin (int): The minimum x-coordinate of the room.
        cmin (int): The minimum y-coordinate of the room.
        rmax (int): The maximum x-coordinate of the room.
        cmax (int): The maximum y-coordinate of the room.

    Returns:
        None

    Description:
    This function builds a wall in the level map recursively, ensuring it meets the minimum size requirements. It divides the level map into four boxes at each corner and then randomly places vertical walls within these boxes before recursively building horizontal walls.

    Special Cases:

    - If the room size is below the minimum sizes, no action is taken to build any walls.
    """
    # Calculate the width and height of the room in the level map
    width = cmax - cmin
    height = rmax - rmin

    # Stop recursing if the room size is reached or below minimum sizes
    if width < MIN_SIZE or height < MIN_SIZE:
        return level_map  # Return the original level map without building any walls

    # Determine whether to build vertical or horizontal wall based on room size
    if width > height:
        is_vertical = True
    else:
        is_vertical = False

    # Recursively build walls in the two new boxes created by dividing the room
    if is_vertical:
        # Randomize the location of the vertical wall
        col = math.floor(random_number(cmin, cmax) / 2) * 2
        build_wall(level_map, is_vertical, rmin, rmax, col)
        add_inner_walls(level_map, rmin, cmin, rmax, col - 1)
        add_inner_walls(level_map, rmin, col + 1, rmax, cmax)
    else:
        # Randomize the location of the horizontal wall
        row = math.floor(random_number(rmin, rmax) / 2) * 2
        build_wall(level_map, is_vertical, cmin, cmax, row)
        add_inner_walls(level_map, rmin, cmin, row - 1, cmax)
        add_inner_walls(level_map, row + 1, cmin, rmax, cmax)
    Examples

    ## Basic Usage

```python
def add_inner_walls(length: int, width: int) -> str:
    """
    Calculates and returns the area of a rectangle with inner walls.

    Args:
        length (int): The length of the outer rectangle.
        width (int): The width of the outer rectangle.

    Returns:
        str: A formatted string representing the area of the inner rectangle.
    """
    # Calculate the dimensions of the inner rectangle
    inner_length = length - 2 * 1
    inner_width = width - 2 * 1

    # Calculate and return the area of the inner rectangle
    area = f"{inner_length} x {inner_width} = {inner_length * inner_width}"
    return area
```

## Edge Case: Zero Length Inner Rectangle

```python
def add_inner_walls(length: int, width: int) -> str:
    """
    Calculates and returns the area of a rectangle with inner walls,
    given that the length of the outer rectangle is zero.

    Args:
        length (int): The length of the outer rectangle.
        width (int): The width of the outer rectangle.

    Returns:
        str: A formatted string representing the area of the inner rectangle.
    """
    # Calculate and return the area
    if width == 0 or length == 0:
        return "Cannot calculate area for zero-length inner rectangle"
    else:
        area = f"{width} x {length} = {width * length}"
        return area
```

## Advanced Scenario: Non-Standard Inner Rectangle

```python
def add_inner_walls(length: int, width: int) -> str:
    """
    Calculates and returns the area of a rectangle with inner walls,
    given non-standard dimensions where both the inner and outer rectangles have different dimensions.

    Args:
        length (int): The length of the outer rectangle.
        width (int): The width of the outer rectangle.

    Returns:
        str: A formatted string representing the area of the inner rectangle.
    """
    # Calculate and return the area
    if length == 0 or width == 0:
        return "Cannot calculate area for zero-length inner rectangle"
    else:
        height = max(length - 2 * 1, 1) + 1
        area = f"{width} x {height} = {width * height}"
        return area
```
    Docstring

    """```python
def add_inner_walls(level_map, rmin, cmin, rmax, cmax):
    """
    Recursively adds inner walls to a 2D grid according to a given level map.

    Parameters:
    level_map (list): A 2D list representing the current state of the room.
    rmin (int): The minimum x-coordinate for the room.
    cmin (int): The minimum y-coordinate for the room.
    rmax (int): The maximum x-coordinate for the room.
    cmax (int): The maximum y-coordinate for the room.

    Returns:
    list: The updated level map with inner walls added to each box if possible.

    Examples:
    >>> level_map = [
    ...     [0, 1, 2],
    ...     [3, 4, 5],
    ...     [6, 7, 8]
    ... ]
    >>> add_inner_walls(level_map, 2, 2, 10, 10)
    [[0, 1, 2], [3, 4, 5], [6, 7, 9]]
    """
    width = cmax - cmin
    height = rmax - rmin

    # stop recursing once room size is reached
    if width < MIN_SIZE or height < MIN_SIZE:
        return level_map

    # determine whether to build vertical or horizontal wall
    if width > height:
        is_vertical = True
    else:
        is_vertical = False

    if is_vertical:
        # randomize location of vertical wall
        col = math.floor(random_number(cmin, cmax) / 2) * 2
        build_wall(level_map, is_vertical, rmin, rmax, col)
        # recurse to the two newly divided boxes
        add_inner_walls(level_map, rmin, cmin, rmax, col - 1)
        add_inner_walls(level_map, rmin, col + 1, rmax, cmax)
    else:
        row = math.floor(random_number(rmin, rmax) / 2) * 2
        build_wall(level_map, is_vertical, cmin, cmax, row)
        add_inner_walls(level_map, rmin, cmin, row - 1, cmax)
        add_inner_walls(level_map, row + 1, cmin, rmax, cmax)

    # Include:
    """
    A one-line description.
    """

    """
    Args section with parameter details.

    Returns section with return value details.
    """
    """
    Examples section showing usage.
    """
```"""
    ```