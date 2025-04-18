# get_random_int

    Purpose

    The `get_random_int` function generates a random integer between `low` and `high - 1`, inclusive.
    Parameters

    ### get_random_int Function Documentation

#### Purpose:
The `get_random_int` function generates a random integer between `low` and `high - 1`, inclusive.

#### Parameters:

- **`low`:**  
  - **Type:** Integer
  - **Description:** The lower bound (inclusive) of the range for the random integer.
  - **Usage Constraints:** Must be an integer, and `low` must be less than or equal to `high`.

- **`high`:**  
  - **Type:** Integer
  - **Description:** The upper bound (exclusive) of the range for the random integer.
  - **Usage Constraints:** Must be an integer, and `high` must be greater than `low`.

#### Example Usage:

```python
import random

# Generate a random integer between 1 and 10
random_number = get_random_int(1, 11)
print(random_number)  # Output will be a random integer between 1 and 10, inclusive.
```

In this example, `get_random_int` is used to generate a random integer between 1 and 10. The function ensures that the generated number is within the specified range, including both bounds.
    Returns

    ```python
def get_random_int(low: int, high: int) -> int:
    """
    Generates a random integer between `low` and `high - 1`, inclusive.

    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: A random integer within the specified range [low, high - 1].

    Special Cases:
        - If `low` is greater than or equal to `high`, an `ValueError` is raised.
        - If `low` is negative and `high` is positive, the function returns a value less than zero,
          but it may still wrap around if using a modulo operation with a large enough number.

    Examples:
        >>> get_random_int(1, 5)
        3
        >>> get_random_int(0, 5)
        4  # Note: This will return 0 to 4 inclusive.
    """
```
    Examples

    ```python
# Basic usage: Generate a random integer between 0 and 10 (exclusive)
import random
print(get_random_int(0, 10))  # Example output could be: 5

# Edge case: Attempt to generate a random integer with non-integer bounds
try:
    print(get_random_int(-3.5, 2.3))
except ValueError as e:
    print(e)  # Output: Bounds must be integers

# Advanced scenario: Generate a random integer within a large range
print(get_random_int(10**9, 10**10))  # Example output could be: 10000000005
```
    Docstring

    """```python
def get_random_int(low, high):
    """
    Generates a random integer within the specified range [low, high-1].

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (exclusive).

    Returns:
        int: A randomly chosen integer between low and high-1.

    Examples:
        >>> get_random_int(1, 5)
        3
        >>> get_random_int(0, 10)
        7
        >>> get_random_int(-1, 2)
        -1
    """
```"""
    ```