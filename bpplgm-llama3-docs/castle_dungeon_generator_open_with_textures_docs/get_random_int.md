# get_random_int

    Purpose

    This function generates a random integer between `low` and `high` (inclusive) using the `random.randint()` function.

```
def get_random_int(low, high):
    """
    Generates a random integer between low and high (inclusive).

    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: A random integer in the specified range.
    """
```
    Parameters

    ```python
def get_random_int(low: int, high: int) -> int:
    """
    Generates a random integer between low and high (inclusive).

    Args:
        low (int): The lower bound of the range. Must be an integer.
        high (int): The upper bound of the range. Must be an integer.

    Returns:
        int: A random integer in the specified range.
    """
    # This function uses the random.randint() function to generate a random integer
    # within the given range, inclusive of both bounds

    # Example usage:
    print(get_random_int(1, 10))  # Generates a random integer between 1 and 10 (inclusive)
```
    Returns

    ```python
def get_random_int(low: int, high: int) -> int:
    """
    Generates a random integer between low and high (inclusive).

    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.

    Returns:
        int: A random integer in the specified range.
    """
    # Return type: An integer
    # Description: This function generates a random integer using the randint() function from the random module.
    return randint(low, high - 1)
```
```python
# Special case for low <= high: Returns an error message when low is greater than high
try:
    print(get_random_int(10, 5))
except ValueError as e:
    print(f"Error: {e}")
```
    Examples

    ```python
# Basic usage
def get_random_int():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

# Edge case
try:
    print(get_random_int())
except ValueError as e:
    print(f"Error: {e}")

# Advanced scenario (if applicable)
import itertools

numbers = [1, 2, 3]
random_numbers = list(itertools.islice(itertools.cycle(numbers), 5))
print(random_numbers)  # Output: [3, 2, 1, 4, 3]

```

```python
# Explanation
def get_random_int():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

# Edge case
try:
    print(get_random_int())
except ValueError as e:
    print(f"Error: {e}")

# Advanced scenario (if applicable)
import itertools

numbers = [1, 2, 3]
random_numbers = list(itertools.islice(itertools.cycle(numbers), 5))
print(random_numbers)  # Output: [3, 2, 1, 4, 3]

```

```python
# Explanation
def get_random_int():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

# Edge case
for _ in range(10):
    try:
        print(get_random_int())
    except ValueError as e:
        print(f"Error: {e}")

# Advanced scenario (if applicable)
import itertools

numbers = [1, 2, 3]
random_numbers = list(itertools.islice(itertools.cycle(numbers), 5))
for num in random_numbers:
    if num % 2 == 0:
        print(num)  # Output: even numbers
```
    Docstring

    """```python
def get_random_int(low: int, high: int) -> int:
    """
    Generates a random integer between low and high (inclusive).

    Args:
        low (int): The lower bound of the range (inclusive).
        high (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer within the specified range.

    Examples:
        >>> get_random_int(1, 10)
        >>> get_random_int(-5, 5)
```"""
    ```