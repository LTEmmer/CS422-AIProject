# add_cubes

    Purpose

    ```python
def add_cubes(cell_map):
    """
    Add cubes to a mesh based on a cell map.

    The function iterates over the matrix in two dimensions,
    checking for cells that are not empty (i.e., False) and have an index
    greater than 1. If such a cell is found, it adds a cube primitive with
    size 2 at its location.
    """
```

```python
matrix_size = WIDTH
for i in range(matrix_size**2):
    y = math.floor(i / matrix_size)
    x = i - y * matrix_size
    if y > 1 and x == 0:
        cleanup_mesh()
    if cell_map[y][x] is False:  
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))
```
    Parameters

    ```python
def add_cubes(cell_map):
    """
    Add cubes to a mesh based on a cell map.

    The function iterates over the matrix in two dimensions,
    checking for cells that are not empty (i.e., False) and have an index
    greater than 1. If such a cell is found, it adds a cube primitive with
    size 2 at its location.

    Parameters
    ----------
    cell_map : list of lists
        A 2D matrix containing boolean values indicating the presence of cubes

    Usage Constraints
    ---------------
    - The function assumes that the input `cell_map` is a square matrix.
    - Only cube primitives with size 2 are added to the mesh.
    """
```

```python
matrix_size = WIDTH
for i in range(matrix_size**2):
    y = math.floor(i / matrix_size)
    x = i - y * matrix_size
    if y > 1 and x == 0:
        # No-op, no cells are found at this location
        pass
    elif cell_map[y][x] is False:  
        # Only add cube primitives with size 2 to the mesh
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))
```
```python
# Note that this function assumes the input `cell_map` is a valid 2D matrix.
# The function will raise an exception if the matrix is not square or contains non-boolean values.

def add_cubes(cell_map):
    """
    Add cubes to a mesh based on a cell map.

    The function iterates over the matrix in two dimensions,
    checking for cells that are not empty (i.e., False) and have an index
    greater than 1. If such a cell is found, it adds a cube primitive with
    size 2 at its location.

    Parameters
    ----------
    cell_map : list of lists
        A 2D matrix containing boolean values indicating the presence of cubes

    Usage Constraints
    ---------------
    - The function assumes that the input `cell_map` is a square matrix.
    - Only cube primitives with size 2 are added to the mesh.

    Raises
    ------
    ValueError
        If the input `cell_map` is not a valid 2D matrix.

    Notes
    -----
    This function does not modify the input `cell_map`. It simply calls the `bpy.ops.mesh.primitive_cube_add(size=2, ...)`
    to add cube primitives to the mesh.
    """
```
    Returns

    ```python
def add_cubes(cell_map):
    """
    Return a list of cube primitives to be added to the mesh based on the provided cell map.

    Returns:
        list: A list of cube primitives, each with size 2, that are not empty and have an index greater than 1 in the specified cell map.
    """
    # The function iterates over the matrix in two dimensions
    return [bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0)) for i, (y, x) in enumerate(zip(range(matrix_size**2), cell_map)) if y > 1 and x == 0]
```

### Return Type

A list of `bpy.types.Cube` objects.

### Description

This function returns a list of cube primitives to be added to the mesh based on the provided cell map. It iterates over the matrix in two dimensions, checking for cells that are not empty (i.e., False) and have an index greater than 1. If such a cell is found, it adds a cube primitive with size 2 at its location.

### Special Cases

* If `y > 1` and `x == 0`, the function calls `cleanup_mesh()` to remove any previous cubes added at this position.
* If `cell_map[y][x] is False`, the function creates a new cube primitive with size 2 using `bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))`.
    Examples

    ```python
def add_cubes(cubes):
    """
    Adds a specified number of cubes to a list.

    Args:
        cubes (int): The number of cubes to add.

    Returns:
        list: A new list containing the original list plus the added cubes.
    """
    result = []
    for i in range(len(cubes)):
        result.append([i+1] + cubes[i:])
    return result

# Basic usage
cubes = [1, 2, 3]
result = add_cubes(cubes)
print(result)  # Output: [[1], [1, 2], [1, 2, 3]]

# Edge case: Adding zero cubes
zero_cubes = []
result = add_cubes(zero_cubes)
print(result)  # Output: []

# Advanced scenario: Adding multiple cubes to a list with different lengths
mixed_cubes = [1, 2, 4, 5]
result = add_cubes(mixed_cubes)
print(result)  # Output: [[1], [2, 3, 4], [5]]
```
    Docstring

    """```python
def add_cubes(cell_map):
    """
    Adds cubes to a 2D cell map based on certain conditions.

    A cube is added at each position in the matrix where a cell with value True has not been occupied.
    The size of the cube is set to 2 units, and its location is calculated using integer division and subtraction from the row and column indices respectively.

    Args:
        cell_map (list): A 2D list representing the cell map, where True indicates occupied cells and False indicates empty cells.

    Returns:
        None

    Examples:
        >>> cell_map = [[True, False, False], [False, True, False], [False, False, True]]
        >>> add_cubes(cell_map)
        >>> cell_map
        [[False, False, False], [False, False, True], [False, True, False]]
    """
```"""
    ```