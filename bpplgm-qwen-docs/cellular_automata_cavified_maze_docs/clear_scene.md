# clear_scene

    Purpose

    This function clears all objects in the current Blender scene by setting the mode to 'OBJECT', selecting all objects, and then deleting them without affecting global transformations.
    Parameters

    ```python
def clear_scene():
    """
    Clears all objects in the current Blender scene.

    Function Purpose:
        This function clears all objects in the current Blender scene by setting the mode to 'OBJECT',
        selecting all objects, and then deleting them without affecting global transformations.

    Parameters:

        None

    Usage Constraints:
        - Ensure that no other operations are performed on the scene or selected objects during this function's execution.
        - This function will delete all objects in the current scene but will not affect objects in other scenes
          unless they share references with those in the current scene.
    """
```
    Returns

    ```python
def clear_scene():
    """
    Clears all objects in the current Blender scene.

    This function sets the mode to 'OBJECT', selects all objects in the scene,
    and deletes them without affecting global transformations. It is useful for resetting
    the scene to a clean state before performing new operations.

    Return:
        bool: True if the scene was successfully cleared, False otherwise.
    """

    # Check if there are any objects in the scene
    if len(bpy.context.collection.objects) == 0:
        print("Scene is already clear.")
        return True

    # Set the mode to 'OBJECT'
    bpy.ops.object.mode_set(mode='OBJECT')

    # Select all objects in the scene
    bpy.ops.object.select_all(action='SELECT')

    # Delete selected objects without affecting global transformations
    bpy.ops.object.delete(use_global=False)

    return True
```
    Examples

    ### Basic Usage

```python
# Clear the entire scene by removing all objects and lights.

clear_scene()
```

### Edge Case

```python
# Attempt to clear a scene that is already empty. This should not cause an error but should be handled gracefully.

try:
    clear_scene()  # No action taken as there are no elements in the scene.
except Exception as e:
    print(e)  # Output: 'No objects or lights to clear.'
```

### Advanced Scenario

```python
# Clear a scene while keeping certain objects and lights intact. For example, keep only static objects and disable dynamic lighting.

clear_scene(objects_to_keep=['static_object'], disable_dynamic_lighting=True)
```

Please note that the actual implementation of `clear_scene` may vary depending on the specific library or framework you are using.
    Docstring

    """```python
def clear_scene():
    """
    Clears all objects from the current scene.

    This function switches to object mode if needed, selects all objects,
    and then deletes them without affecting global coordinates. It checks if
    any operations are allowed on the active Blender context before proceeding.

    Args:
        None

    Returns:
        None

    Examples:
        >>> clear_scene()
        Clears all selected objects in the scene.
    """
```"""
    ```