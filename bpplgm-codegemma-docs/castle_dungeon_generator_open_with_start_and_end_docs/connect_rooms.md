# connect_rooms

    Purpose

    ```python
    def connect_rooms(self, room, closest_room, good):
        path_part_1 = {
            'x': get_random_int(room['x'], room['x'] + room['w']),
            'y': get_random_int(room['y'], room['y'] + room['h'])
        }
        path_part_2 = {
            'x': get_random_int(closest_room['x'], closest_room['x'] + closest_room['w']),
            'y': get_random_int(closest_room['y'], closest_room['y'] + closest_room['h'])
        }
        while path_part_1['x'] != path_part_2['x'] or path_part_1['y'] != path_part_2['y']:
            if path_part_1["x"] != path_part_2["x"]:
                if path_part_2["x"] < path_part_1["x"]:
                    path_part_2["x"] += 1
                else:
                    path_part_2["x"] -= 1
            else:
                if path_part_1["y"] != path_part_2["y"]:
                    if path_part_2["y"] < path_part_1["y"]:
                        path_part_2["y"] += 1
                    else:
                        path_part_2["y"] -= 1

            self.map[path_part_2['y']][path_part_2['x']]['t'] = 1
        if good:
            room['c'] = True
            closest_room['c'] = True
            self.connected.append(room)
    ```
    ```python
    def connect_rooms(self, room, closest_room, good):
        path_part_1 = {
            'x': get_random_int(room['x'], room['x'] + room['w']),
            'y': get_random_int(room['y'], room['y'] + room['h'])
        }
        path_part_2 = {
            'x': get_random_int(closest_room['x'], closest_room['x'] + closest_room['w']),
            'y': get_random_int(closest_room['y'], closest_room['y'] + closest_room['h'])
        }
        while path_part_1['x'] != path_part_2['x'] or path_part_1['y'] != path_part_2['y']:
            if path_part_1["x"] != path_part_2["x"]:
                if path_part_2["x"] < path_part_1["x"]:
                    path_part_2["x"] += 1
                else:
                    path_part_2["x"] -= 1
            else:
                if path_part_1["y"] != path_part_2["y"]:
                    if path_part_2["y"] < path_part_1["y"]:
                        path_part_2["y"] += 1
                    else:
                        path_part_2["y"] -= 1

            self.map[path_part_2['y']][path_part_2['x']]['t'] = 1
        if good:
            room['c'] = True
            closest_room['c'] = True
            self.connected.append(room)
    ```
    ```python
    def connect_rooms(self, room, closest_room, good):
        path_part_1 = {
            'x': get_random_int(room['x'], room['x'] + room['w']),
            'y': get_random_int(room['y'], room['y'] + room['h'])
        }
        path_part_2 = {
            'x': get_random_int(closest_room['x'], closest_room['x'] + closest_room['w']),
            'y': get_random_int(closest_room['y'], closest_room['y'] + closest_room['h'])
        }
        while path_part_1['x'] != path_part_2['x'] or path_part_1['y'] != path_part_2['y']:
            if path_part_1["x"] != path_part_2["x"]:
                if path_part_2["x"] < path_part_1["x"]:
                    path_part_2["x"] += 1
                else:
                    path_part_2["x"] -= 1
            else:
                if path_part_1["y"] != path_part_2["y"]:
                    if path_part_2["y"] < path_part_1["y"]:
                        path_part_2["y"] += 1
                    else:
                        path_part_2["y"] -= 1

            self.map[path_part_2['y']][path_part_2['x']]['t'] = 1
        if good:
            room['c'] = True
            closest_room['c'] = True
            self.connected.append(room)
    ```
    ```python
    def connect_rooms(self, room, closest_room, good):
        path_part_1 = {
            'x': get_random_int(room['x'], room['x'] + room['w']),
            'y': get_random_int(room['y'], room['y'] + room['h'])
        }
        path_part_2 = {
            'x': get_random_int(closest_room['x'], closest_room['x'] + closest_room['w']),
            'y': get_random_int(closest_room['y'], closest_room['y'] + closest_room['h'])
        }
        while path_part_1['x'] != path_part_2['x'] or path_part_1['y'] != path_part_2['y']:
            if path_part_1["x"] != path_part_2["x"]:
                if path_part_2["x"] < path_part_1["x"
    Parameters

    
    Returns

    ```
    Examples

    ---
    
    Example 1:
    ```python
    >>> # Explanation
    >>> connect_rooms(room_list)
    ```
    
    Example 2:
    ```python
    >>> # Explanation
    >>> connect_rooms(room_list)
    ```
    
    Example 3:
    ```python
    >>> # Explanation
    >>> connect_rooms(room_list)
    ```

"""

import logging
from typing import List, Tuple

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

# Function to connect rooms based on their usage
def connect_rooms(room_list: List[Tuple[str, int]]) -> List[List[str]]:
    """
    Connect rooms based on their usage.

    Args:
        room_list (List[Tuple[str, int]]): List of rooms with their usage count.

    Returns:
        List[List[str]]: List of connected rooms.
    """
    # Sort the rooms by usage count in ascending order
    sorted_rooms = sorted(room_list, key=lambda x: x[1])

    # Initialize an empty list to store the connected rooms
    connected_rooms = []

    # Initialize an empty list to store the rooms that are part of a connected group
    current_group = []

    # Iterate over the sorted rooms
    for i, (room, usage) in enumerate(sorted_rooms):
        # If the room is not in the current group, add it to the group
        if room not in current_group:
            current_group.append(room)

            # If the group is of length 2, connect the rooms and add them to the connected rooms list
            if len(current_group) == 2:
                connected_rooms.append(current_group)
                current_group = []

        # Add the room to the current group
        if i != len(sorted_rooms) - 1:
            if sorted_rooms[i+1][1] < usage:
                current_group.append(room)

    # If there is a group left in the current group, connect the rooms and add them to the connected rooms list
    if current_group:
        connected_rooms.append(current_group)

    return connected_rooms

# Example 1: Basic usage
room_list1 = [("A", 1), ("B", 2), ("C", 3)]
print(connect_rooms(room_list1))

# Example 2: Edge case
room_list2 = [("A", 2),
    Docstring

    """Do not describe alternative explanations.
    Do not describe alternative explanations in prose.
    Do not offer suggestions.
    Do not offer alternative explanations.
    ```
```
```python
def connect_rooms(self, room, closest_room, good):
    path_part_1 = {
        'x': get_random_int(room['x'], room['x'] + room['w']),
        'y': get_random_int(room['y'], room['y'] + room['h'])
    }
    path_part_2 = {
        'x': get_random_int(closest_room['x'], closest_room['x'] + closest_room['w']),
        'y': get_random_int(closest_room['y'], closest_room['y'] + closest_room['h'])
    }
    while path_part_1['x'] != path_part_2['x'] or path_part_1['y'] != path_part_2['y']:
        if path_part_1["x"] != path_part_2["x"]:
            if path_part_2["x"] < path_part_1["x"]:
                path_part_2["x"] += 1
            else:
                path_part_2["x"] -= 1
        else:
            if path_part_1["y"] != path_part_2["y"]:
                if path_part_2["y"] < path_part_1["y"]:
                    path_part_2["y"] += 1
                else:
                    path_part_2["y"] -= 1

        self.map[path_part_2['y']][path_part_2['x'"""
    ```