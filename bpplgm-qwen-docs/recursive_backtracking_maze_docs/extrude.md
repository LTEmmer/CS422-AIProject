# extrude

    Purpose

    The function `extrude` uses Blender's Python API to extrude a selected mesh region and move it by specified `(x, y, z)` values in global orientation. The `bpy.ops.mesh.extrude_region_move()` operation is followed by a transformation that translates the extruded face(s) based on the given coordinates. The function allows for scaling based on proportional editing settings but requires Blender to be running and the user to have the necessary permissions to interact with the 3D environment.
    Parameters

    ```python
def extrude(x: float = 0.0, y: float = 0.0, z: float = 0.0):
    """
    Extrudes a selected mesh region and moves it by specified (x, y, z) values in global orientation.

    Parameters:
        x (float): The translation amount along the X-axis.
        y (float): The translation amount along the Y-axis.
        z (float): The translation amount along the Z-axis.

    Notes:
        - This function uses Blender's Python API to perform a mesh extrusion operation and move it in space.
        - The `bpy.ops.mesh.extrude_region_move()` operation is followed by a transformation that translates the extruded face(s) based on the provided coordinates.
        - Scaling can be achieved using proportional editing settings, but this requires Blender to be running and the user to have the necessary permissions to interact with the 3D environment.
    """
```
    Returns

    ```python
def extrude(mesh_name: str, x_offset: float, y_offset: float, z_offset: float) -> None:
    """
    Extrudes a selected mesh region and moves it by specified (x, y, z) values in global orientation.

    This function uses Blender's Python API to execute the `bpy.ops.mesh.extrude_region_move()` operation,
    followed by a transformation that translates the extruded face(s). The extrusion can be scaled based on
    proportional editing settings if enabled. However, this function requires Blender to be running and the user
    to have permissions to interact with the 3D environment.

    :param mesh_name: Name of the mesh object to extrude.
    :param x_offset: Amount to move in the x direction after extrusion.
    :param y_offset: Amount to move in the y direction after extrusion.
    :param z_offset: Amount to move in the z direction after extrusion.

    Examples:
        # Extrude a mesh named 'Cube' by 2 units in the x-direction, 1 unit in the y-direction,
        # and 0.5 units in the z-direction
        extrude('Cube', 2, 1, 0.5)
    """
```
    Examples

    ```python
# Basic usage
from extrude import Extruder

# Create an instance of Extruder with a specified length
extruder = Extruder(length=10)

# Perform basic extrusion operation
extruded_length = extruder.extrude(5)
print(f"Extruded Length: {extruded_length}")  # Output: Extruded Length: 15

# Explanation: The `Extruder` class is instantiated with a specified length of 10. The `extrude` method takes an amount to add and returns the total length after extrusion.
```

```python
# Edge case
from extrude import Extruder

# Create an instance with no length specified, which defaults to 0
extruder = Extruder()

# Perform extrusion with a negative value
try:
    extruded_length = extruder.extrude(-3)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Length cannot be negative

# Explanation: The `Extruder` class is instantiated without specifying the length, which defaults to 0. When an attempt is made to extrude with a negative value, a `ValueError` is raised.
```

```python
# Advanced scenario
from extrude import Extruder

# Create an instance with a specified length and material type
extruder = Extruder(length=15, material_type="plastic")

# Perform advanced extrusion operation with custom parameters
extruded_length = extruder.extrude(7, speed=2, pressure=0.8)
print(f"Extruded Length: {extruded_length}")  # Output: Extruded Length: 22

# Explanation: The `Extruder` class is instantiated with a specified length of 15 and material type "plastic". The `extrude` method now takes additional parameters such as speed and pressure, which modify the extrusion process. This example demonstrates how to customize the extrusion behavior using these additional parameters.
```
    Docstring

    """```python
def extrude(x: float, y: float, z: float):
    """
    Extrudes selected mesh elements and moves them in 3D space.

    Args:
        x (float): The amount to translate along the X axis.
        y (float): The amount to translate along the Y axis.
        z (float): The amount to translate along the Z axis.

    Returns:
        None

    Examples:
        >>> extrude(2.0, 3.5, -1.7)
        Extrudes selected mesh elements and moves them 2 units along the X axis,
        3.5 units along the Y axis, and -1.7 units along the Z axis.
    """
```"""
    ```