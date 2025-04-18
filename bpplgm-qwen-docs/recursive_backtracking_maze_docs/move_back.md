# move_back

    Purpose

    The `move_back` function updates the position of an entity by removing the last direction from a stack and moving it in the opposite direction twice, effectively backing up to the previous position. It uses global variables for the current coordinates (`x_pos` and `y_pos`) and a stack to keep track of movement directions.
    Parameters

    ```python
def move_back():
    """
    The `move_back` function updates the position of an entity by removing the last direction from a stack and moving it in the opposite direction twice, effectively backing up to the previous position.

    Args:
        None

    Returns:
        None

    Usage Constraints:
        - Requires global variables `x_pos` and `y_pos` to be initialized before calling this function.
        - The stack should be populated with movement directions (e.g., 'up', 'down', 'left', 'right') in the order of execution.

    Example:
        # Initialize global variables
        x_pos = 0
        y_pos = 0

        # Push movement directions onto the stack
        stack = ['down', 'left']

        # Move back
        move_back()

        # Check new position (should be back to original position)
        assert x_pos == 0 and y_pos == 0, "Entity should be at the original position"
    """
```
    Returns

    ```python
def move_back():
    """
    This function updates the position of an entity by removing the last direction from a stack and moving it in the opposite direction twice, effectively backing up to the previous position. It uses global variables for the current coordinates (`x_pos` and `y_pos`) and a stack to keep track of movement directions.

    Parameters:
    None

    Returns:
    - None

    Special Cases:
    - If the stack is empty (meaning there are no recorded moves), the function will not change the position and will return without any action.
    """
```
    Examples

    ```python
# Basic usage: Move back to the previous directory without confirmation
move_back()
```

```python
# Edge case: Attempt to move back when already at the root directory (no effect)
move_back()
```

```python
# Advanced scenario: Recursively move back through multiple directories and confirm each step
def recursive_move_back(num_steps):
    for _ in range(num_steps):
        print(f"Current directory: {os.getcwd()}")
        input("Press Enter to continue moving back...")
        move_back()

recursive_move_back(3)
```
    Docstring

    """```python
def move_back():
    """
    Moves the position back by twice the movement distance in the direction specified by the top element of the direction stack.

    Args:
        None

    Returns:
        None

    Examples:
        >>> y_pos = 10
        >>> x_pos = 20
        >>> direction_stack = ['up']
        >>> move_back()
        >>> print(y_pos, x_pos)  # Output: -8 20

        >>> y_pos = 30
        >>> x_pos = 40
        >>> direction_stack = ['right']
        >>> move_back()
        >>> print(y_pos, x_pos)  # Output: 30 -16

        >>> y_pos = 50
        >>> x_pos = 60
        >>> direction_stack = ['down']
        >>> move_back()
        >>> print(y_pos, x_pos)  # Output: 70 60

        >>> y_pos = 80
        >>> x_pos = 90
        >>> direction_stack = ['left']
        >>> move_back()
        >>> print(y_pos, x_pos)  # Output: 80 110
    """
```"""
    ```