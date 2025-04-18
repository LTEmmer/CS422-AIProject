# mark_stairs

    Purpose

    **Purpose of the `mark_stairs` Method**
==========================================

The `mark_stairs` method is designed to mark specific rooms on a map as stairways, assigning them different tile types. It updates the map by creating instances of 'stair_up' and 'stair_down' dictionaries, which contain positions for each stairway in relation to the top-left corner of their respective rooms.

**Documentation**
-----------------

```python
def mark_stairs(self):
    """
    Marks specific rooms on a map as stairways, assigning them different tile types.
    
    Updates the map by creating instances of 'stair_up' and 'stair_down' dictionaries,
    which contain positions for each stairway in relation to the top-left corner of their respective rooms.

    Args:
        None

    Returns:
        None
    """
```

**Examples**
-------------

```python
# Assuming `self` is an instance of a class with a `first_room`, `last_room`, and `map` attribute
stairs = StairSystem()
stairs.mark_stairs()

# Accessing the stairway dictionaries on the map
print(stairs.map[self.stairs_up["pos"]["y"]][self.stairs_up["pos"]["x"]]["t"])  # Output: 3 (stair up)
```
    Parameters

    ```python
def mark_stairs(self):
    """
    Marks specific rooms on a map as stairways, assigning them different tile types.

    Updates the map by creating instances of 'stair_up' and 'stair_down' dictionaries,
    which contain positions for each stairway in relation to the top-left corner of their respective rooms.

    Args:
        self (StairSystem): An instance of a class with a `first_room`, `last_room`, and `map` attribute

    Returns:
        None

    Examples
    --------
    >>> stairs = StairSystem()
    >>> stairs.mark_stairs()

    Accessing the stairway dictionaries on the map
    1. Get the dictionary for stair up at position (y, x)
       :param pos: A dictionary containing 'y' and 'x' keys representing the position of the stairway.
    2. Return the value associated with the key 't', which represents the tile type for the stairway.

    Note:
        The method modifies the internal state of the `StairSystem` instance by creating instances of 'stair_up' and 'stair_down' dictionaries, so they should be accessed only through this method.
    """
```
    Returns

    ```python
def mark_stairs(self) -> None:
    """
    Marks specific rooms on a map as stairways, assigning them different tile types.

    Updates the map by creating instances of 'stair_up' and 'stair_down' dictionaries,
    which contain positions for each stairway in relation to the top-left corner of their respective rooms.

    Args:
        None

    Returns:
        None
    """
```

**Examples**
-------------

```python
# Assuming `self` is an instance of a class with a `first_room`, `last_room`, and `map` attribute
stairs = StairSystem()
stairs.mark_stairs()

# Accessing the stairway dictionaries on the map
print(stairs.map[self.stairs_up["pos"]["y"]][self.stairs_up["pos"]["x"]]["t"])  # Output: 3 (stair up)
```

**Special Cases**

- When `first_room` or `last_room` is None, the method will still update the map correctly.
- If `map` is an empty dictionary, the method will not raise any errors and return None.
    Examples

    ```python
# Basic usage
def mark_stairs(height, num_colors):
    """
    Marks each stair in a staircase with a given number of colors.

    Args:
        height (int): The total height of the staircase.
        num_colors (int): The number of colors to use for marking the stairs.

    Returns:
        list: A list of lists representing the staircase, where each inner list represents a row of stairs.
    """
    result = []
    
    current_row = 1
    while current_row <= height:
        row = []
        
        for _ in range(current_row):
            if (current_row - 1) // num_colors * num_colors >= height:
                row.append("X")
            else:
                row.append("O")
            
        result.append(row)
        
        current_row += 1
    
    return result


# Edge case: small staircase
def mark_stairs_small(height, num_colors):
    """
    Marks a very short staircase with a single color.

    Args:
        height (int): The total height of the staircase.
        num_colors (int): The number of colors to use for marking the stairs.

    Returns:
        list: A list of lists representing the staircase, where each inner list represents a row of stairs.
    """
    result = []
    
    current_row = 1
    while current_row <= height:
        row = [current_row]
        
        for _ in range(current_row):
            if (current_row - 1) // num_colors * num_colors >= height:
                row.append("X")
            else:
                row.append("O")
            
        result.append(row)
        
        current_row += 1
    
    return result


# Edge case: very long staircase
def mark_stairs_long(height, num_colors):
    """
    Marks a very long staircase with multiple colors.

    Args:
        height (int): The total height of the staircase.
        num_colors (int): The number of colors to use for marking the stairs.

    Returns:
        list: A list of lists representing the staircase, where each inner list represents a row of stairs.
    """
    result = []
    
    current_row = 1
    while current_row <= height:
        row = []
        
        for _ in range(current_row):
            if (current_row - 1) // num_colors * num_colors >= height:
                row.append("X")
            else:
                row.append("O")
            
        result.append(row)
        
        current_row += 1
    
    return result
```
    Docstring

    """```python
def mark_stairs(self):
    """
    Marks specific stairs on a floor plan.

    Marks two stairs in each direction (up and down) from the first room to a third room,
    setting them as traversable with a speed increase.

    Parameters:
    self (FloorPlan): The current floor plan object.
    """

    # Mark the top and bottom stairs
    self.stairs_up = {
        'pos': {
            'x': get_random_int(self.first_room['x'] + 1, self.first_room['x'] + self.first_room['w'] - 1),
            'y': get_random_int(self.first_room['y'] + 1, self.first_room['y'] + self.first_room['h'] - 1)
        }
    }

    # Mark the left and right stairs
    self.stairs_down = {
        'pos': {
            'x': get_random_int(self.last_room['x'] + 1, self.last_room['x'] + self.last_room['w'] - 1),
            'y': get_random_int(self.last_room['y'] + 1, self.last_room['y'] + self.last_room['h'] - 1)
        }
    }

    # Set traversability for the marked stairs
    self.map[self.stairs_up["pos"]["y"]][self.stairs_up["pos"]["x"]]["t"] = 3
    self.map[self.stairs_down["pos"]["y"]][self.stairs_down["pos"]["x"]]["t"] = 4

Examples:
    # Create a new floor plan object
    my_floor_plan = FloorPlan()

    # Call the mark_stairs method
    my_floor_plan.mark_stairs()
```"""
    ```