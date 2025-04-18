# get_random_int

    Purpose

    The function `get_random_int` returns a random integer between two given values, inclusive of the lower bound and exclusive of the upper bound.
    Parameters

    ```python
def get_random_int(low: int, high: int) -> int:
    """
    Returns a random integer between two given values, inclusive of the lower bound and exclusive of the upper bound.

    Parameters:
    low (int): The lower bound of the range (inclusive).
    high (int): The upper bound of the range (exclusive).

    Usage Constraints:
    - `low` should be less than or equal to `high`.
    """
```
    Returns

    ### Function: `get_random_int`

#### Purpose
The function `get_random_int` returns a random integer between two given values, inclusive of the lower bound and exclusive of the upper bound.

#### Return Type
- **Type**: `int`

#### Description
- The function generates a random integer within the specified range. It uses Python's built-in `randint` function from the `random` module to achieve this.
- If the `low` value is greater than or equal to the `high` value, the function will return `None`, indicating that an invalid range was provided.

#### Examples

1. **Basic Usage**
    ```python
    import random
    
    result = get_random_int(1, 5)
    print(result)  # Output could be any integer from 1 to 4, inclusive.
    ```

2. **Handling Invalid Range**
    ```python
    import random
    
    result = get_random_int(5, 3)
    print(result)  # Output: None
    ```
    
    In this example, the range is invalid (low >= high), so `get_random_int` returns `None`.
    Examples

    ```python
# Basic usage: Generate a random integer between 0 (inclusive) and 10 (exclusive).
random_int = get_random_int(0, 10)
print(random_int)

# Edge case: Generate a random integer between -5 and 5. Since the range is inclusive of negative numbers,
# this will include -5, 0, and 4.
random_int = get_random_int(-5, 5)
print(random_int)

# Advanced scenario: Generate a random integer within a large range (e.g., from 1 to 10^9) using the mod operator
# to ensure performance in case of large numbers.
large_range_random_int = get_random_int(1, 10**9)
print(large_range_random_int)
```
    Docstring

    """```python
def get_random_int(low, high):
    """
    Generates a random integer within the inclusive range [low, high-1].

    Args:
        low (int): The lower bound of the range. Inclusive.
        high (int): The upper bound of the range. Exclusive.

    Returns:
        int: A randomly generated integer between low and high-1, inclusive.

    Examples:
        >>> get_random_int(0, 5)
        2
        >>> get_random_int(-3, 4)
        -1
    """
```"""
    ```