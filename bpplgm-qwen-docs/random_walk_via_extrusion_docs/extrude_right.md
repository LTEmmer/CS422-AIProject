# extrude_right

    Purpose

    The `extrude_right` function executes an extrusion operation along the right axis by moving a specified distance in the positive x-direction without changing the y or z coordinates.
    Parameters

    Certainly! Here is the Google-style docstring for the `extrude_right` function, along with examples using the existing code:

```python
def extrude_right(distance):
    """
    Execute an extrusion operation along the right axis by moving a specified distance in the positive x-direction without changing the y or z coordinates.

    Parameters:
    - distance (float): The distance to move along the positive x-axis. Must be non-negative.

    Usage Constraints:
    - The `distance` parameter must be a non-negative float.
    """
    # Example usage
    extrude_right(5.0)  # Move 5 units in the positive x-direction

    # Expected output: [x=5.0, y=0.0, z=0.0]
```

This docstring describes the purpose of the function and provides detailed information about its parameters, their types, descriptions, and usage constraints. The example usage demonstrates how to call the function with a specific distance, and it includes expected output for clarity.
    Returns

    The `extrude_right` function executes an extrusion operation along the right axis by moving a specified distance in the positive x-direction without changing the y or z coordinates. The function takes two arguments: `dx`, which represents the distance to move in the x direction, and `current_position`, which is a tuple representing the current position of the object being extruded (x, y, z). The function returns a new tuple representing the updated position of the object after the extrusion.

Return type: Tuple[float, float, float]

Description: The function returns a new tuple containing the x-coordinate incremented by `dx`, while the y and z coordinates remain unchanged. This effectively moves the object along the right axis by the specified distance.

Special cases:
- If `dx` is negative, it will move the object to the left instead of moving it to the right.
- The function assumes that the input position tuple is in the form (x, y, z).
    Examples

    ```python
# Basic usage: Extrude a rectangle along the x-axis by 5 units.
rectangle = Rectangle((0, 0), (10, 2))
extruded_rectangle = extrude_right(rectangle, 5)
print(extruded_rectangle)

# Edge case: Extruding a line does not change it as lines are one-dimensional.
line = Line((0, 0), (10, 0))
extruded_line = extrude_right(line, 5)
print(extruded_line)

# Advanced scenario: Extruding an irregular polygon by different amounts for each side.
polygon = Polygon([(0, 0), (4, 0), (4, 3), (0, 3)])
extruded_polygon = extrude_right(polygon, [1, 2, 3, 4])
print(extruded_polygon)
```
    Docstring

    """```python
def extrude_right(x_move_distance):
    """
    Perform an extrusion operation on the model along the right axis.

    Args:
        x_move_distance (float): The distance to move along the X-axis during the extrusion.

    Returns:
        None: This function does not return a value.

    Examples:

    >>> extrude_right(10)
    Move the model 10 units to the right and extrude.
    """
```"""
    ```