# add_inner_walls

    Purpose

    ## The purpose of this function is to build walls on an n x n grid based on the provided input parameters: level_map, rmin, cmin, rmax, and cmax. The code defines a function called add_inner_walls that recursively divides the grid into smaller boxes based on the provided input parameters and builds walls on the border of each box. The function also defines a function called build_wall that builds a wall on the grid at a given location. The code also defines a function called random_number that generates a random number between two provided input parameters.
    ## The function add_inner_walls is called with the provided parameters and returns the updated level_map grid after all the walls have been added. The code also defines a variable called MIN_SIZE and sets it to an arbitrary small value of 1. The code also defines a variable called is_vertical and sets it to a boolean value based on whether or not the grid is vertical or horizontal. The code also defines a variable called width and sets it to the difference between cmax and cmin. The code also defines a variable called height and sets it to the difference between rmax and rmin. The code also defines a variable called col and sets it to a random number between cmin and cmax and is multiplied by 2. The code also defines a variable called row and sets it to a random number between rmin and rmax and is multiplied by 2. The code also defines a variable called level_map and sets it to the input parameter. The code also defines a variable called rmin and sets it to the input parameter. The code also defines a variable called cmin and sets it to the input parameter. The code also defines a variable called rmax and sets it to the input parameter. The code also defines a variable called cmax and sets it to the input parameter. The code also defines a variable called is_vertical and sets it to a boolean value based on whether or not the grid is vertical or horizontal. The code also defines a variable called width and sets it to the difference between cmax and cmin. The code also defines a variable called height and sets it to the difference between rmax and rmin. The code also defines a variable called col and sets it to a random number between cmin and cmax and is multiplied by 2. The code also defines a variable called row and sets it to a random number between rmin and rmax and is multiplied by 2. The code also defines a variable called level_map and sets it to the input parameter. The code also defines a variable called rmin and sets it to the input parameter. The code also defines a variable called cmin and sets it to the input parameter. The code also defines a variable called rmax and sets it to the input parameter. The code also defines a variable called cmax and sets it to the input parameter.
    ## The code defines a variable called MIN_SIZE and sets it to an arbitrary small value of 1. The code also defines a variable called is_vertical and sets it to a boolean value based on whether or not the grid is vertical or horizontal. The code also defines a variable called width and sets it to the difference between cmax and cmin. The code also defines a variable called height and sets it to the difference between rmax and rmin. The code also defines a variable called col and sets it to a random number between cmin and cmax and is multiplied by 2. The code also defines a variable called row and sets it to a random number between rmin and rmax and is multiplied by 2. The code also defines a variable called level_map and sets it to the input parameter. The code also defines a variable called rmin and sets it to the input parameter. The code also defines a variable called cmin and sets it to the input parameter. The code also defines a variable called rmax and sets it to the input parameter. The code also defines a variable called cmax and sets it to the input parameter.
    ## The code defines a variable called MIN_SIZE and sets it to an arbitrary small value of 1. The code also defines a variable called is_vertical and sets it to a boolean value based on whether or not the grid is vertical or horiz
    Parameters

    T
    Returns

    @param {Array} level_map The current level map.
    @param
    Examples

    Ensure that the code executes as expected.
    ```python
    # Explanation
    code
    ```
    
    
    

# Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 0))
```

Explanation
add_inner_walls(wall, (0, 0, 0), (1, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 1))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 1, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (1, 0, 0))
```
```python
add_inner_walls(wall, (0, 0, 0), (0, 1, 0))
```
```pyth
    Docstring

    """```
    def add_inner_walls(level_map, rmin, cmin, rmax, cmax):
        """
        Args:
            level_map (list): 2d array representing map
            rmin, cmin, rmax, cmax (int): bounding box
        """
        width = cmax - cmin
        height = rmax - rmin

        # stop recursing once room size is reached
        if width < MIN_SIZE or height < MIN_SIZE:
            return level_map

        # determine whether to build vertical or horizontal wall
        if width > height:
            is_vertical = True
        else:
            is_vertical = False

        if is_vertical:
            # randomize location of vertical wall
            col = math.floor(random_number(cmin, cmax) / 2) * 2
            build_wall(level_map, is_vertical, rmin, rmax, col)
            # recurse to the two new"""
    ```