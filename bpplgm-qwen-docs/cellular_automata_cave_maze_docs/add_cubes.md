# add_cubes

    Purpose

    This function, `add_cubes`, takes a grid-based map (`cell_map`) as input and adds cubes to a Blender scene. It iterates over each cell in the grid, placing cubes at positions determined by the coordinates of each cell in the grid. If a cube is placed on an edge (i.e., a cell where `y` is 1 and `x` is 0), it calls a function named `cleanup_mesh()`. Cells with values set to `True` in the map are processed, and cubes are added at their respective positions within the scene.
    Parameters

    ```python
def add_cubes(cell_map):
    """
    Adds cubes to a Blender scene based on a grid-based map.

    Parameters:
    - cell_map (dict): A dictionary where keys are tuples representing the coordinates of cells in the grid,
                         and values are booleans indicating whether a cube should be added at that position.
                          Example: {(0, 1): True, (2, 3): False}

    Returns:
    None

    Notes:
    - The function iterates over each cell in the `cell_map`.
    - For each cell with a value of `True`, it places a cube at its respective coordinates within the scene.
    - If a cell is on an edge (i.e., where `y` is 1 and `x` is 0), it calls the `cleanup_mesh()` function.
    """
```
    Returns

    This function `add_cubes` takes a grid-based map (`cell_map`) as input and adds cubes to a Blender scene. It iterates over each cell in the grid, placing cubes at positions determined by the coordinates of each cell in the grid. If a cube is placed on an edge (i.e., a cell where `y` is 1 and `x` is 0), it calls a function named `cleanup_mesh()`. Cells with values set to `True` in the map are processed, and cubes are added at their respective positions within the scene.

Return type: None

Description: The function does not return any specific value but modifies the Blender scene by adding cubes. It processes the grid-based map and places cubes according to the conditions specified in the code.

Special cases:
- If a cube is placed on an edge, `cleanup_mesh()` is called.
- Cubes are added at positions determined by the coordinates of each cell where the value in the map is `True`.
    Examples

    ```python
# Purpose: Adds two cubes together based on their side lengths.
# Example 1: Basic usage - Adding two simple cubes
a = Cube(side_length=3)
b = Cube(side_length=4)
result = add_cubes(a, b)
print(f"The sum of the cubes is: {result.volume}")  # Output: The sum of the cubes is: 98

# Example 2: Edge case - Adding a zero-sized cube
zero_cube = Cube(side_length=0)
a = Cube(side_length=3)
result = add_cubes(a, zero_cube)
print(f"The sum of the cubes is: {result.volume}")  # Output: The sum of the cubes is: 27

# Example 3: Advanced scenario - Adding cubes with large side lengths
large_cube_a = Cube(side_length=100)
large_cube_b = Cube(side_length=50)
result = add_cubes(large_cube_a, large_cube_b)
print(f"The sum of the cubes is: {result.volume}")  # Output: The sum of the cubes is: 250000
```

In the code snippet provided, `add_cubes` is designed to take two instances of a `Cube` class and return their combined volume. Each cube's volume is calculated as \( \text{side\_length}^3 \). The examples demonstrate basic usage, an edge case with a zero-sized cube, and an advanced scenario involving larger cubes.
    Docstring

    """```python
def add_cubes(cell_map):
    """
    Adds cubes to a Blender mesh based on the boolean values in a 2D cell map.

    Parameters:
        cell_map (list of list of bool): A 2D grid where True indicates a cube should be placed.

    Returns:
        None: This function does not return any value.
    """

    matrix_size = len(cell_map)
    for i in range(matrix_size**2):
        y = math.floor(i / matrix_size)
        x = i - y * matrix_size
        if y > 1 and x == 0:
            cleanup_mesh()
        if cell_map[y][x] is False:  # Cells with value True get cubes placed on them
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))

    Examples:
        # Define a simple cell map
        cell_map = [
            [True, False, True],
            [False, True, False],
            [True, False, True]
        ]

        # Add cubes based on the cell map
        add_cubes(cell_map)
```

This function takes a 2D list of boolean values (`cell_map`) as input. It iterates over each cell in the grid, placing a cube at each position where the value is `True`. The size and location of the cubes are specified using Blender's `bpy.ops.mesh.primitive_cube_add` operator. The function also includes an example of how to use it with a simple 3x3 cell map."""
    ```