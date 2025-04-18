# place_cube

    Purpose

    The `place_cube` function creates a new cube in Blender using the specified coordinates `(x, y)` and places it at the origin. The cube's size is set to 2 units in all dimensions.
    Parameters

    ```python
def place_cube(x: float = 0.0, y: float = 0.0):
    """
    Create a new cube in Blender at the specified coordinates (x, y).

    Parameters:
        x (float): The x-coordinate where the cube should be placed.
        y (float): The y-coordinate where the cube should be placed.

    Description:
        This function creates a cube and places it in Blender using the provided
        coordinates. The cube's size is set to 2 units in all dimensions, meaning it
        will have side lengths of 2 units on each axis.
        
        Usage Constraints:
            - `x` and `y` should be valid floating-point numbers representing the
              position on the x and y axes respectively.
    """
```

### Examples:

```python
# Example usage: Place a cube at (3.0, 4.0)
place_cube(3.0, 4.0)

# Example usage: Place a different-sized cube at (1.5, -2.0) with side length of 1 unit
place_cube(x=1.5, y=-2.0, size=1.0)
```

### Usage Constraints:

- `x` and `y` must be valid floating-point numbers representing the position on the x and y axes respectively.
- The cube's size is set to 2 units in all dimensions, so the default size remains unchanged unless specified otherwise.
    Returns

    ```python
def place_cube(x: float = 0.0, y: float = 0.0) -> bpy.types.Object:
    """
    Place a new cube in Blender with specified coordinates (x, y).

    The function creates a cube object with dimensions of 2 units in all directions.
    It places the cube at the origin by default.

    Args:
        x (float): The X-coordinate where the cube will be placed.
        y (float): The Y-coordinate where the cube will be placed.

    Returns:
        bpy.types.Object: The newly created and placed cube object.

    Special cases:
        - If no coordinates are provided, the cube defaults to being at the origin (0.0, 0.0).
        - If the function is called without Blender initialized, it will raise an error.
    """
```
    Examples

    ```python
# Basic usage
place_cube(cube_id=1, x=5, y=3)

# Explanation:
# This function places a cube with ID 1 at the position (x=5, y=3) in the game world.
# It is designed to be called when the player wants to place an item.

# Edge case
place_cube(cube_id=2, x=-1, y=-1)

# Explanation:
# This function attempts to place a cube with ID 2 at a position (x=-1, y=-1), which is outside the valid range for cube placement.
# It will raise an error indicating that the coordinates are out of bounds.

# Advanced scenario
place_cube(cube_id=3, x=10, y=10, orientation='diagonal')

# Explanation:
# This function places a cube with ID 3 at the position (x=10, y=10) and sets its orientation to diagonal.
# It is useful for creating more complex structures or puzzles in the game.
    Docstring

    """```python
def place_cube(x, y):
    """Add a cube to the scene at the specified (x, y) location.

    Parameters:
        x (float): The X coordinate for the center of the cube.
        y (float): The Y coordinate for the center of the cube.

    Returns:
        None

    Examples:
        >>> place_cube(1.0, 2.0)
        A cube is added to the scene at the position (1.0, 2.0, 0.0).
    """
```"""
    ```