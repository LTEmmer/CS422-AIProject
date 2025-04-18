# extrude_up

    Purpose

    This function defines a simple extrusion action that moves an object in the Y-axis by a specified `y_move_distance`. The coordinates for movement are (0, y_move_distance, 0), meaning it will move along the Y-axis without changing its X or Z position.
    Parameters

    ```python
def extrude_up(y_move_distance: float) -> None:
    """
    Function purpose: This function defines a simple extrusion action that moves an object in the Y-axis by a specified `y_move_distance`. The coordinates for movement are (0, y_move_distance, 0), meaning it will move along the Y-axis without changing its X or Z position.

    Parameters:
        y_move_distance (float): The distance to move the object in the Y-axis. This value can be positive for upward movement or negative for downward movement.
    """
    # Example usage of extrude_up
    extrude_up(5)  # Moves the object 5 units along the Y-axis
```
    Returns

    ```python
def extrude_up(y_move_distance: float) -> None:
    """
    This function defines a simple extrusion action that moves an object in the Y-axis by a specified `y_move_distance`. The coordinates for movement are (0, y_move_distance, 0), meaning it will move along the Y-axis without changing its X or Z position.

    Parameters:
        y_move_distance (float): The distance to move the object in the Y-axis. A positive value moves upwards, and a negative value moves downwards.

    Returns:
        None: This function does not return any value as it directly modifies the movement of an object.

    Special Cases:
        - If `y_move_distance` is 0, the object will remain stationary along the Y-axis.
        - If `y_move_distance` is not a finite number (e.g., infinity), the behavior is undefined and may result in unexpected movements or errors.
    """
```
    Examples

    ```python
# Basic usage: Extrude a cube upwards by 5 units.
extrude_up(cube_mesh, amount=5)
```
This function takes a mesh object and an optional `amount` parameter (default is 1). It increases the height of each vertex in the mesh by the specified amount, effectively extruding it upwards. If no amount is provided, it defaults to extruding by 1 unit.

```python
# Edge case: Extrude a single point upwards.
extrude_up(point_mesh, amount=5)
```
This function can handle an input with only one vertex, such as a single point. When the `amount` parameter is used, it will increase the height of the point by 5 units.

```python
# Advanced scenario: Extrude multiple meshes and apply different amounts.
extrude_up([cube_mesh, sphere_mesh], [3, 2])
```
In this advanced scenario, an array of mesh objects is provided along with an array of corresponding `amount` values. The function will extrude each mesh individually by the specified amount. If a mesh does not have a matching amount value in the array, it will use the default amount (1). This allows for flexible and customizable extrusion of multiple meshes simultaneously.
    Docstring

    """```python
def extrude_up():
    """
    Extrudes a block upwards by a specified distance.

    Args:
        y_move_distance (float): The distance to move the block upwards.

    Returns:
        None

    Examples:
        >>> extrude_up(y_move_distance=5)
        This will extrude a block upwards by 5 units.
    """
```"""
    ```