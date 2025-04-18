# perform_game_of_life_iteration

    Purpose

    ```python
    def cou
    Parameters

    ```

For function 'perform_game_of_life_iteration', document these parameters: ['old_map']
    Function purpose: ```python
    def cou
    Provide Google-style parameter documentation with:
    - Name
    - Type
    - Description
    - Any usage constraints

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```

For function 'get_next_generation_map', document these parameters: ['current_generation_map']
    Function purpose: ```python
    def cou
    Provide Google-style parameter documentation with:
    - Name
    - Type
    - Description
    - Any usage constraints

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```

For function 'get_current_generation_map', document these parameters: ['map', 'generatio
    Returns

    DO NOT INCLUDE THE CODE TO PERFORM THE ITERATION OF THE GAME OF LIFE.
    ```
    - Function signature: ```python
    def perform_game_of_life_iteration(map: List[List[int]]):
        """
        Perform a single iteration of Conway's Game of Life on a given map.

        Args:
            map (List[List[int]]): The current map of cells, represented as a list of lists, where '1' represents live cells and '0' represents dead cells.

        Returns:
            List[List[int]]: A new map representing the updated map after the iteration.
        """
        ```
    - Arguments: None

    - Return type: ```python
    def cou
    Function
    Args: None
    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    DO NOT INCLUDE THE CODE TO PERFORM THE ITERATION OF THE GAME OF LIFE.
    ```
    - Function signature: ```python
    def perform_game_of_life_iteration(map: List[List[int]]) -> List[List[int]]:
        """
        Perform a single iteration of Conway's Game of Life on a given map.

        Args:
            map (List[List[int]]): The current map of cells, represented as a list of lists, where '1' represents live cells and '0' represents dead cells.

        Returns:
            List[List[int]]: A new map representing the updated map after the iteration.
        """
        ```
    - Arguments: None

    - Return type: ```python
    def cou
    Function
    Args: None
    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    DO NOT INCLUDE THE CODE TO PERFORM THE ITERATION OF THE GAME OF LIFE.
    ```
    - Function signature: ```python
    def perform_game_of_life_iteration(map: List[List[int]]):
    Examples

    Do not use any code that could be used in production.
    """

    def test_perform_game_of_life_iteration():
        """
        # Explanation
        Perform game of life iteration.
        """
        import numpy as np
        from scipy.signal import correlate2d

        @jit(nopython=True, fastmath=True)
        def neighbors(data):
            """
            Returns a numpy array with the number of neighbors
            for each cell in the input array.
            """
            kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
            neighborhood = correlate2d(data, kernel, mode="same", boundary="wrap")
            neighborhood[data == 1] = neighborhood[data == 1] - 1
            return neighborhood

        @jit(nopython=True, fastmath=True)
        def iterate(arr):
            """
            Returns a numpy array with the next generation of the input array.
            """
            neighborhood = neighbors(arr)
            return (
                (arr == 1) & (neighborhood < 2)
                | (arr == 0) & (neighborhood == 3)
                | ((arr == 1) & (2 <= neighborhood) & (neighborhood <= 3))
            )

        @jit(nopython=True, fastmath=True)
        def perform_game_of_life_iteration(arr):
            """
            Perform game of life iteration.
            """
            arr_next = iterate(arr)
            arr[arr_next] = 1
            arr[arr == 1] = 0
            return arr

    def test_perform_game_of_life_iteration_edge_case():
        """
        Perform game of life iteration with an edge case.
        """
        import numpy as np
        from scipy.signal import correlate2d

        @jit(nopython=True, fastmath=True)
        def neighbors(data):
            """
            Returns a numpy array with the number of neighbors
            for each cell in the input array.
            """
            kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
            neighborhood = correlate2d(data, kernel, mode="same", boundary="wrap")
            neighborhood[data == 1] =
    Docstring

    """```
    def perform_game_of_life_iteration(old_map):
    """
    Iterate a single generation of Conway's Game of Life.
    This will return a new map where False is open and True is a wall.
    Args:
        old_map: The level map to iterate
    Returns:
        A new map where False is open and True is a wall.
    """
    new_map = [[False for i in range(WIDTH)] for j in range(HEIGHT)]
    for x in range(len(old_map)):
        for y in range(len(old_map[0])):
            live_neighbor_count = count_alive_neighbors(old_map, x, y)

            if old_map[x][y] is True:
                if live_neighbor_count < DEATH_LIMIT:
                    new_map[x][y] = False
                else:
                    new_map[x][y] = T"""
    ```