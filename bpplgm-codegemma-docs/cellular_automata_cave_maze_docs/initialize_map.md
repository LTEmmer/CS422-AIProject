# initialize_map

    Purpose

    This function initializes the map for Conway's Game of Life using a helper function called alive_calc() that calculates whether a cell is alive or dead based on its neighboring cells. The function then creates a 2D list called initial_map with a size based on the WIDTH and HEIGHT constants and initializes each cell's value based on the value returned by the alive_calc() function.

    The alive_calc() function takes in a cell's position (x, y) and a 2D list called board and returns whether the cell is alive or dead based on the sum of its neighbors. The sum of neighbors is calculated using a nested for loop that iterates over the neighboring cells and adds the value of each cell to the sum.

    The initialize_map() function creates a 2D list called initial_map with a size based on the WIDTH and HEIGHT constants and initializes each cell's value based on the value returned by the alive_calc() function. The for loop iterates over each cell in the initial_map and updates its value based on the value returned by the alive_calc() function.

    The result is a 2D list called initial_map that represents the initial state of the Conway's Game of Life board, where each cell in the board represents whether a cell is alive or dead based on its neighboring cells. The function is designed to create a starting configuration for Conway's Game of Life based on the current state of the board.

    ```python
    def alive_calc(board, x, y):
    sum_of_neighbors = 0
    neighbor_positions = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    for neighbor_pos in neighbor_positions:
    if neighbor_pos[0] >= 0 and neighbor_pos[0] < len(board) and neighbor_pos[1] >= 0 and neighbor_pos[1] < len(board[0]):
    sum_of_neighbors += board[neighbor_pos[0]][neighbor_pos[1]]
    return sum_of_neighbors % 2
    ```
            This function takes in a 2D list called board, a position (x, y), and returns whether a cell is alive or dead based on its neighboring cells. The sum of neighbors is calculated using a nested for loop that iterates over the neighboring cells and adds the value of each cell to the sum.

    The function then calculates whether a cell is alive or dead based on the sum of its neighbors and returns the result. The result is a value (either 0 or 1) representing whether the cell is alive or dead, based on whether its sum of neighbors is equal to 3 or whether it is equal to 2 and its immediate neighbors are also alive.

    The function assumes that the input board has already been validated to ensure that it is a 2D list of size WIDTH x HEIGHT. The function also assumes that x and y are within the valid range for the input board.

    The result is a value (either 0 or 1) representing whether a cell is alive or dead, based on whether its sum of neighbors is equal to 3 or whether it is equal to 2 and its immediate neighbors are also alive. The function is designed to calculate whether a cell i
    Parameters

    
    Returns

    
    Examples

    ### Code

    ```python
    # Explanation
    ```

    ### Explanation

    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)

    ### Code

    ```python
    # Explanation
    ```

    ### Explanation

    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)

    ### Code

    ```python
    # Explanation
    ```

    ### Explanation

    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)

    ### Code

    ```python
    # Explanation
    ```

    ### Explanation

    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)
    - Explanation: Code Explanation (Provide a concise explanation of the code)

    ### Code

    ```python
    # Explanatio
    Docstring

    """"""
    ```
    ```
    def initialize_map():
    """
    Creates a map of the initial state of game of life, this is a 2D array
    and has a size equal to the WIDTH, HEIGHT and a starting cell that is randomly
    determined.

    Parameters
    ----------
    None

    Returns
    -------
    map

    Examples
    --------
    >>> initialize_map()
    """
    initial_map = [[alive_calc() for i in range(WIDTH)] for j in range(HEIGHT)]
    return initial_map

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.

    """
    ```
    ```
    def initialize_map():
    """
    Creates a map of the initial state of game of life, this is a 2D array
    and has a size equal to the WIDTH, HEIGHT and a starting cell that is randomly
    determined.

    Parameters
    ----------
    None

    Returns
    -------
    map

    Examples
    --------
    >>> initialize_map()
    """
    initial_map = [[alive_calc() for i in range(WIDTH)] for j in range(HEIGHT)]
    return initial_map

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section s"""
    ```