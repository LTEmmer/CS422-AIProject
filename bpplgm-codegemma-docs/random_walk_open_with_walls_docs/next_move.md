# next_move

    Purpose

    I wrote this function to be used in a game called "Snake. This game has a snake that starts at 0,0 and has the ability to move up, down, left, or right.

            This function is used to move the snake in a game of Snake. The function takes a string parameter called "direction" and modifies the "x_pos" and "y_pos" variables based on the direction string. The function
            modifies the "visited" list by appending the current x and y coordinates of the snake's head to the list.
    Parameters

    Provide Google-style parameter documentation with:
    - Name
    - Type
    - Description
    - Any usage constraints

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


Function documentation:

    Next Move Function:

    This function determines the next move for a snake game, based on the given direction. It modifies the "x_pos" and "y_pos" variables based on the "direction" parameter, and updates the "visited" list.

    Parameters:

    - 'direction': A string representing the direction to move the snake. It can be 'up', 'down', 'left', or 'right'.

    Modif
    Returns

    Write a Markdown file with a brief description of your code.
    Write a README.md file with an appropriate title and description.
    Include links to your Git repository and a screenshot of your test code.
    When submitting your project, upload your repository via GitHub.
    Use your best judgment to decide when to refactor and/or rewrite your code.
    Write comments for
    Examples

    Please do not offer any suggestions, refactorings, or code improvements.
    """
```
    Docstring

    """```
    def next_move(direction):
    global y_pos
    global x_pos

    if direction == 'up':
        y_pos += Y_MOVE_DISTANCE

    if direction == 'right':
        x_pos += X_MOVE_DISTANCE

    if direction == 'down':
        y_pos -= Y_MOVE_DISTANCE

    if direction == 'left':
        x_pos -= X_MOVE_DISTANCE
    place_tile(x_pos, y_pos)
    visited.append((x_pos, y_pos))

    # Place your code here


    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.

    ```python
    def next_move(direction):
    global y_pos
    global x_pos

    if direction == 'up':
        y_pos += Y_MOVE_DISTANCE

    if direction == 'right':
        x_pos += X_MOVE_DISTANCE

    if direction == 'down':
        y_pos -= Y_MOVE_DISTANCE

    if direction == 'left':
        x_pos -= X_MOVE_DISTANCE
    place_tile(x_pos, y_pos)
    visited.append((x_pos, y_pos))

    # Place your code here


    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as w"""
    ```