# connect_rooms

    Purpose

    ```
        ---
    ```
        ---
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
    ```
        ---
    ```
        ---
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
            ---
    ```
        ---
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
        ---
    ```
        ---
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
    Parameters

    
    Returns

    """
    Examples

    ```python
    # Basic usage
    >>> from connect_rooms import connect_rooms
    >>> rooms = ['room1', 'room2', 'room3']
    >>> connect_rooms(rooms)
    {
        'room1': {'room2', 'room3'},
        'room2': {'room1', 'room3'},
        'room3': {'room1', 'room2'}
    }
    ```

    ```python
    # Edge case: Room with no neighbors
    >>> from connect_rooms import connect_rooms
    >>> rooms = ['room1']
    >>> connect_rooms(rooms)
    {
        'room1': set()
    }
    ```

    ```python
    # Advanced scenario: Multiple rooms with neighbors
    >>> from connect_rooms import connect_rooms
    >>> rooms = ['room1', 'room2', 'room3', 'room4', 'room5']
    >>> connect_rooms(rooms)
    {
        'room1': {'room2', 'room5'},
        'room2': {'room1', 'room3', 'room4'},
        'room3': {'room2'},
        'room4': {'room2'},
        'room5': {'room1'}
    }
    ```

"""
---
- Author: [Misael Hernandez](https://twitter.com/misaelhm09)
- Date: 2023-06-02
- Repository: https://github.com/misaelhm/python_examples
- License: MIT License
---
"""
    Docstring

    """```
    ```python
    def connect_rooms(self, room, closest_room, good):
        '''
        Connect a room to a closest room and return a path.
        :param room: The room to connect.
        :type room: dict
        :param closest_room: The closest room to connect to.
        :type closest_room: dict
        :param good: True if we should connect the rooms in a good way.
        :type good: bool
        :return: A path in the map.
        :rtype: list
        '''
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
                    p"""
    ```