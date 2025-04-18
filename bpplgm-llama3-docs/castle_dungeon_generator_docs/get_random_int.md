# get_random_int

    Purpose

    The function `get_random_int` generates a random integer within the specified range `low` to `high (exclusive)`. It uses the built-in `randint` function from the `random` module to perform this calculation. 

```python
import random

def get_random_int(low, high):
    return random.randint(low, high - 1)
```

This code snippet is designed to generate a random integer between two specified integers.
    Parameters

    ```python
def get_random_int(low: int, high: int) -> int:
    """
    Generates a random integer within the specified range low to high (exclusive).

    Parameters:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (exclusive).

    Returns:
        int: A random integer between low and high.

    Usage constraints:
        This function can be used in applications where a random integer needs to be generated within a specific range.
    """
    return random.randint(low, high - 1)
```
    Returns

    ### get_random_int Function

#### Return Type

The return value of the `get_random_int` function is an integer.

#### Description

The `get_random_int` function generates a random integer within the specified range `low` to `high (exclusive)` using the built-in `randint` function from the `random` module.

#### Special Cases

There are no special cases defined for this function.
    Examples

    ```python
def get_random_int(min_value=0, max_value=100):
    """
    Returns a random integer within the specified range.

    Args:
        min_value (int, optional): The minimum value in the range. Defaults to 0.
        max_value (int, optional): The maximum value in the range. Defaults to 100.

    Returns:
        int: A random integer between min_value and max_value (inclusive).

    Examples:
        >>> get_random_int()
        50
        >>> get_random_int(10)
        46
    """
    return random.randint(min_value, max_value)

# Explanation
import random

# Basic usage
print(get_random_int())  # Output: A random integer between 0 and 100 (inclusive).

# Edge case
print(get_random_int(-1))  # Output: A random integer between -1 and 0 (inclusive).

# Advanced scenario (if applicable)
def get_max_natural_numbers(n):
    """
    Returns a list of n natural numbers.

    Args:
        n (int): The number of natural numbers to generate.

    Returns:
        list: A list of n natural numbers.
    """
    return random.sample(range(1, 100), n)

print(get_max_natural_numbers(10))
```
    Docstring

    """```python
def get_random_int(low: int, high: int) -> int:
    """
    Returns a random integer between low (inclusive) and high - 1 (exclusive).

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (exclusive).

    Returns:
        int: A random integer within the specified range.

    Examples:
        >>> get_random_int(1, 10)
        random.randint(1, 9)  # low is inclusive
        >>> get_random_int(10, 20)
        random.randint(10, 19)  # high - 1 is exclusive
```"""
    ```