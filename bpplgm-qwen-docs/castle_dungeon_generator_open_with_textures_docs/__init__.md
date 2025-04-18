# __init__

    Purpose

    The provided code initializes various attributes for a map generator. It sets dimensions, size limits for rooms, room counts, and pointers to several elements necessary for generating a dungeon-like map using the Cellular Automaton algorithm. The `__init__` method is used to initialize these attributes with default values.
    Parameters

    ```python
class MapGenerator:
    def __init__(self):
        """
        Initialize a new map generator with default settings.

        Parameters:
            self: The instance of the class being initialized. It is used to access and modify instance variables within the class.
        """
        # Initialize dimensions of the map
        self.width = 100  # Type: int, Description: Width of the map grid in blocks.
        
        # Initialize size limits for rooms
        self.room_min_size = 5  # Type: int, Description: Minimum size a room can have in terms of width and height.
        self.room_max_size = 20  # Type: int, Description: Maximum size a room can have in terms of width and height.
        
        # Initialize the number of rooms to generate
        self.num_rooms = 15  # Type: int, Description: Total number of rooms to be generated on the map.

        # Pointers to various elements necessary for generating the dungeon-like map using Cellular Automaton algorithm
        self.rooms = []  # Type: list, Description: A list to store information about each room.
```

This documentation describes the purpose and functionality of the `__init__` method in the `MapGenerator` class. It includes parameter documentation with descriptions and types for the parameters used within the method.
    Returns

    ```python
def __init__(self):
    """Initialize the map generator with default attributes.

    This method sets up various parameters and pointers needed for generating a dungeon-like map using the Cellular Automaton algorithm. It initializes the following:
        - dimensions: The width and height of the grid.
        - min_room_size: The minimum size that a room can be.
        - max_room_size: The maximum size that a room can be.
        - num_rooms: The total number of rooms to generate in the dungeon.

    Parameters:
    None

    Returns:
    None
    """
```
    Examples

    ```python
# Basic usage: Initialize an object with default values
class MyClass:
    def __init__(self):
        self.value = 0

my_instance = MyClass()
print(my_instance.value)  # Output: 0
```

```python
# Edge case: Initialize with a custom value
class MyClass:
    def __init__(self, initial_value=5):
        self.value = initial_value

my_instance = MyClass(10)
print(my_instance.value)  # Output: 10
```

```python
# Advanced scenario: Using keyword arguments and default values
class MyClass:
    def __init__(self, name='John', age=30):
        self.name = name
        self.age = age

my_instance = MyClass(age=25)
print(my_instance.name)  # Output: John
print(my_instance.age)   # Output: 25
```
    Docstring

    """```python
class DungeonGenerator:
    """
    Initializes a new instance of the DungeonGenerator class.

    Attributes:
        x_size (int): The width of the dungeon grid in tiles.
        y_size (int): The height of the dungeon grid in tiles.
        min_room_size (int): The minimum size of a room to generate, in tiles.
        max_room_size (int): The maximum size of a room to generate, in tiles.
        num_rooms (int): The total number of rooms to generate. If not provided, calculated based on `min_rooms` and `max_rooms`.
        min_rooms (int): The minimum number of rooms to generate.
        max_rooms (int): The maximum number of rooms to generate.
        map (list of list of int): A 2D grid representing the dungeon layout with different values indicating areas.
        rooms (list of Room): A list of Room objects that have been generated in the dungeon.
        first_room (Room): The room where the player starts.
        last_room (Room): The room where stairs lead to the surface, if any are present.
        stairs_up (Room): The room above the last room.
        stairs_down (Room): The room below the last room.
        connected (bool): A flag indicating whether all rooms in the dungeon are connected.
        light (int): The current level of illumination in the dungeon.

    Returns:
        None
    """

    def __init__(self):
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
        self.stairs_up = None
        self.stairs_down = None
        self.connected = None
        self.light = 0

    Examples:
        >>> dungeon_generator = DungeonGenerator()
        >>> print(dungeon_generator.x_size)
        60
        >>> print(dungeon_generator.y_size)
        40
```"""
    ```