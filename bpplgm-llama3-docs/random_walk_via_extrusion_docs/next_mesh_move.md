# next_mesh_move

    Purpose

    ## Purpose of the Code

This Python function, named `next_mesh_move`, appears to be part of a 3D modeling or animation application. It is designed to handle user input (direction) and move the next mesh face based on the input direction.

## Functionality Documentation

### main loop

The function iterates through each face in the mesh using a `for` loop. For each face, it sets all faces to be unselected (`select = False`). The code then checks if the current position of `x_pos` and `y_pos` are valid based on user input direction.

### Extrusion logic

Depending on the user's input direction, the function attempts to:

* Move the next mesh face up (or down) using the `extrude_up()` or `extrude_down()` functions.
* Move the next mesh face right (or left) using the `extrude_right()` or `extrude_left()` functions.

In all cases, if a valid position is found for the current face, it is selected and the corresponding face is set as the new "next" face.
    Parameters

    ```python
def next_mesh_move(direction):
    """
    Handles user input direction to move the next mesh face.

    Parameters:
    direction (str): Direction to move the next mesh face based on ('up', 'down' for extrusion, 
                      'right', 'left' for extrusion)

    Returns:
        None

    Notes:
        The function iterates through each face in the mesh and checks if a valid position is found.
        Based on user input direction, it attempts to move the next mesh face up or down using
        `extrude_up()` or `extrude_down()`, or right or left using `extrude_right()` or `extrude_left().
        If a valid position is found, the corresponding face is selected and set as the new "next" face.

    Constraints:
        The function assumes that there are two sets of faces ('up' and 'down') and two sets of
        edges (right and left) for each mesh.
    """
```

```python
# Main loop

def main_loop(mesh, x_pos, y_pos):
    # Iterate through each face in the mesh using a for loop
    for i in range(len(mesh)):
        # Set all faces to be unselected (`select = False`)
        for j in range(len(mesh[i])):
            mesh[i][j].select = False
        
        # Check if the current position of `x_pos` and `y_pos` are valid based on user input direction
        # The constraints assume that there are two sets of faces ('up' and 'down') and two sets of edges (right and left) for each mesh
        if x_pos > 0:  # Check the right edge
            next_face = extrude_right(mesh, i, j)
            mesh[i][j].select = True
            mesh[next_face[1]].select = True
        
        elif y_pos < 0:  # Check the down edge
            next_face = extrude_down(mesh, i, j)
            mesh[i][j].select = True
            mesh[next_face[1]].select = True
    
    return mesh
```
    Returns

    ### return value for 'next_mesh_move'

The return value for the `next_mesh_move` function is a tuple containing two boolean values:

*   `select`: A boolean indicating whether the selected face should be set as the next face.
*   `next_face`: The index of the next face in the mesh to move.

### Purpose of the Code

## main loop

The function iterates through each face in the mesh using a `for` loop. For each face, it sets all faces to be unselected (`select = False`). The code then checks if the current position of `x_pos` and `y_pos` are valid based on user input direction.

### Extrusion logic

Depending on the user's input direction, the function attempts to:

*   Move the next mesh face up (or down) using the `extrude_up()` or `extrude_down()` functions.
*   Move the next mesh face right (or left) using the `extrude_right()` or `extrude_left()` functions.

In all cases, if a valid position is found for the current face, it is selected and the corresponding face is set as the new "next" face.
    Examples

    ```python
# Basic usage
def next_mesh_move(current_position: tuple[float], current_direction: str) -> tuple[float, str]:
    """
    Generates the next mesh move based on the current position and direction.

    Args:
        current_position (tuple[float]): The current position in 2D space as a tuple of two floats.
        current_direction (str): The current direction in 3D space as a string ("N", "S", "E", or "W").

    Returns:
        tuple[float, str]: A tuple containing the next mesh move coordinates and direction.

    Example:
    ```python
current_position = (0.5, 0.2)
direction = 'N'
next_move = next_mesh_move(current_position, direction)
print(next_move)  # Output: (1.0, 0.3, 'S')
```

    """
    # Edge case: invalid input
def next_mesh_move_invalid_input(current_position: tuple[float], current_direction: str) -> None:
    """
    Raises an error if the input is invalid.

    Args:
        current_position (tuple[float]): The current position in 2D space as a tuple of two floats.
        current_direction (str): The current direction in 3D space as a string ("N", "S", "E", or "W").

    Raises:
        ValueError: If the input is invalid.

    Example:
    ```python
try:
    next_mesh_move(current_position, 'Z')
except ValueError as e:
    print(e)  # Output: Input must be a tuple of two floats.
```

    """
    # Advanced scenario: calculate mesh movement based on Euler angles
def next_mesh_move_euler_angles(current_position: tuple[float], current_direction: str, euler_angles: dict[str, float]) -> tuple[float, str]:
    """
    Generates the next mesh move based on the current position and direction, taking into account Euler angles.

    Args:
        current_position (tuple[float]): The current position in 2D space as a tuple of two floats.
        current_direction (str): The current direction in 3D space as a string ("N", "S", "E", or "W").
        euler_angles (dict[str, float]): A dictionary containing Euler angles in radians.

    Returns:
        tuple[float, str]: A tuple containing the next mesh move coordinates and direction.

    Example:
    ```python
import math

euler_angles = {'x': 0.5, 'y': 1.2}
next_move = next_mesh_move_euler_angles(current_position, current_direction, euler_angles)
print(next_move)  # Output: (1.0, 0.3, 'S')
```
    Docstring

    """```python
def next_mesh_move(direction):
    """
    Moves to the next mesh face in a specified direction.

    Args:
        direction (str): The direction to move ('up', 'right', 'down', or 'left')

    Returns:
        None
    """
```

**Description:**

This function iterates through each face of the current mesh and sets its selection state. It then uses various geometric calculations to determine which face should be selected next based on the user's input direction.

**Documentation:**

* Iterates through each face of the current mesh, setting its selection state.
* Uses a combination of geometric calculations (`calc_center_median`) to determine which face should be selected next in each specified direction ('up', 'right', 'down', or 'left').
* Moves to the next face in the specified direction based on the calculated selection.

**Examples:**

```python
# Move up
next_mesh_move('up')
```

This will start extruding from the current face, incrementing `y_pos` by `y_move_distance`."""
    ```