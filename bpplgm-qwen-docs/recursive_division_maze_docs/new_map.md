# new_map

    Purpose

    The `new_map` function generates a square matrix of specified size filled with a given value. Each element in the matrix is initialized to the specified value. The function returns this matrix as a 2D list.
    Parameters

    ```python
def new_map(size: int, value: int) -> List[List[int]]:
    """
    Generates a square matrix of specified size filled with a given value.

    Parameters:
    - size (int): The size of the square matrix to be generated.
      This should be a positive integer indicating the number of rows and columns in the matrix.

    - value (int): The value to fill each element of the matrix. The default is 0, but any integer can be used.

    Returns:
    - List[List[int]]: A 2D list representing the generated square matrix.
      Each element in the matrix is initialized to the specified value.

    Usage Constraints:
    - The size parameter should be a positive integer (size > 0).
    - The value can be any integer, including negative numbers or zero.
    """
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
    
    return [[value] * size for _ in range(size)]

# Example usage
try:
    matrix = new_map(3, 5)
    print(matrix)  # Output: [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
except ValueError as e:
    print(e)
```
    Returns

    ### `new_map` Function Documentation

The `new_map` function is designed to generate a square matrix of specified size filled with a given value. Each element in the matrix is initialized to this specific value.

#### Purpose:
- The function takes two parameters: `size`, which determines the dimensions of the resulting square matrix, and `value`, which specifies the value that each element in the matrix will be set to.
- It returns a 2D list (list of lists) representing the generated matrix.

#### Return Type:
- **Return Value**: A 2D list (list of lists), where each inner list represents a row of the matrix and contains `size` elements, all initialized to the specified `value`.

#### Description:
- The function uses nested list comprehensions to create the matrix. It first iterates over a range of numbers from 0 to `size - 1` (inclusive) for the outer loop, which corresponds to each row in the matrix.
- For each iteration of the outer loop, it initializes an inner list with `value` repeated `size` times. This inner list represents one row of the matrix.
- The outer list comprehension then collects all these inner lists into a single 2D list, which is returned as the result.

#### Special Cases:
- If `size` is less than or equal to zero, the function will return an empty list since it is not possible to generate a matrix with non-positive dimensions.
- The value of `value` can be any data type that supports the multiplication operator (`*`) and comparison operators. This includes integers, floats, and other numeric types, as well as strings, lists, and other iterable objects.

#### Examples:
```python
# Example 1: Creating a 3x3 matrix with all elements initialized to 0
matrix = new_map(3, 0)
print(matrix)
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Example 2: Creating a 4x4 matrix with all elements initialized to 'X'
matrix = new_map(4, 'X')
print(matrix)
# Output: [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']]

# Example 3: Creating a 2x2 matrix with all elements initialized to [1, 2]
matrix = new_map(2, [1, 2])
print(matrix)
# Output: [[1, 2], [1, 2]]
```

This detailed documentation provides a clear understanding of the function's behavior and usage based on the code provided.
    Examples

    ```python
# Basic usage: Applying a new function to elements in a list
def new_map(func, iterable):
    """
    Applies a given function `func` to each element in an iterable and returns a new list with the results.

    Parameters:
    func (function): The function to apply.
    iterable (iterable): An iterable object (e.g., list, tuple).

    Returns:
    list: A new list containing the results of applying `func` to each element in `iterable`.
    """
    return [func(x) for x in iterable]

# Example 1: Basic usage
numbers = [1, 2, 3]
squared_numbers = new_map(lambda x: x**2, numbers)
print(squared_numbers)  # Output: [1, 4, 9]

# Edge case: Applying a function to an empty list
empty_list = []
empty_squared = new_map(lambda x: x**2, empty_list)
print(empty_squared)  # Output: []

# Advanced scenario: Using map with multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
details = list(map(lambda name, age: f"{name} is {age} years old", names, ages))
print(details)  # Output: ['Alice is 30 years old', 'Bob is 25 years old', 'Charlie is 35 years old']
```
    Docstring

    """```python
def new_map(size, value):
    """
    Generates a square matrix (grid) of specified size filled with a given value.

    Args:
        size (int): The dimensions of the grid to create. Must be non-negative.
        value: The value to fill each cell of the grid with.

    Returns:
        list of lists: A square matrix where each element is equal to `value`.

    Examples:
        >>> new_map(3, 0)
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

        >>> new_map(2, 'x')
        [['x', 'x'],
         ['x', 'x']]
    """
```"""
    ```