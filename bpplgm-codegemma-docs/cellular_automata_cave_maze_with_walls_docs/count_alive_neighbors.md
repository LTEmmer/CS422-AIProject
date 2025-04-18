# count_alive_neighbors

    Purpose

    ```python
    def count_alive_neighbors(live_map, x, y):
        count = 0
        i = -1
        while i < 2:
            j = -1
            while j < 2:
                neighbor_x = x + i
                neighbor_y = y + j
                if i == 0 and j == 0:  # If we're looking at the middle point
                    pass  # Do nothing, we don't want to add ourselves in!
                elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                    count += 1
                elif live_map[neighbor_x][neighbor_y] is True:
                    count += 1
                j += 1
            i += 1
        return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x
    Parameters

    
    Returns

    """
    Examples

    Please refer to [example_usage_1.py](https://github.com/khalil-mohamed/python-code-examples/blob/main/Generate%202-3%20usage%20examples%20for%20%27count_alive_neighbors%27/example_usage_1.py)
    and [example_usage_2.py](https://github.com/khalil-mohamed/python-code-examples/blob/main/Generate%202-3%20usage%20examples%20for%20%27count_alive_neighbors%27/example_usage_2.py)
    for each example.
    """

import typing as tp

import numpy as np


def count_alive_neighbors(board: np.ndarray) -> tp.Dict[int, int]:
    """
    Calculates the count of alive neighbors for each cell in the given board.

    Parameters:
        board (np.ndarray): A 2D numpy array representing the game board.

    Returns:
        tp.Dict[int, int]: A dictionary where keys are cell indices (0-indexed)
        and values are the count of alive neighbors for each cell.
    """
    # Check if the input board is valid (not empty).
    if not board.any():
        raise ValueError("Input board is empty.")

    # Extract the dimensions of the board.
    rows, cols = board.shape

    # Initialize an empty dictionary to store the count of alive neighbors for each cell.
    alive_neighbors = {}

    # Iterate over each cell in the board.
    for i in range(rows):
        for j in range(cols):
            # Compute the indices of the neighboring cells (including diagonals).
            neighbors = [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),  # Upper row
                (i, j - 1), (i, j + 1),  # Left and right columns
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)  # Lower row
            ]

            # Initialize the count of alive neighbors for the current cell to 0.
            alive_neighbor_count = 0

            # Iterate over the neighboring cells and count the alive neighbors.
            for neighbor in neighbors:
                # Check if the neighbor is within the bounds of the board.
                if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                    # If the neighbor is alive, increment the count.
                    if board[neighbor[0], neighbor[1]]:
                        alive_neighbor_count += 1

            # Store the count of alive neighbors for the current cell in the dictionary.
            alive_neighbors[(i, j)] = alive_neighbor_count

    return alive_neighbors


# Basic usage
board = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 0]])
result = count_alive_neighbors(board)
print(result)

# Edge case
board = np.array([])
try:
    result = count_alive_neighbors(board)
except ValueError as e:
    print(e)

# Advanced scenario (if applicable)
board = np.zeros((100, 100), dtype=np.uint8)
result = count_alive_neighbors(board)
print(re
    Docstring

    """"""
    ```
    ```python
    def count_alive_neighbors(live_map, x, y):
    """Return the number of living neighbors in a given cell.

    Args:
        live_map: The map of cells, where True is live and False is dead.
        x: The x-coord of the cell.
        y: The y-coord of the cell.

    Returns:
        The number of alive neighbors of the cell at (x, y).

    Examples:
        >>> count_alive_neighbors([[True, True, True], [True, False, True], [True, True, True]], 1, 1)
        4
    """
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:  # If we're looking at the middle point
                pass  # Do nothing, we don't want to add ourselves in!
            # In case the index we're looking at it off the edge of the live_map
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # Otherwise, a normal check of the neighbour
            elif li"""
    ```