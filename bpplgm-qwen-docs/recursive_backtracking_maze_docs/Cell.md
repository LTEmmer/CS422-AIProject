# Cell

    Purpose

    This Python class represents a cell in a grid and includes methods to check its neighbors. It tracks the cell's position and whether it has been visited. The `check_neighbors` method returns an unvisited neighbor cell and its direction relative to the current cell if any exist, or `None` otherwise.
    Docstring

    """```python
class Cell:
    """Represents a cell in a grid with properties for row position, column position,
    and whether it has been visited. It provides functionality to check neighboring cells
    and randomly return an unvisited neighbor."""
    
    def __init__(self, x, y):
        """
        Initialize the Cell instance.
        
        :param x: The row position of the cell.
        :param y: The column position of the cell.
        """
        self.x = x  # cell's row position
        self.y = y  # cell's column position
        self.visited = False

    def check_neighbors(self):
        """Check neighboring cells and return an unvisited neighbor if available."""
        global cell_array
        neighbors = []  # keep track of the neighboring cells
        unvisited_directions = {}  # keep track of the relative direction of unvisited neighboring cells
        direction_key = 0  # keeps track of the number of directions available of unvisited cells
        
        up = None
        right = None
        down = None
        left = None

        if index(self.x, self.y - 1):
            up = cell_array[index(self.x, self.y - 1)]
        if index(self.x + 1, self.y):
            right = cell_array[index(self.x + 1, self.y)]
        if index(self.x, self.y + 1):
            down = cell_array[index(self.x, self.y + 1)]
        if index(self.x - 1, self.y):
            left = cell_array[index(self.x - 1, self.y)]

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

        if len(neighbors) > 0:
            r = int(math.floor(random.uniform(0, len(neighbors) - .000001)))
            return neighbors[r], unvisited_directions[r]
        else:
            return None, None

# Example usage
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_array = [[Cell(i, j) for j in range(width)] for i in range(height)]

def index(x, y):
    """Calculate the 1D index of a cell given its row and column positions."""
    return x * width + y

# Example of how to use the Grid class
grid = Grid(5, 5)
cell = grid.cell_array[0][0]
neighbor, direction = cell.check_neighbors()
if neighbor:
    print(f"Unvisited neighbor found in {direction}.")
else:
    print("No unvisited neighbors available.")
```"""
    ```