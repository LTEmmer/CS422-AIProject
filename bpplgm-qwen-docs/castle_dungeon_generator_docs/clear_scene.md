# clear_scene

    Purpose

    The `clear_scene` function clears all objects in the current Blender scene. It first checks if there is an active object and ensures it's in 'Object' mode, then selects all objects and deletes them without affecting other scenes.
    Parameters

    ```python
def clear_scene(scene=None):
    """
    Clears all objects in the current Blender scene.

    Parameters:
    - scene (bpy.types.Scene): The specific scene to clear. Defaults to the active scene if not specified.
    """
    # Check if a specific scene is provided, otherwise use the active scene
    if scene is None:
        scene = bpy.context.scene

    # Ensure the current mode is 'Object' to allow object selection and deletion
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Select all objects in the scene
    bpy.ops.object.select_all(action='SELECT')

    # Delete selected objects, which will clear the scene
    bpy.ops.object.delete(use_global=False)
```

**Examples:**

To clear the active scene's objects:
```python
import bpy

clear_scene()
```

To clear a specific scene's objects:
```python
my_scene = bpy.data.scenes['My Scene']
clear_scene(scene=my_scene)
```
    Returns

    The `clear_scene` function does not return any value; it returns `None`. The purpose of this function is to clear all objects in the current Blender scene. It first checks if there is an active object and ensures it's in 'Object' mode, then selects all objects and deletes them without affecting other scenes. Special cases include when the scene is empty, or when the user has not selected any object in the scene before calling this function.
    Examples

    ```python
# Basic usage: Clearing a simple scene by removing all entities and resetting camera position
clear_scene()

# Edge case: Trying to clear a scene that doesn't exist (this will do nothing)
clear_scene()  # No action is taken as there's no scene to clear

# Advanced scenario: Clearing a complex scene with multiple layers, including an entity at a specific position
clear_scene()
```
    Docstring

    """```python
def clear_scene():
    """
    Clears all objects from the current scene. The function first checks if an active object exists and switches its mode to 'OBJECT' if necessary. It then selects all objects in the scene and deletes them, ensuring global deletion (i.e., not affecting other scenes).

    Args:
        None

    Returns:
        None

    Examples:
        To clear the current scene, you can call the function as follows:

            >>> clear_scene()
    """
```"""
    ```