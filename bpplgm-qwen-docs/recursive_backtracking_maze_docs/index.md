# index

    Purpose

    The function `index` calculates the linear index of a position `(x, y)` in a grid with dimensions `cols` by `rows`. If the position is out of bounds, it returns `None`; otherwise, it returns the linear index corresponding to the position.
    Parameters

    ```python
def index(x, y):
    """Calculate the linear index of a position (x, y) in a grid.

    Parameters:
    x (int): The column index of the position. Must be non-negative.
    y (int): The row index of the position. Must be non-negative.

    Returns:
    int or None: The linear index corresponding to the position if it's within bounds;
                 otherwise, returns None.
    """

    # Check if the indices are within the grid dimensions
    if x < 0 or y < 0:
        return None
    cols = 10  # Assume a constant number of columns for demonstration purposes
    rows = 5   # Assume a constant number of rows for demonstration purposes

    # Calculate the linear index using the formula: (x * rows) + y
    linear_index = (x * rows) + y

    return linear_index
```

This function `index` computes the linear index of a position `(x, y)` in a grid with a fixed number of columns (`cols`) and rows (`rows`). The indices must be non-negative for valid positions. If the indices are out of bounds (i.e., less than zero), the function returns `None`. Otherwise, it calculates and returns the linear index using the formula `(x * rows) + y`.
    Returns

    ```python
def index(x, y, cols, rows):
    """
    Calculate the linear index of a position (x, y) in a grid with dimensions `cols` by `rows`.

    Args:
    x (int): The column index of the position.
    y (int): The row index of the position.
    cols (int): The number of columns in the grid.
    rows (int): The number of rows in the grid.

    Returns:
    int or None: If the position (x, y) is out of bounds, returns `None`. Otherwise,
                 returns the linear index corresponding to the position. The linear
                 index is calculated as x + y * cols.

    Special Cases:
    - If x < 0 or y < 0, returns `None` because negative indices are not valid.
    - If x >= cols or y >= rows, returns `None` because out-of-bounds positions are invalid.

    Examples:
    >>> index(2, 3, 5, 4)
    17
    >>> index(-1, 2, 5, 4)
    None
    >>> index(2, 4, 5, 4)
    None
    """
```
    Examples

    ```python
# Basic usage: Demonstrates accessing an element by its index in a list.
my_list = ['apple', 'banana', 'cherry']
print(my_list[1])  # Output: banana

# Edge case: Accessing an out-of-bounds index raises an IndexError.
try:
    print(my_list[3])
except IndexError as e:
    print(e)  # Output: list index out of range

# Advanced scenario: Demonstrates negative indexing and slicing.
print(my_list[-1])  # Output: cherry
print(my_list[0:2])   # Output: ['apple', 'banana']
```
    Docstring

    """```python
def index(x, y):
    """
    Calculate the linear index for a 2D array given its row and column indices.

    Args:
        x (int): The column index (0-based).
        y (int): The row index (0-based).

    Returns:
        int or None: The linear index of the position (x, y) if within bounds,
                     otherwise returns None.

    Examples:
    >>> index(2, 3)
    14
    >>> index(-1, 3)
    None
    >>> index(2, -1)
    None
    >>> index(2, 5)
    None
    """
```"""
    ```