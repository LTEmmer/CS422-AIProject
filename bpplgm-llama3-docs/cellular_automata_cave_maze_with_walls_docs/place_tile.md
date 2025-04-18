# place_tile

    Purpose

    The `place_tile` function creates a new 2D plane object in the 3D space using Blender's Python API (`bpy`) and places it at the specified coordinates `(x, y)`.

### Examples
```python
import bpy

# Place a tile at coordinates (100, 200)
bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(100, 200, -1))
```
or
```python
# Place two tiles side by side in the middle of the screen at coordinates (300, 400)
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(300, 400, -1))
```
    Parameters

    ```python
def place_tile(
    x: float,  # The x-coordinate in 3D space where to place the tile.
    y: float   # The y-coordinate in 3D space where to place the tile.
):
    """
    Creates a new 2D plane object in Blender's Python API (`bpy`) and places it at the specified coordinates `(x, y)`.

    Parameters
    ----------
    x : float
        The x-coordinate in 3D space where to place the tile. Must be non-negative.
    
    y : float
        The y-coordinate in 3D space where to place the tile. Must be non-negative.
        
    Examples
    --------
    Place a tile at coordinates (100, 200)
    bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(100, 200, -1))
    
    Place two tiles side by side in the middle of the screen at coordinates (300, 400)
    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(300, 400, -1))
    """
```
    Returns

    ### place_tile Function

#### return value

```python
return bpy.context.scene.objects.new('place_tile', {'data': {'type': 'Plane'}})
```

#### Description

The `place_tile` function creates a new 2D plane object in the 3D space using Blender's Python API (`bpy`) and places it at the specified coordinates `(x, y)`.

#### Examples
```python
import bpy

# Place a tile at coordinates (100, 200)
bpy.ops.mesh.primitive_plane_add(size=5, enter_editmode=False, location=(100, 200, -1))
```
or
```python
# Place two tiles side by side in the middle of the screen at coordinates (300, 400)
bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(300, 400, -1))
```
    Examples

    ```python
def place_tile(tile_name: str, tile_size: int) -> None:
    """
    Places a tile at the specified location on the map.

    Args:
        tile_name (str): The name of the tile to be placed.
        tile_size (int): The size of the tile in pixels.

    Returns:
        None
    """
    # Explanation
    print(f"Place {tile_name} tile at ({tile_size}, {tile_size})")

def place_tile_at_edge(x: int, y: int) -> None:
    """
    Places a tile at an edge location on the map.

    Args:
        x (int): The x-coordinate of the edge location.
        y (int): The y-coordinate of the edge location.

    Returns:
        None
    """
    # Explanation
    print(f"Place {x}x{y} tile at ({x}, {y})")

def place_tile_at_edge_with_size(x: int, y: int, size: int) -> None:
    """
    Places a tile at an edge location on the map with a specified size.

    Args:
        x (int): The x-coordinate of the edge location.
        y (int): The y-coordinate of the edge location.
        size (int): The size of the tile in pixels.

    Returns:
        None
    """
    # Explanation
    print(f"Place {x}x{y} tile at ({x}, {y}) with size {size}")
```
    Docstring

    """```python
def place_tile(x: float, y: int) -> None:
    """
    Place a plane at a specified location.

    Creates a new plane with a size of 2 units and enters edit mode. The plane is placed at coordinates (x, y, -1).

    Args:
        x (float): The x-coordinate of the plane's location.
        y (int): The y-coordinate of the plane's location.

    Returns:
        None

    Examples:
        >>> place_tile(10, 20)
        A plane at (10.0, 20.0) has been created and placed in edit mode.
    ```"""
    ```