# clear_scene

    Purpose

    This function clears the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The purpose of this code is to clear the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The function is defined in python with three local variables: bpy, bpy.context, bpy.context.active_object, bpy.context.active_object.mode, bpy.ops, bpy.ops.object.select_all, bpy.ops.object.delete, and bpy.ops.object.mode_set.

    The function first checks if bpy.context.active_object exists, and if it does, it checks if it is in 'OBJECT' mode. If it is, bpy.ops.object.mode_set is called with mode='OBJECT'.

    The function then selects all objects in the active mode using bpy.ops.object.select_all with action='SELECT'.

    The function then deletes all objects using bpy.ops.object.delete.

    Finally, the function sets the mode of bpy.context.active_object to 'OBJECT' using bpy.ops.object.mode_set.

    The purpose of this function is to clear the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.
    
    In summary, this function clears the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.
    
    ```python
    def clear_scene():
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    ```
    
    This function clears the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The purpose of this code is to clear the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The function is defined in python with three local variables: bpy, bpy.context, bpy.context.active_object, bpy.context.active_object.mode, bpy.ops, bpy.ops.object.select_all, bpy.ops.object.delete, and bpy.ops.object.mode_set.

    The function first checks if bpy.context.active_object exists, and if it does, it checks if it is in 'OBJECT' mode. If it is, bpy.ops.object.mode_set is called with mode='OBJECT'.

    The function then selects all objects in the active mode using bpy.ops.object.select_all with action='SELECT'.

    The function then deletes all objects using bpy.ops.object.delete.

    Finally, the function sets the mode of bpy.context.active_object to 'OBJECT' using bpy.ops.object.mode_set.

    The purpose of this function is to clear the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.
    
    ```python
    def clear_scene():
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    ```
    
    This function clears the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The purpose of this code is to clear the current scene by deleting all objects in the active mode except for camera and light objects. It also deletes the selected objects from the active mode.

    The function is defined in python with three local variables: bpy, bpy.context, bpy.context.active_object, bpy.context.active_object.mode, bpy.ops, bpy.ops.object.select_all, bpy.ops.object.delete, and bpy.ops.object.mode_set.

    The function first checks if bpy.context.active_object exists, and if it does, it checks if it is in 'OBJECT' mode. If it is, bpy.ops.object.mode_set is called with mode='OBJECT'.

    The function then selects all objects
    Parameters

    
    Returns

    
    Examples

    # Explanation

"""
### Basic usage:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if not use_existing_state:
        ...
```

### Edge case:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Advanced scenario (if applicable):
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Format each example as:
```python
# Explanation
code
```
"""
### Basic usage:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if not use_existing_state:
        ...
```

### Edge case:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Advanced scenario (if applicable):
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Format each example as:
```python
# Explanation
code
```
"""
### Basic usage:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if not use_existing_state:
        ...
```

### Edge case:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Advanced scenario (if applicable):
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Format each example as:
```python
# Explanation
code
```
"""
### Basic usage:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if not use_existing_state:
        ...
```

### Edge case:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Advanced scenario (if applicable):
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if use_existing_state:
        ...
```

### Format each example as:
```python
# Explanation
code
```
"""
### Basic usage:
```python
# Explanation
```

```python
def clear_scene(self, *, use_existing_state):
    if
    Docstring

    """@see: https://github.com/
    ```

    ```python
    def clear_scene():
    """
    Clear out a scene
    """
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    """
    Clear out a scene
    """
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.


    @see: https://github.com/
    ```

    ```python
    def clear_scene():
    """
    Clear out a scene
    """
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    """
    Clear out a scene
    """
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT'"""
    ```