# build_walls

    Purpose

    The function above takes a list of walls and places them in a list of visited cells. It then iterates through each position in the list of walls and checks if it is a valid position for a wall. If it is, it creates a wall and adds it to the list of walls.
    
    The function builds walls in a loop where it iterates through each position in the list of walls. The loop then checks if the position is a valid position for a wall by checking if there is a wall at the position or if it is out of bounds. If it is a valid position, it creates a wall and adds it to the list of walls.
    
    Overall, this function is designed to create walls in a list of walls in a loop where it iterates through each position in the list of walls. The loop then checks if the position is a valid position for a wall by checking if there is a wall at the position or if it is out of bounds. If it is a valid position, it creates a wall and adds it to the list of walls.
    
    ```
    Parameters

    Use the following template:

    ### PARAMETER NAME ### (### PARAMETER TYPE ###): ### PARAMETER DESCRIPTION ###
    #### PARAMETER USAGE CONSTRAINTS ####

    Provide a concrete example or set of examples to illustrate
    the parameter usage.

    Here's an example of usage:

    #### PARAMETER USAGE #####
    Returns

    Do not offer suggestions, refactorings, or code improvements.

    Function Purpose:
    The function above takes a list of walls and places them in a list of visited cells. It then iterates through each position in the list of walls and checks if it is a valid position for a wall. If it is, it creates a wall and adds it to the list of walls.

    Parameters:
    walls (list): The list of walls to add to the list of visited cells.

    Return Type:
    list: The list of walls in a loop where it iterates through each position in the list of walls. The loop then checks if the position is a valid position for a wall by checking if there is a wall at the position or if it is out of bounds. If it is a valid position, it creates a wall and adds it to the list of walls.

    Return Value:
    The function builds walls in a loop wh
    Examples

    Make sure to test your example before modifying.

"""

def build_walls(height, width):
    """
    Build a rectangular wall of specified height and width.
    
    Args:
    - height (int): Height of the wall.
    - width (int): Width of the wall.
    
    Returns:
    - str: Wall made up of '#', '-', and '|' characters.
    """
    # Basic usage
    result = []
    for _ in range(height):
        result.append(['#' if _ < height - 1 else '|'] + ['-' if _ < height - 1 else '|'] * width)
    return '\n'.join([''.join(row) for row in result])

    # Edge case
    result = []
    for _ in range(height):
        result.append(['#' if _ < height - 1 else '|'] + ['-' if _ < height - 1 else '|'] * width)
    return '\n'.join([''.join(row) for row in result])

    # Advanced scenario
    result = []
    for _ in range(height):
        result.append(['#' if _ < height - 1 else '|'] + ['-' if _ < height - 1 else '|'] * width)
    return '\n'.join([''.join(row) for row in result])

    # Test cases
    # Basic usage
    height, width = 3, 3
    expected_output = """
###
#-|
###
"""
    actual_output = build_walls(height, width)
    assert actual_output == expected_output, "Basic usage failed"
    print("Basic usage passed")

    # Edge case
    height, width = 1, 1
    expected_output = """#
|
"""
    actual_output = build_walls(height, width)
    assert actual_output == expected_output, "Edge case failed"
    print("Edge case passed")

    # Advanced scenario
    height, width = 5, 5
    expected_output = """
###########
#-#######-|
#-#######-|
###########
###########
"""
    actual_output = build_walls(height, width)
    assert actual_output == expected_output, "Advanced scenario failed"
    print("Advanced scenario passed")

    # Test runner
    test_cases
    Docstring

    """For example:

    >>> build_walls()

    Build the walls for the graph and return the walls created.
    ```
    ```python
    def build_walls():
    """Build the walls for the graph and return the walls created.

    >>> build_walls()
    """
    walls = []
    visited = set()
    queue = []
    current_positions = set(visited)
    queue.extend(current_positions)
    visited.update(current_positions)
    while len(queue) > 0:
        node = queue.pop()
        if node not in visited:
            visited.update(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.update(neighbor)
                walls.append(Wall(node, neighbor))
    return walls
    ```

    For example:

    >>> build_walls()
    """Build the walls for the graph and return the walls created.

    >>> build_walls()
    """
    walls = []
    visited = set()
    queue = []
    current_positions = set(visited)
    queue.extend(current_positions)
    visited.update(current_positions)
    while len(queue) > 0:
        node"""
    ```