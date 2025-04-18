# clear_scene

    Purpose

    The function `clear_scene()` is designed to delete all objects in the current Blender scene. It first checks if there is an active object, and if so, ensures it's in 'OBJECT' mode. Then, it selects all objects in the scene and deletes them, ignoring their global transformation settings.
    Parameters

    ```python
def clear_scene():
    """
    Clears all objects in the current Blender scene.

    This function will delete all objects present in the active Blender scene. It first checks if there is an active object,
    and if so, ensures it's in 'OBJECT' mode. Then, it selects all objects in the scene and deletes them, ignoring their
    global transformation settings.

    Example usage:
    clear_scene()
    """
```
    Returns

    ```python
def clear_scene():
    """Clear all objects from the current Blender scene.

    Returns:
        None: This function does not return any value. It modifies the Blender scene in-place.

    Description:
    The function `clear_scene()` is designed to delete all objects in the current Blender scene. 
    It first checks if there is an active object, and if so, ensures it's in 'OBJECT' mode. 
    Then, it selects all objects in the scene and deletes them, ignoring their global transformation settings.

    Special cases:
    - If no objects are present in the scene, the function does not perform any actions.
    - The function uses Blender's built-in operations to clear the scene without affecting other parts of the user interface or data structure.
    """
```
    Examples

    ```python
# Basic usage: Clears the current scene to make it empty for new elements.
def clear_scene():
    pass

# Explanation:
# This function empties the current scene by removing all existing objects, lights, and textures.
# It is useful when you want to start fresh with a clean environment without having any previous elements.
```

```python
# Edge case: Attempting to clear an empty scene does not change anything.
def clear_scene():
    pass

# Explanation:
# If the current scene is already empty (i.e., it contains no objects, lights, or textures),
# calling `clear_scene` will not have any effect on the scene. The function will simply do nothing
# because there are no elements to remove.
```

```python
# Advanced scenario: Clearing a complex scene with multiple layers and interactions.
def clear_scene():
    pass

# Explanation:
# In an advanced scenario, `clear_scene` would handle more complex operations such as clearing all
# layers of a 3D model, removing custom materials, and resetting physics properties. This could be
# useful for applications like animations or when you need to start from scratch with a completely clean environment.
```
    Docstring

    """```python
def clear_scene():
    """Clears all objects in the current scene."""
    
    # If there is an active object and it is not in OBJECT mode
    if bpy.context.active_object:
        if bpy.context.active_object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')  # Switch to OBJECT mode

    # Select all objects in the scene
    bpy.ops.object.select_all(action='SELECT')

    # Delete all selected objects without affecting other scenes (use_global=False)
    bpy.ops.object.delete(use_global=False)

# Examples
# Clear all objects in the current scene by selecting them and then deleting them.
clear_scene()
```"""
    ```