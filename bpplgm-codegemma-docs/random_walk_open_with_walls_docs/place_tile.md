# place_tile

    Purpose

    This function is a simple addition of a plane to a given location. The location is determined by the x and y parameters. The function is called with x=1 and y=2. The function adds a plane to the location (1, 2, -1).
    Parameters

    Only offer suggestions, refactorings, or code improvements if you feel it helps.
    If you're unable to make any suggestions or refactorings, you'll receive a 20% discount on your test score.
    If you're unable to make any suggestions or refactorings at all, you'll receive a 10% discount on your test score.
    Please contact us with any questions or concerns.

    If you're unable to make any suggestions, refactorings, or code improvements, you'll receive a 20% discount on your test score.
    If you're unable to make any suggestions or refactorings, you'll receive a 10% discount on your test score.
    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.

    Please contact us with any questions or concerns.
    Returns

    Do not include suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not include suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or code improvements.
    Instead, just describe the code's purpose.
    Do not offer suggestions, refactorings, or c
    Examples

    ## Example 1:
    ```python
    >>> from PIL import Image
    >>> from place_tile import place_tile

    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (10, 10))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 1 tiles.

    >>> assert img.size == (img.width * 10, img.height * 10)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```

    ## Example 2:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```

    ## Example 3:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```

    ## Example 4:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```
    ## Example 5:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```

    ## Example 6:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```
    ## Example 7:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```
    ## Example 8:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated {len(tiles)} tiles.")
    Generated 100 tiles.

    >>> assert img.size == (img.width * 100, img.height * 100)
    >>> for tile in tiles:
    ...     assert tile.size == (img.width, img.height)
    ```
    ## Example 9:
    ```python
    >>> img = Image.open("sample_image.jpg")
    >>> tiles = place_tile(img, (100, 100))

    >>> print(f"Generated
    Docstring

    """Include tests if you can.
    ```

    """

    def place_tile(x, y):
        """ Place a tile

        Parameters
        ----------
        x : int
            X coordinate
        y : int
            Y coordinate

        Returns
        -------
        None
        """
        bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, location=(x, y, -1))
        # Add a tile
        tile = bpy.context.object
        tile.name = 'Tile'

    def place_tiles("""
    ```