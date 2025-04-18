# count_alive_neighbors

    Purpose

    ```
    This function counts the number of alive neighbors for a given point in a live_map. The function takes in a live_map as a list of lists where each cell is True or False. The function starts by initializing a count variable to 0 and then loops through the live_map using nested loops to iterate over all the points in the map. The function then uses an i and j variable to iterate through the neighbors of the given point, starting with the middle point. If we're looking at the middle point, we don't want to add ourselves to the count, so we skip that check. If the index we're looking at is off the edge of the live_map, we add 1 to the count variable and continue. Otherwise, a normal check of the neighbour is made using an elif statement. If the neighbour is True, we add 1 to the count variable. We then return the count.
    ```
        ```
    def count_alive_neighbors(live_map, x, y):
    count = 0
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            neighbor_x = x + i
            neighbor_y = y + j
            # If we're looking at the middle point
            if i == 0 and j == 0:
                pass
            # In case the index we're looking at it off the edge of the live_map
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(live_map) or neighbor_y >= len(live_map[0]):
                count += 1
            # Otherwise, a normal check of the neighbour
            elif live_map[neighbor_x][neighbor_y] is True:
                count += 1
            j += 1
        i += 1
    return count
    ```
    ```
    This function counts the number of alive neighbors for a given point in a live_map. The function takes in a live_map as a list of lists where each cell is True or False. The function starts by initializing a count variable to 0 and then loops through the live_map using nested loops to iterate over all the points in the map. The function then uses an i and j variable to iterate through the neighbors of the given point, starting with the middle point. If we're looking at the middle point, we don't want to add ourselves to the count, so we skip that check. If the index we're looking at is off the edge of the live_map, we add 1 to the count variable and continue. Otherwise, a normal check of the neighbour is made using an elif statement. If the neighbour is True, we add 1 to the c
    Parameters

    
    Returns

    ```
    Examples

    """
    import pytest
    from alive_tools import count_alive_neighbors


    def test_main():
        pytest.skip('Write the actual test here.')
    def test_edge_case():
        pytest.skip('Write the actual test here.')
    def test_advanced():
        pytest.skip('Write the actual test here.')


    @pytest.mark.parametrize('board,expected',
    [
        # Basic usage
        pytest.param(
            [],
            0,
            id='Empty board',
        ),
        pytest.param(
            [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
            3,
            id='Basic board',
        ),
        # Edge case
        pytest.param(
            [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]],
            4,
            id='Board of odd size',
        ),
        # Advanced scenario
        pytest.param(
            [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            0,
            id='Board of even size with all zeros',
        ),
    ]
    )
    def test_count_alive_neighbors(board, expected):
        assert count_alive_neighbors(board) == expected

"""
- Basic usage:
"""
    ```python
    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """

- Edge case:
"""
    ```python
    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 0, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 4
    """

- Advanced scenario:
"""
    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 0, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 0
    """

- Additional edge case:
"""
    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 2
    """


    """
    # Explanation
    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 4
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 0, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 0
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 2
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 4
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 4
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 2
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 4
    """

    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 0, 1, 0],
    ...     [1, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [0, 0, 0, 0],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 3
    """


    >>> from alive_tools import count_alive_neighbors
    >>> board = [
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ...     [1, 1, 1, 1],
    ... ]
    >>> count_alive_neighbors(board)
    >>> 2
    """

    >>> from alive_tool
    Docstring

    """Only offer suggestions if I can tell you.
    ```"""
    ```