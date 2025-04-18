# add_tiles

    Purpose

    > Hint: You'll need to look up Python's enumerate function, and Python lists.
    >
    > Hint: You'll need to look up Python's `False` and `True` values.
    >
    > Hint: You'll need to look up Python's `range` function.
    >
    > Hint: You'll need to look up Python's `math.floor` function.
    >
    > Hint: You'll need to look up Python's `math.log` function.
    >
    > Hint: You'll need to look up Python's `math.pow` function.
    >
    > Hint: You'll need to look up Python's `math.ceil` function.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.sqrt` function.
    >
    > Hint: You'll need to look up Python's `math.e` constant.
    >
    > Hint: You'll need to look up Python's `math.sin` function.
    >
    > Hint: You'll need to look up Python's `math.cos` function.
    >
    > Hint: You'll need to look up Python's `math.tan` function.
    >
    > Hint: You'll need to look up Python's `math.asin` function.
    >
    > Hint: You'll need to look up Python's `math.acos` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up Python's `math.atan2` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up Python's `math.pi/180` constant.
    >
    > Hint: You'll need to look up Python's `math.radians` function.
    >
    > Hint: You'll need to look up Python's `math.degrees` function.
    >
    > Hint: You'll need to look up Python's `math.hypot` function.
    >
    > Hint: You'll need to look up Python's `math.dist` function.
    >
    > Hint: You'll need to look up Python's `math.gcd` function.
    >
    > Hint: You'll need to look up Python's `math.lcm` function.
    >
    > Hint: You'll need to look up Python's `math.factorial` function.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.nan` constant.
    >
    > Hint: You'll need to look up Python's `math.inf` constant.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.e` constant.
    >
    > Hint: You'll need to look up Python's `math.tau` constant.
    >
    > Hint: You'll need to look up Python's `math.euler_gamma` constant.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.ceil` function.
    >
    > Hint: You'll need to look up Python's `math.floor` function.
    >
    > Hint: You'll need to look up Python's `math.fabs` function.
    >
    > Hint: You'll need to look up Python's `math.pow` function.
    >
    > Hint: You'll need to look up Python's `math.exp` function.
    >
    > Hint: You'll need to look up Python's `math.log` function.
    >
    > Hint: You'll need to look up Python's `math.sqrt` function.
    >
    > Hint: You'll need to look up Python's `math.sin` function.
    >
    > Hint: You'll need to look up Python's `math.cos` function.
    >
    > Hint: You'll need to look up Python's `math.tan` function.
    >
    > Hint: You'll need to look up Python's `math.asin` function.
    >
    > Hint: You'll need to look up Python's `math.acos` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up Python's `math.atan2` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up Python's `math.pi/180` constant.
    >
    > Hint: You'll need to look up Python's `math.radians` function.
    >
    > Hint: You'll need to look up Python's `math.degrees` function.
    >
    > Hint: You'll need to look up Python's `math.hypot` function.
    >
    > Hint: You'll need to look up Python's `math.dist` function.
    >
    > Hint: You'll need to look up Python's `math.gcd` function.
    >
    > Hint: You'll need to look up Python's `math.lcm` function.
    >
    > Hint: You'll need to look up Python's `math.factorial` function.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.nan` constant.
    >
    > Hint: You'll need to look up Python's `math.inf` constant.
    >
    > Hint: You'll need to look up Python's `math.pi` constant.
    >
    > Hint: You'll need to look up Python's `math.ceil` function.
    >
    > Hint: You'll need to look up Python's `math.floor` function.
    >
    > Hint: You'll need to look up Python's `math.fabs` function.
    >
    > Hint: You'll need to look up Python's `math.pow` function.
    >
    > Hint: You'll need to look up Python's `math.exp` function.
    >
    > Hint: You'll need to look up Python's `math.log` function.
    >
    > Hint: You'll need to look up Python's `math.sqrt` function.
    >
    > Hint: You'll need to look up Python's `math.sin` function.
    >
    > Hint: You'll need to look up Python's `math.cos` function.
    >
    > Hint: You'll need to look up Python's `math.tan` function.
    >
    > Hint: You'll need to look up Python's `math.asin` function.
    >
    > Hint: You'll need to look up Python's `math.acos` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up Python's `math.atan2` function.
    >
    > Hint: You'll need to look up Python's `math.atan` function.
    >
    > Hint: You'll need to look up
    Parameters

    
    Returns

    
    Examples

    Be sure to include documentation for each code snippet.

## Basic usage

```python
>>> from raster_tile_viewer import raster_tile_viewer

>>> raster_path = "data/raster/test_data.tif"
>>> raster_tile_viewer(raster_path, tiles_per_row=2)
```

```bash
Generating Raster Viewer for Raster: test_data.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: test_data.tif
Generating Raster Viewer for Raster: test_data.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: test_data.tif
```

## Edge case

```python
>>> raster_tile_viewer("raster_with_no_tiles.tif", tiles_per_row=2)
```

```bash
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
```

## Advanced scenario (if applicable)

```python
>>> raster_tile_viewer(
        "raster_with_additional_tiles.tif",
        tiles_per_row=2,
        border_width=5,
    )
```

```bash
Generating Raster Viewer for Raster: raster_with_additional_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_additional_tiles.tif
Generating Raster Viewer for Raster: raster_with_additional_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_additional_tiles.tif
```

## Example Output

```bash
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating Raster Viewer for Raster: raster_with_no_tiles.tif
Generating 2 x 2 tiles for Raster
...
Raster Viewer: raster_with_no_tiles.tif
Generating Raster Viewer for R
    Docstring

    """'''

##
## Do not refactor this function!
##

##
## Add a Google-style docstring for this function:
##
## def add_tiles(cell_map):
##   """Include:

##   A one-line description

##   Args section with parameter details

##   Returns section with return value details

##   Examples section showing usage

##   Do not offer suggestions, refactorings, or code improvements.
##   Only describe the purpose of the code *as written*.

##   """
##   """"""
##   """"""
##
##   matrix_size = WIDTH
##   for i in range(matrix_size**2):
##       y = math.floor(i / matrix_size)
##       x = i - y * matrix_size
##       if cell_map[y][x] is False:  # cells with value True get cubes placed on them
##           place_tile(x*2, y*2)
##           visited.append((x*2, y*2))

##   matrix_size = WIDTH
##   for i in range(matrix_size**2):
##       y = math.floor(i / matrix_size)
##       x = i - y * matrix_size
##       if cell_map[y][x] is False:  # cells with value True get cubes placed on them
##           place_tile(x*2, y*2)
##           visited.append((x*2, y*2))

##   Include:

##   A one-line description

##   Args section with parameter details

##   Returns section with return value details

##   Examples section showing usage

##   Do not offer suggestions, refactorings, or code improvements.
##   Only describe the purpose of the code *as written*.

##   """
##   """"""
##   """"""

##
## Add a Google-style docstring for this function:
##
## def add_tiles(cell_map):
##   """Include:

##   A one-line description

##   Args section with parameter details

##   Returns section with return value details

##   Examples section showing usage

##   Do not offer suggestions, refactorings, or code improvements.
##   Only describe the purpose of the code *as written*.
##"""
    ```