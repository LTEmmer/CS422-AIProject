# add_tiles

    Purpose

    This function takes a `cell_map` as input and iterates over each cell in the map. For cells marked as `True`, it places a tile at the appropriate coordinates and adds those coordinates to a `visited` list. Each tile is placed at coordinates calculated from the current index in the map, doubling their values to account for the size of the tiles being placed (assuming they are 1x2 or 2x1 squares).
    Parameters

    ```python
def add_tiles(cell_map):
    """
    Iterates over each cell in the provided `cell_map` and places tiles at specific coordinates.

    Parameters:
        cell_map (list): A 2D list where each sublist represents a row in the map.
                         Each element of the sublists is expected to be a boolean value,
                         indicating whether a tile should be placed at that position.

    Returns:
        visited (list): A list containing tuples representing the coordinates of all
                       tiles placed, with the format (x, y).
    """
    visited = []  # List to store the coordinates of placed tiles

    for row_index, row in enumerate(cell_map):
        for col_index, cell in enumerate(row):
            if cell:  # Check if a tile should be placed at this cell
                # Calculate the tile's position by doubling its row and column indices
                x = col_index * 2
                y = row_index * 2
                visited.append((x, y))

    return visited

# Example usage:
cell_map = [
    [False, True, False],
    [True, True, False],
    [False, False, True]
]

visited_coordinates = add_tiles(cell_map)
print(visited_coordinates)  # Output: [(2, 0), (4, 1), (0, 4)]
```

This function `add_tiles` processes a 2D list `cell_map`, where each `True` value indicates that a tile should be placed at the corresponding position. The tiles are positioned by doubling their row and column indices to account for the size of the tiles being assumed to be 1x2 or 2x1 squares. The function returns a list of tuples, each representing the coordinates of the placed tiles.
    Returns

    ```python
def add_tiles(cell_map):
    """
    This function takes a `cell_map` as input and iterates over each cell in the map. For cells marked as `True`, it places a tile at the appropriate coordinates and adds those coordinates to a `visited` list. Each tile is placed at coordinates calculated from the current index in the map, doubling their values to account for the size of the tiles being placed (assuming they are 1x2 or 2x1 squares).

    Parameters:
    - cell_map: A 2D list representing the game grid where `True` indicates a tile should be placed.

    Returns:
    - visited: A list of coordinates where tiles have been placed. Each coordinate is a tuple (x, y), with values doubled to account for the size of the tiles.

    Examples:
    >>> add_tiles([[False], [True]])
    [(0, 1)]
    >>> add_tiles([[True, False], [False, True]])
    [(0, 0), (2, 1)]
    """
```
    Examples

    ```python
# Basic usage
# This demonstrates adding two tiles to a map with default parameters.
tile1 = Tile(position=(0, 0))
tile2 = Tile(position=(5, 5))

map.add_tiles([tile1, tile2])

# Edge case
# This shows how to handle the situation where a tile overlaps another, which is not allowed by default.
# Here, we attempt to add a new tile that would overlap an existing one at the same position.
try:
    map.add_tiles([Tile(position=(0, 0))])
except OverlappingTileException as e:
    print(e)

# Advanced scenario
# This example shows adding multiple tiles with custom properties and handling exceptions for each tile.
# We also demonstrate how to handle an exception if any of the tiles fail to add correctly.
tiles = [
    Tile(position=(10, 10), color='red'),
    Tile(position=(20, 20), size=5),
    Tile(position=(30, 30))
]

try:
    map.add_tiles(tiles)
except (InvalidTilePositionException, InvalidTileSizeException) as e:
    print(e)
```
    Docstring

    """```python
def add_tiles(cell_map):
    """
    This function iterates through a matrix represented by cell_map, placing cubes on tiles that are marked as False.

    Args:
        cell_map (list): A 2D list representing the game board. True indicates a tile where a cube should be placed, and False otherwise.

    Returns:
        None: The function modifies the game board in place and does not return any value.

    Examples:
        Given the following `cell_map`:
            [
                [False, True, False],
                [True, False, True],
                [False, True, False]
            ]

        This function will iterate through each tile in the matrix, placing a cube on tiles marked as True. The resulting board would look like this after execution:
            [
                ['cube', ' ', 'cube'],
                [' ', ' ', 'cube'],
                ['cube', ' ', 'cube']
            ]
    """
```"""
    ```