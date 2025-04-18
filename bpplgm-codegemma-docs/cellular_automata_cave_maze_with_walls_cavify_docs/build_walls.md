# build_walls

    Purpose

    *The purpose of this function is to create walls around visited positions and place them as walls until the list of visited positions is empty.
    ```python
    def check_neighbors_and_place_wall(position):
        if(not visited.contains(position)):
            for neighbor in position.neighbors:
                if(not visited.contains(neighbor)):
                    visited.add(neighbor)
        elif(position.wall is None):
            position.wall = Wall(position)
        ```
    *This function checks the neighbors of a position and adds the neighbor to the visited list if it has not been visited yet. If a wall is not already placed in the position, a new Wall object is created and added to the position.
    ```python
    def add_to_visited(self, position):
    visited.add(position)
    ```
    *This function adds a position to the visited list, effectively marking it as visited.
    ```python
    def has_not_visited(self, position):
    return position not in visited
    ```
    *This function returns True if the position is not in the visited list, meaning it has not been visited yet.
    ```python
    def add(self, position):
    if(not has_not_visited(position)):
        visited.remove(position)
    ```
    *This function adds a position to the visited list, removing it if it has already been visited.
    ```python
    def build(self):
    visited.clear()
    visited.add(start_position)
    ```
    *This function builds the maze by starting with the start position and marking it as visited, then checking the neighbors of the current position and adding them to the visited list if they have not been visited yet.
    ```python
    def build_walls(self):
    for position in visited:
        check_neighbors_and_place_wall(position)
    ```
    *This function loops through the list of visited positions and checks the neighbors of each position and adds them to the visited list if they have not been visited yet.
    ```python
    def check_neighbors_and_place_wall(self, position):
        if(not visited.contains(position)):
            for neighbor in position.neighbors:
                if(not visited.contains(neighbor)):
                    visited.add(neighbor)
        elif(position.wall is None):
            position.wall = Wall(position)
    ```
    *This function checks the neighbors of a position and adds the neighbor to the visited list if it has not been visited yet. If a wall is not already placed in the position, a new Wall object is created and added to the position.
    ```python
    def has_not_visited(self, position):
    return position not in visited
    ```
    *This function returns True if the position is not in the visited list, meaning it has not been visited yet.
    ```python
    def add(self, position):
    if(not has_not_visited(position)):
        visited.remove(position)
    ```
    *This function adds a position to the visited list, removing it if it has already been visited.
    ```python
    def add_to_visited(self, position):
    visited.add(position)
    ```
    *This function adds a position to the visited list, effectively marking it as visited.
    ```python
    def remove(self, position):
    visited.remove(position)
    ```
    *This function removes a position from the visited list, effectively marking it as not visited.
    ```python
    def remove(self, position):
    if(visited.contains(position)):
        visited.remove(position)
    ```
    *This function removes a position from the visited list, effectively marking it as not visited.
    ```python
    def has_not_visited(self, position):
    return position not in visited
    ```
    *This function returns True if the position is not in the visited list, meaning it has not been visited yet.
    ```python
    def build(self):
    visited.clear()
    visited.add(start_position)
    ```
    *This function builds the maze by starting with the start position and marking it as visited, then checking the neighbors of the current position and adding them to the visited list if they have not been visited yet.
    ```python
    def build_walls(self):
    for position in visited:
        check_neighbors_and_place_wall(position)
    ```
    *This function loops through the list of visited positions and checks the neighbors of each position and adds the
    Parameters

    
    Returns

    
    Examples

    No additional context about the problem/situation is needed.
    You do not need to write any pseudo-code, type hints, or documentation.
    Write code in Python.
    ```python
    # Explanation
    code
    ```

    Replace ``<your-code>`` with your code.


Basic usage:
```python
# Explanation
```

Code snippet:

```python
# Explanation
```

Edge case:
```python
# Explanation
```

Code snippet:

```python
# Explanation
```

Advanced scenario (if applicable):
```python
# Explanation
```

Code snippet:

```python
# Explanation
```
    Docstring

    """```
    """

    """
    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    """

    def build_walls():
    """
    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    """
    for position in visited:
        check_neighbors_and_place_wall(position)

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as w"""
    ```