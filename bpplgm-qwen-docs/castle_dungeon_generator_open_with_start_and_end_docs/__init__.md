# __init__

    Purpose

    This function initializes a maze generation class with various parameters for room size, number of rooms, and other attributes related to the generation process. It sets up variables that will be used to create and manage a maze's map, rooms, start and end points, connectivity, and light level. The purpose is to prepare an environment for generating a maze using these settings.
    Parameters

    ```python
class MazeGenerator:
    def __init__(self):
        """
        Initializes a maze generation class.

        Parameters:
            self (MazeGenerator): The instance of the class being initialized.

        Purpose: This function initializes a maze generation class with various parameters for room size, number of rooms, and other attributes related to the generation process. It sets up variables that will be used to create and manage a maze's map, rooms, start and end points, connectivity, and light level. The purpose is to prepare an environment for generating a maze using these settings.
        """
```
    Returns

    This function initializes a maze generation class with various parameters for room size, number of rooms, and other attributes related to the generation process. It sets up variables that will be used to create and manage a maze's map, rooms, start and end points, connectivity, and light level. The purpose is to prepare an environment for generating a maze using these settings.

The return type of this function is `None`. The function does not return any value; it simply initializes the class attributes with default or provided values, preparing it to generate a maze based on the specified parameters.

Special cases:

- If no parameters are provided, the function defaults to setting reasonable values for all attributes.
- The function initializes an empty map and list of rooms, as well as sets start and end points to `None` initially. These will be filled in during the maze generation process.
- The connectivity matrix is initialized with zeros, which will be used to represent the adjacency relationships between rooms.
- The light level attribute is set to zero, representing no initial light in the maze. This may change during the maze generation process as rooms are connected and lit up.

This initialization sets up a basic framework for generating a maze using the specified parameters, preparing all necessary data structures and variables for further processing and generation steps.
    Examples

    ```python
# Basic usage: Creating an instance of a class with default parameters
class MyClass:
    def __init__(self):
        self.value = 0

my_instance = MyClass()
print(my_instance.value)  # Output: 0
```

```python
# Edge case: Initializing an instance with custom parameters
class Calculator:
    def __init__(self, mode='add'):
        self.mode = mode

calc_add = Calculator(mode='add')
calc_subtract = Calculator(mode='subtract')

print(calc_add.mode)  # Output: add
print(calc_subtract.mode)  # Output: subtract
```

```python
# Advanced scenario: Using '__init__' for multiple attributes and default values
class Person:
    def __init__(self, name, age=30):
        self.name = name
        self.age = age

person1 = Person('Alice')
person2 = Person('Bob', 25)

print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person2.name)  # Output: Bob
print(person2.age)   # Output: 25
```
    Docstring

    """```python
class MapGenerator:
    """
    Initializes a map generator object with various parameters to control room size and number generation.
    
    Args:
        x_size (int): The width of the generated map.
        y_size (int): The height of the generated map.
        min_room_size (int): The minimum allowable size for rooms in cells.
        max_room_size (int): The maximum allowable size for rooms in cells.
        num_rooms (Optional[int]): The number of rooms to generate. If None, it will be randomly selected between min_rooms and max_rooms.
        min_rooms (int): The minimum number of rooms to generate if num_rooms is not specified.
        max_rooms (int): The maximum number of rooms to generate if num_rooms is not specified.

    Returns:
        None
    """

    def __init__(self):
        """
        Initializes the map generator with default settings for room size and number generation.
        """
        self.x_size = 60
        self.y_size = 40
        self.min_room_size = 5
        self.max_room_size = 15
        self.num_rooms = None
        self.min_rooms = 10
        self.max_rooms = 15
        self.map = None
        self.rooms = None
        self.first_room = None
        self.last_room = None
        self.end = None
        self.start = None
        self.connected = None
        self.light = 0

# Example usage:
# generator = MapGenerator()
```"""
    ```