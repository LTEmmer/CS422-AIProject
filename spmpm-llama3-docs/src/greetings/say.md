# say

    Purpose

    This function defines a simple method `say` that takes a string argument `name` and returns a greeting message in the form 'Hello <name>!'.

```python
def say(name):
    return f'Hello {name}!'
```

Examples:

```python
print(say('John'))  # Output: Hello John!
print(say('Alice'))  # Output: Hello Alice!
```
    Parameters

    ```python
def say(name: str) -> str:
    """
    This function defines a simple method `say` that takes a string argument `name` and returns a greeting message in the form 'Hello <name>!'.

    Parameters
    ----------
    name : str
        The name to be used in the greeting message.

    Returns
    -------
    str
        A greeting message with the specified name.

    Examples
    --------
    >>> print(say('John'))  # Output: Hello John!
    >>> print(say('Alice'))  # Output: Hello Alice!

    Constraints
            None
    """
```
    Returns

    ```python
def say(name: str) -> str:
    """
    Returns a greeting message in the form 'Hello <name>!'.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting message.

    Examples:
        >>> print(say('John'))
        'Hello John!'
        >>> print(say('Alice'))
        'Hello Alice!'
    """
    return f'Hello {name}!'
```
    Examples

    ```python
def say(text):
    """
    Prints the given text.

    Args:
        text (str): The text to be printed.
    """
    print(" saying " + text)

def say_hello(name):
    """
    Prints a personalized greeting.

    Args:
        name (str): The person's name.
    """
    say("Hello, " + name + "!")

# Basic usage
say_hello("World")  # Output: Hello, World!

# Edge case
try:
    say("1234567890")  # This will raise ValueError as it contains a non-ASCII character
except ValueError as e:
    print(e)

# Advanced scenario (if applicable)
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the input numbers.
    """
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Average:", average)  # Output: Average: 3.0
```
    Docstring

    """```python
def say(name: str) -> str:
    """
    Returns a personalized greeting.

    A one-line description:
        Generates a friendly hello message with the specified name.

    Args section:
        - **name**: The person to be greeted (string)

    Returns section:
        - **str**: The greeting message

    Examples section:
        >>> say('John')
        'Hello John!'
```"""
    ```