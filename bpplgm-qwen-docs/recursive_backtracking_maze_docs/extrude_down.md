# extrude_down

    Purpose

    The `extrude_down` function is designed to extrude a model along the z-axis by moving it downwards by a specified distance.
    Parameters

    ```python
def extrude_down(model: dict, distance: float) -> dict:
    """
    Extrudes a 3D model downwards along the z-axis.

    Parameters:
    - model (dict): A dictionary representing the 3D model with 'vertices' and 'faces'.
      Each vertex is represented as a tuple of (x, y, z) coordinates.
      Each face is represented as a list of indices into the 'vertices' list.
    - distance (float): The amount by which to move each vertex downwards.

    Returns:
    dict: A new model with all vertices moved along the z-axis by the specified distance.

    Usage Constraints:
    - Ensure that the input model dictionary has valid 'vertices' and 'faces'.
    - The 'distance' must be a positive number.
    """
```
    Returns

    ```python
def extrude_down(model, distance):
    """
    Extrudes a model along the z-axis by moving it downwards by a specified distance.

    Args:
    model (Model): The 3D model to be extruded.
    distance (float): The amount of distance to move the model downwards along the z-axis.

    Returns:
    Model: A new model that is an extrusion of the original model down by the specified distance.
    """
    # Assuming 'extrude_down' moves each point in the model's vertices by a fixed amount along the z-axis
    extruded_model = model.clone()  # Clone the original model to avoid modifying it directly

    for vertex in extruded_model.vertices:
        vertex.position.z -= distance  # Move the vertex downwards by the specified distance

    return extruded_model
```

**Special Cases:**
- If `distance` is zero, the function returns a copy of the original model without any modifications.
- The function assumes that the vertices of the model are represented as objects with a `position` attribute which is a 3D vector.
    Examples

    ```python
# Basic usage: Extrude a single object downwards by 5 units
extrude_down(my_object, distance=5)
```
This function `extrude_down` takes an object and an optional `distance` parameter (default is 1). It moves the specified object downward by the given number of units. For example:
```python
# Example: Extruding a cube downwards
cube = create_cube()
extrude_down(cube, distance=5)
```

```python
# Edge case: Extruding an empty collection
try:
    extrude_down([])
except ValueError as e:
    print(e)  # Expected error message for empty input
```
This example demonstrates how the function handles errors with invalid inputs. When `extrude_down` is called with an empty list, it raises a `ValueError`.
    Docstring

    """A function to extrude geometry downwards by a specified distance.

Args:
    None

Returns:
    None

Examples:
    To extrude a mesh downward by 2 units:

        extrude_down()
    ```"""
    ```