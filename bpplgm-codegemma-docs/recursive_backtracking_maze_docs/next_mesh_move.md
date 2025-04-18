# next_mesh_move

    Purpose

    Next Mesh Move Function:
        This function takes a direction as an argument and modifies the state of the next_face variable, and updates the x and y coordinates of the next face to be moved, as well as the direction stack.
    Next Face Variable:
        The next_face variable is used to keep track of the next face to be moved.
    X and Y Pos Variables:
        The x_pos and y_pos variables are used to track the current x and y coordinates of the next face to be moved.
    Direction Stack Variable:
        The direction_stack variable is used to keep track of the direction(s) the mesh should be moved in.
    Direction Variable:
        The direction variable is used to store the direction the mesh should be moved in (either 'up', 'down', 'right', or 'left').
```
    def next_mesh_move(direction):
        global next_face
        global y_pos
        global x_pos
        for f in mesh.faces:
            f.select = False

        if direction == 'up':
            for f in mesh.faces:
                if f.normal.y == 1.0 and \
                        round(f.calc_center_median()[1]) == y_pos and \
                        round(f.calc_center_median()[0]) == x_pos - 1:
                    f.select = True
                    next_face = f
                    y_pos += y_move_distance * 2
                    direction_stack.append(direction)
            extrude_up()
            extrude_up()

        if direction == 'right':
            for f in mesh.faces:
                if f.normal.x == 1.0 and \
                        round(f.calc_center_median()[0]) == x_pos and \
                        round(f.calc_center_median()[1]) == y_pos - 1:
                    f.select = True
                    next_face = f
                    x_pos += x_move_distance * 2
                    direction_stack.append(direction)
            extrude_right()
            extrude_right()

        if direction == 'down':
            for f in mesh.faces:
                if f.normal.y == -1.0 and \
                        round(f.calc_center_median()[1]) == y_pos - y_move_distance and \
                        round(f.calc_center_median()[0]) == x_pos - 1:
                    f.select = True
                    next_face
    Parameters

    
    Returns

    Next Face Variable:
        The next_face variable is used to keep track of the next f
    Examples

    ```
    Basic usage
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Edge case
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Advanced scenario (if applicable)
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.

    

    ```
    Basic usage
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Edge case
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Advanced scenario (if applicable)
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```

    Basic usage
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Edge case
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Advanced scenario (if applicable)
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```

    Basic usage
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Edge case
    ```
    ```python
    # Explanation
    code
    ```

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    ```
    Advan
    Docstring

    """You needn"""
    ```