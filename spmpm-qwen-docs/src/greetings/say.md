# say

    Purpose

    The function `say` takes a single argument `name` and returns a string that combines 'Hello', the provided name, and an exclamation mark.
    Parameters

    ```python
def say(name: str) -> str:
    """
    Return a greeting string combining 'Hello', the provided name, and an exclamation mark.

    Parameters:
        - name (str): The person's name to greet. This parameter is required and must be a non-empty string.

    Returns:
        str: A formatted string that says "Hello" followed by the provided name and an exclamation mark.
    """
    return f"Hello, {name}!"
```
    Returns

    ```python
def say(name):
    """Return a greeting message combining 'Hello', the provided name, and an exclamation mark.

    :param name: The name to be included in the greeting.
    :return: A string in the format 'Hello {name}!'.
    """
    return f'Hello {name}!'
```

**Special Cases**:
- If `name` is an empty string, the function will still return `'Hello!'`.
- If `name` contains only whitespace characters, it will also return `'Hello!'`.
    Examples

    ```python
# Basic usage: Say hello to a person's name.
def say(name):
    """Say hello to a given name."""
    return f"Hello, {name}!"

print(say("Alice"))  # Output: Hello, Alice!

# Edge case: Handle empty input gracefully.
def say_hello(name=""):
    """Say hello with an optional default value for the name."""
    if not name:
        return "Hello!"
    else:
        return f"Hello, {name}!"

print(say_hello())  # Output: Hello!
print(say_hello("Bob"))  # Output: Hello, Bob!

# Advanced scenario: Customize the greeting with punctuation.
def say_with_punctuation(name, punctuation="!"):
    """Say hello with a custom punctuation mark."""
    return f"Hello, {name}{punctuation}"

print(say_with_punctuation("Charlie", "."))  # Output: Hello, Charlie.
```
    Docstring

    """```python
def say(name):
    """
    Say a greeting to a given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting message in the form 'Hello {name}!'.

    Examples:
        >>> say('Alice')
        'Hello Alice!'
        >>> say('Bob')
        'Hello Bob!'
    """
```"""
    ```