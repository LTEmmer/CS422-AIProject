# add_cubes

    Purpose

    ---
    This function adds cubes to a Blender scene based on the provided cell map, where False represents a blank cell.

    It iterates through each cell in the map, where True values represent populated cells. For cells that are populated, it creates a cube of size 2 at the cell's location.

    ## Parameters
    - `cell_map`: A nested list representing the cell map, where True represents a populated cell.

    ## Modifies Blender
    - Adds cubes to the Blender scene for each populated cell based on the provided cell map.

    ## Return Value
    None

    ## Example Usage
    ```python
    cell_map = [
        [False, False, True, False, False, False],
        [False, False, False, False, True, False],
        [True, True, True, True, True, False],
        [False, True, False, True, False, True],
        [False, True, True, False, True, False],
        [False, True, False, True, False, False]
    ]

    add_cubes(cell_map)
    ```
    """
    This function takes a cell map and adds cubes to Blender for each populated cell in the map.

    ## Parameters
    - `cell_map`: A nested list representing the cell map, where True represents a populated cell.

    ## Modifies Blender
    - Adds cubes to the Blender scene for each populated cell based on the provided cell map.

    ## Return Value
    None

    ## Example Usage
    ```python
    cell_map = [
        [False, False, True, False, False, False],
        [False, False, False, False, True, False],
        [True, True, True, True, True, False],
        [False, True, False, True, False, True],
        [False, True, True, False, True, False],
        [False, True, False, True, False, False]
    ]

    add_cubes(cell_map)
    ```
    """
    This function takes a cell map and adds cubes to Blender for each populated cell in the map.

    ## Parameters
    - `cell_map`: A nested list representing the cell map, where True represents a populated cell.

    ## Modifies Blender
    - Adds cubes to the Blender scene for each populated cell based on the provided cell map.

    ## Return Value
    None

    ## Example Usage
    ```python
    cell_map = [
        [False, False, True, False, False, False],
        [False, False, False, False, True, False],
        [True, True, True, True, True, False],
        [False, True, False, True, False, True],
        [False, True, True, False, True, False],
        [False, True, False, True, False, False]
    ]

    add_cubes(cell_map)
    ```
    """
    This function takes a cell map and adds cubes to Blender for each populated cell in the map.

    ## Parameters
    - `cell_map`: A nested list representing the cell map, where True represents a populated cell.

    ## Modifies Blender
    - Adds cubes to the Blender scene for each populated cell based on the provided cell map.

    ## Return Value
    None

    ## Example Usage
    ```python
    cell_map = [
        [False, False, True, False, False, False],
        [False, False, False, False, True, False],
        [True, True, True, True, True, False],
        [False, True, False, True, False, True],
        [False, True, True, False, True, False],
        [False, True, False, True, False, Fals
    Parameters

    """
    This function takes a cell map and adds cubes to Blender for each po
    Returns

    """
    Examples

    The code is not meant to be used as-is, but should be well-formed and easily runnable.

    Ensure that each example has a unique, distinct, and executable code block.
    Write any supplementary explanations in a markdown cell (you can also add markdown blocks in-between).
    Include any code comments and/or documentation throughout the code.
    Ensure your examples are readable and well-formatted, especially when the code is poorly-formatted.

    For each code block, start with a brief explanation, followed by a code block (as an inline code block).
    If the code block is a function call, enclose it in parentheses.
    If the code block is a variable assignment, enclose it in curly braces.
    For example,
    ```python
    def add_cubes(x, y):
        return x + y
    ```
    becomes,
    ```python
    (x + y)
    ```
    This ensures that the code is easily runnable.

    Ensure that the code block is runnable before submitting the examples.

    Use markdown cells to explain any code blocks that are being used.

    Additionally, consider the scenarios and code blocks provided below and describe any changes you'd make based on them.

    Scenario:
    Given that the function ```add_cubes``` is defined as ```def add_cubes(x, y):```
    When I call ```add_cubes(1, 2)```
    Then I should get an output of ```3```

    Scenario:
    Given that the function ```add_cubes``` is defined as ```def add_cubes(x, y):```
    When I call ```add_cubes(1, 2)```
    Then I should get an output of ```3```

    Scenario:
    Given that the function ```add_cubes``` is defined as ```def add_cubes(x, y):```
    When I call ```add_cubes(1, 2)```
    Then I should get an output of ```3```

    Scenario:
    Given that the function ```add_cubes``` is defined as ```def add_cubes(x, y):```
    When I call ```add_cubes(1, 2)```
    Then I should get an output of ```3```

    Scenario:
    Given that the function ```add_cubes``` is defined as ```de
    Docstring

    """@param cell_map 2D array of cells. Empty cells are False, True is cube placed.
    @param WIDTH Number of cells in a side of a cube map.
    """
    ```

    ```python
    def add_cubes(cell_map):
    """Add cubes to mesh

    Parameters
    ----------
    cell_map : numpy.ndarray
        2D array of cells. Empty cells are False, True is cube placed.
    """
    matrix_size = WIDTH
    for i in range(matrix_size**2):
        y = math.floor(i / matrix_size)
        x = i - y * matrix_size
        if y > 1 and x == 0:
            cleanup_mesh()
        if cell_map[y][x] is False:  # cells with value True get cubes placed on them
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))
    """
    ```
    ```python
    def add_cubes(cell_map):
    """Add cubes to mesh

    Parameters
    ----------
    cell_map : numpy.ndarray
        2D array of cells. Empty cells are False, True is cube placed.
    """
    matrix_size = WIDTH
    for i in range(matrix_size**2):
        y = math.floor(i / matrix_size)
        x = i - y * matrix_size
        if y > 1 and x == 0:
            cleanup_mesh()
        if cell_map[y][x] is False:  # cells with value True get cubes placed on them
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, location=(x*2, y*2, 0))
    """
    ```
    ```python
    def add_cubes(cell_map):
    """Add cubes to mesh

    Parameters
    ----------
    cell_map : numpy.ndarray
        2D array of cells. Empty cells are False, True is cube placed.
    """
    matri"""
    ```