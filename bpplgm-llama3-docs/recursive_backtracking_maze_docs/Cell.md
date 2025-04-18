# Cell

    Purpose

    Here is a description of the purpose of this Python class in 1-2 sentences:

This `Cell` class represents a single cell on a grid or matrix and provides methods to check its neighboring cells for potential exploration.

Documentation of the existing functionality:

* The `__init__` method initializes a new `Cell` object with its row position (`x`) and column position (`y`). It also sets the `visited` attribute to `False`.
* The `check_neighbors` method determines the neighboring cells of the current cell by iterating over all possible directions (up, right, down, left) and checking if there are any unvisited neighboring cells in those directions. If a neighbor is found that has not been visited yet, it is added to a list of unvisited neighbors with their corresponding direction. The method randomly returns an unvisited neighbor's direction if more than one unvisited neighbor exists.

Examples:

* `cell = Cell(0, 0)`: Creates a new cell at position (0, 0).
* `neighbors = cell.check_neighbors()`: Returns a list of neighboring cells with their directions.
* `direction = neighbors[0]`: Returns the direction of an unvisited neighbor cell.
    Docstring

    """```python
class Cell:
    """
    Represents a single cell in a grid.

    Attributes:
        x (int): The row position of the cell.
        y (int): The column position of the cell.
        visited (bool): Whether the cell has been visited or not.
    """

    def __init__(self, x, y):
        """
        Initializes a new Cell object.

        Args:
            x (int): The row position of the cell.
            y (int): The column position of the cell.
        """
        self.x = x  # cell's row position
        self.y = y  # cell's column position
        self.visited = False

    def check_neighbors(self):
        """
        Returns a tuple containing a list of neighboring cells and their relative directions.

        Returns:
            tuple: A tuple where the first element is a list of neighboring cells, 
                   and the second element is a dictionary mapping direction indices to relative directions.
        """
        global cell_array
        neighbors = []  # keep track of the neighboring cells
        unvisited_directions = {}  # keep track of the relative direction of unvisited neighboring cells
        direction_key = 0  # keeps track of the number of directions available of unvisited cells

        # Check each direction to determine if neighboring cells exist on the cell_array
        if index(self.x, self.y - 1):
            up = cell_array[index(self.x, self.y - 1)]
        if index(self.x + 1, self.y):
            right = cell_array[index(self.x + 1, self.y)]
        if index(self.x, self.y + 1):
            down = cell_array[index(self.x, self.y + 1)]
        if index(self.x - 1, self.y):
            left = cell_array[index(self.x - 1, self.y)]

        # If the cell has a neighbor in a particular direction, check if that neighbor has been visited yet
        if up and not up.visited:
            neighbors.append(up)
            unvisited_directions[direction_key] = 'up'
            direction_key += 1
        if right and not right.visited:
            neighbors.append(right)
            unvisited_directions[direction_key] = 'right'
            direction_key += 1
        if down and not down.visited:
            neighbors.append(down)
            unvisited_directions[direction_key] = 'down'
            direction_key += 1
        if left and not left.visited:
            neighbors.append(left)
            unvisited_directions[direction_key] = 'left'

        # Return a random direction from the unvisited neighbors, or None if no neighbors exist
        if len(neighbors) > 0:
            r = int(math.floor(random.uniform(0, len(neighbors) - .000001)))
            return neighbors[r], unvisited_directions[r]
        else:
            return None, None

```"""
    ```