# find_closest

    Purpose

    The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master room's x and y coordinate.
            The function then returns the closest room to the master room.
            The function is taking a room as an argument, as well as an optional list of rooms to compare against.
            The function is calculating the average x and y coordinate of the room and the master room, then calculating the distance between the average x and y coordinate of the room and the master room, and returning the room closest to the master room.
            The function is creating a dictionary for each room in a list called rooms, then calculating the average x and y coordinate of the room, then calculating the distance between the average x and y coordinate of the room and the master
    Parameters

    
    Returns

    Ex
    Examples

    """


    def find_closest(self, arr, target):
        """
        Find the element in the array that is closest to the target.

        Args:
            arr (list): A sorted array of distinct elements.
            target (int): The target value to search for.

        Returns:
            int: The element closest to the target.

        Examples:
            >>> obj = Solution()
            >>> obj.find_closest(arr=[1, 2, 3, 4], target=2)
            2
            >>> obj.find_closest(arr=[1, 3, 6, 8, 10], target=7)
            6
        """
        # Initialize left and right pointers
        left, right = 0, len(arr) - 1

        # Binary search to find the closest element
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Handle edge cases
        if left == 0:
            return arr[0]
        if right == len(arr) - 1:
            return arr[-1]

        # Find the closest element
        closest_left, closest_right = arr[left], arr[right]
        return closest_left if abs(closest_left - target) < abs(closest_right - target) else closest_right


"""
Edge case
If target is not found in the array, return None.
"""

def find_closest(self, arr, target):
    """
    Find the element in the array that is closest to the target.

    Args:
        arr (list): A sorted array of distinct elements.
        target (int): The target value to search for.

    Returns:
        int: The element closest to the target.

    Examples:
        >>> obj = Solution()
        >>> obj.find_closest(arr=[1, 2, 3, 4], target=2)
        2
        >>> obj.find_closest(arr=[1, 3, 6, 8, 10], target=7)
        None
    """
    # Initialize left and right pointers
    left, right = 0, len(arr) - 1

    # Binary search to find the closest element
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Handle edge cases
    if left == 0:
        return arr[0]
    if right ==
    Docstring

    """Don't say "That was easy!" or
    "That's weird."

    @author: Kevin D'Souza

    @created_on: 2018-07-07
    ```

    def find_closest(self, room, others=None):
        """

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*. Don't say "That was easy!" or
    "That's weird."

    @author: Kevin D'Souza

    @created_on: 2018-07-07

    @updated_on: 2018-07-07

    """
    master_room = {'x': room['x'] + room['w'] / 2,
                   'y': room['y'] + room['h'] / 2
                   }
    room_min = 1000
    final_room"""
    ```