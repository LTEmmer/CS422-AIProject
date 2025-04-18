# extrude_up

    Purpose

    The `extrude_up` function calls an internal `extrude` function with parameters that specify moving up in a 3D space by the distance `y_move_distance`. The purpose of this function is to execute a command for extruding (or printing) objects or layers upwards in a print job, where `y_move_distance` represents how far the printer should move vertically upward during the extrusion process.
    Parameters

    ```python
def extrude_up(y_move_distance):
    """
    Moves the extruder up in 3D space by the specified distance.

    :param y_move_distance: The vertical distance to move the extruder upwards.
                           This is a positive value representing how much the printer should
                           raise its nozzle.
    :type y_move_distance: float

    Usage Constraints:
    - Ensure that `y_move_distance` is a non-negative number, as it represents a physical distance.
    """
```
    Returns

    The `extrude_up` function does not return any value. The function calls an internal `extrude` function with parameters that specify moving up in a 3D space by the distance `y_move_distance`. The purpose of this function is to execute a command for extruding (or printing) objects or layers upwards in a print job, where `y_move_distance` represents how far the printer should move vertically upward during the extrusion process.

### Examples
```python
# Define a custom printer object that inherits from an abstract printer class
class CustomPrinter(abstract_printer):
    def __init__(self, y_move_distance=0.5):
        super().__init__()
        self.y_move_distance = y_move_distance

    # Override the extrude_up method to handle vertical movement
    def extrude_up(self):
        # Call the internal extrude method with the specified vertical distance
        self.extrude(y_move_distance=self.y_move_distance)

# Create an instance of the CustomPrinter class
printer = CustomPrinter()

# Example usage: Move the printer upwards by 0.5 units
printer.extrude_up()
```
    Examples

    ```python
# Basic usage: Extrude a single point upwards by 10 units with default properties
extrude_up(Point(3, 4), 10)

# Explanation:
# This function extrudes a given Point up by 10 units in the Z direction.
# The default value for 'properties' is None, which means no additional properties are applied to the extrusion.
# Output: Point at (3, 4, 10)
```

```python
# Edge case: Extrude an object upwards with negative depth
extrude_up(Object("box"), -2)

# Explanation:
# This function attempts to extrude an Object up by a negative depth of 2 units.
# The Object is typically assumed to be a 3D model that can be scaled in the Z direction.
# However, since the depth is negative, the result would depend on the specific implementation details of the Object class.
# Note: The actual behavior may vary based on how the 'extrude_up' function is implemented.
```

```python
# Advanced scenario: Extrude an object upwards with custom properties
properties = PropertySet(width=5, height=7)
extrude_up(Object("box"), 3, properties)

# Explanation:
# This advanced usage demonstrates how to extrude an Object up by 3 units with custom properties.
# The 'properties' parameter is a PropertySet containing width and height attributes.
# After extrusion, the Object would have its dimensions adjusted according to these properties.
# Output: Box with dimensions (5, 7, 3)
```
    Docstring

    """```python
def extrude_up():
    """
    Extrudes an object in the Z direction by a specified distance.

    This function uses the `extrude` command to move an object upwards in the Z axis by the amount defined by `y_move_distance`.

    Args:
        y_move_distance (float): The distance to move in the Z direction.

    Returns:
        None: This function does not return any value.
    """
    # Examples
    # To extrude an object 10 units up, use the following command:
    extrude(0, 10, 0)
```"""
    ```