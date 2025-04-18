# extrude_right

    Purpose

    The purpose of this function is to execute a series of extrusion commands with specified parameters, likely in a 3D modeling or rendering context.

```python
def extrude_right():
    extrude(x_move_distance, 0.0, 0)
```

Examples:

```python
extrude_right()
```
This will execute the command `extrude(x_move_distance=1.5, y_move_distance=2.0, z_move_distance=3.0)`.

```python
extrude_right(4.8, 6.0, -7.2)
```
    Parameters

    ```python
def extrude_right(
    # x_move_distance (float): The distance to move along the x-axis before performing an extrusion command.
    extrude(x_move_distance=0.0,
            # y_move_distance (float): The distance to move along the y-axis before performing an extrusion command.
            y_move_distance=0.0,  # Default value for z_move_distance
            # z_move_distance (float): The distance to move along the z-axis before performing an extrusion command.
            z_move_distance=0.0)
):
    """
    Execute a series of extrusion commands with specified parameters.

    This function likely in a 3D modeling or rendering context, and is intended for use in
    contexts where complex shapes need to be created by stacking multiple units.

    Parameters
    ----------
    extrude(x_move_distance : float, optional): The distance to move along the x-axis before performing an extrusion command.
        Default value: 0.0

    y_move_distance : float, optional: The distance to move along the y-axis before performing an extrusion command.
        Default value: 0.0

    z_move_distance : float, optional: The distance to move along the z-axis before performing an extrusion command.
        Default value: 0.0

    Returns
    -------
    None
    """

    # Provide documentation for each parameter
    params = {
        'extrude(x_move_distance)': {
            'name': 'x_move_distance',
            'type': 'float',
            'description': 'The distance to move along the x-axis before performing an extrusion command.',
            'usage_constraints': (
                'Must be a non-negative number.',
                'Extrusion commands can only be used for positive distances.'
            )
        },
        'y_move_distance': {
            'name': 'y_move_distance',
            'type': 'float',
            'description': 'The distance to move along the y-axis before performing an extrusion command.',
            'usage_constraints': (
                'Must be a non-negative number.',
                'Extrusion commands can only be used for positive distances.'
            )
        },
        'z_move_distance': {
            'name': 'z_move_distance',
            'type': 'float',
            'description': 'The distance to move along the z-axis before performing an extrusion command.',
            'usage_constraints': (
                'Must be a non-negative number.',
                'Extrusion commands can only be used for positive distances.'
            )
        }
    }

    # Print documentation for each parameter
    print("Parameters:")
    for param in params:
        print(f"{param}:")
        print(f"  name: {params[param]['name']}")
        print(f"  type: {params[param]['type']}")
        print(f"  description: {params[param]['description']}")
        print(f"  usage_constraints: ({', '.join(params[param]['usage_constraints'])})")
    Returns

    ```python
def extrude_right():
    """
    Execute a series of extrusion commands with specified parameters.

    This function is designed to be used in 3D modeling or rendering contexts to create three-dimensional shapes.
    
    Returns:
        list: A list of return values from the extruded commands. Each value represents the change made to the model
              as a result of the corresponding extrusion command.

    Description:
        The purpose of this function is to execute a series of extrusion commands with specified parameters, likely in a 
        3D modeling or rendering context. It takes into account the specific parameters for each extrusion command and 
        returns the changes made to the model as a result of these commands.

    Special cases:
        None
```
    Examples

    ```python
# Basic usage
def extrude_right(surface, angle):
    """
    Extrudes the surface along the right edge by a specified angle.

    Args:
        surface (Surface): The surface to be extruded.
        angle (float): The angle of extrusion in degrees.

    Returns:
        ExtrudedSurface: A new Surface object representing the extruded surface.
    """
    return surface.extrude_right(angle)

# Edge case
def extrude_right_negative_angle(surface):
    """
    Extrudes the surface along its negative right edge, which is opposite to the normal direction.

    Args:
        surface (Surface): The surface to be extruded.

    Returns:
        ExtrudedSurface: A new Surface object representing the extruded surface.
    """
    return surface.extrude_right(-angle)

# Advanced scenario
def extrude_right_with_offset(surface, offset):
    """
    Extrudes the surface along its right edge by a specified angle while also applying an offset to it.

    Args:
        surface (Surface): The surface to be extruded.
        offset (float): The amount of offset applied to the surface.

    Returns:
        ExtrudedSurface: A new Surface object representing the extruded surface with offset.
    """
    return surface.extrude_right(offset)
```
    Docstring

    """```python
def extrude_right(x_move_distance: float, x_scale: float = 1.0, y_offset: float = 0.0) -> None:
    """
    Exports a 3D point in the positive z-direction by moving it to the right by `x_move_distance` units.

    This function is used as an intermediate step in creating extrusions of 3D objects or shapes.

    :param x_move_distance: The distance to move the point to the right (in units)
    :type x_move_distance: float
    :param y_offset: An optional offset from the center plane (default is 0.0, meaning no offset)
    :type y_offset: float (default=0.0)
    :return: None
    """
```"""
    ```