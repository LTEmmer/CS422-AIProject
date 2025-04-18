# cleanup_mesh

    Purpose

    The function `cleanup_mesh` performs several operations on a Blender object:

1. **Selects and joins all cube objects**: It toggles the selection to deselect all, then selects all again to join them into one object.
2. **Enters edit mode**: The function switches to the 'EDIT' mode to manipulate the mesh data directly.
3. **Removes doubles**: It removes vertices that are within a certain tolerance of each other, which helps clean up the mesh and reduce duplication.
4. **De-selects everything in edit mode**: After cleaning up the mesh, it de-selects all objects to reset the scene for further operations.
5. **Selects interior faces**: The function selects only the "interior" faces of the mesh, excluding those on the top and bottom (where `f.normal[2]` is either 1.0 or -1.0).
6. **Deletes selected faces**: It removes the selected faces, leaving a hollow mesh behind.
7. **Exits edit mode**: Finally, it returns to the 'OBJECT' mode to exit editing.

This function is primarily used to clean up and prepare a mesh for further modeling tasks by removing unnecessary vertices, ensuring only interior faces are left, and creating a hollow mesh with no top or bottom surfaces.
    Parameters

    ```python
def cleanup_mesh():
    """
    Function `cleanup_mesh` performs several operations on a Blender object:

1. **Selects and joins all cube objects**: It toggles the selection to deselect all, then selects all again to join them into one object.
2. **Enters edit mode**: The function switches to the 'EDIT' mode to manipulate the mesh data directly.
3. **Removes doubles**: It removes vertices that are within a certain tolerance of each other, which helps clean up the mesh and reduce duplication.
4. **De-selects everything in edit mode**: After cleaning up the mesh, it de-selects all objects to reset the scene for further operations.
5. **Selects interior faces**: The function selects only the "interior" faces of the mesh, excluding those on the top and bottom (where `f.normal[2]` is either 1.0 or -1.0).
6. **Deletes selected faces**: It removes the selected faces, leaving a hollow mesh behind.
7. **Exits edit mode**: Finally, it returns to the 'OBJECT' mode to exit editing.

This function is primarily used to clean up and prepare a mesh for further modeling tasks by removing unnecessary vertices, ensuring only interior faces are left, and creating a hollow mesh with no top or bottom surfaces.
    """

# No parameters to document
```

This documentation provides a clear explanation of the purpose and functionality of the `cleanup_mesh` function as described in the comments within the code.
    Returns

    ```python
def cleanup_mesh(mesh_object):
    """
    This function cleans up a Blender mesh object by performing several operations:
    
    1. Selects and joins all cube objects to combine them into one.
    2. Enters edit mode to manipulate the mesh data directly.
    3. Removes vertices that are within a certain tolerance of each other to clean up the mesh.
    4. De-selects everything in edit mode after cleaning up.
    5. Selects only the interior faces of the mesh, excluding top and bottom faces where `f.normal[2]` is either 1.0 or -1.0.
    6. Deletes selected faces to create a hollow mesh with no top or bottom surfaces.
    7. Exits edit mode.

    This function is primarily used to clean up and prepare a mesh for further modeling tasks by removing unnecessary vertices,
    ensuring only interior faces are left, and creating a hollow mesh with no top or bottom surfaces.
    
    Parameters:
        mesh_object (bpy.types.Object): The Blender object representing the mesh to be cleaned up.

    Returns:
        None: This function does not return any value. It modifies the mesh in-place.
    """
```

**Special Cases:**
- If the input `mesh_object` is not a valid Blender object, the function will raise an error when trying to access its properties or methods.
- The function assumes that all cube objects are selected before joining them, which might not always be the case if other objects were selected initially.
    Examples

    ```python
# Basic usage: Cleans up a mesh by removing redundant vertices and faces.
import bpy

mesh = bpy.data.meshes['Cube']
cleanup_mesh(mesh)

# Explanation: This function iterates over the mesh, checking for duplicate vertices and faces.
# It removes these duplicates to optimize the mesh data.

# Edge case: Cleaning an empty mesh does not change it.
empty_mesh = bpy.data.meshes.new('EmptyMesh')
cleanup_mesh(empty_mesh)
# Explanation: If the mesh has no vertices or faces, calling cleanup_mesh will have no effect on the mesh.

# Advanced scenario: Cleans up a complex mesh with multiple sub-surfaces and UV maps.
complex_mesh = bpy.data.objects['ComplexMesh']
for part in complex_mesh.children:
    if part.type == 'MESH':
        cleanup_mesh(part.data)
cleanup_mesh(complex_mesh.data)
# Explanation: This advanced usage demonstrates how to apply cleanup_mesh to each sub-mesh within an object that consists of multiple mesh parts.
```
    Docstring

    """```python
def cleanup_mesh():
    """
    Cleans up a mesh by joining its separate cube objects into one, removing doubles,
    and then selecting and deleting interior faces, leaving a hollow mesh behind.

    Args:

        No parameters are required for this function.

    Returns:

        The cleaned-up mesh object.

    Examples:

    ```python
    import bpy

    # Select the cubes you want to clean up
    bpy.ops.object.select_all(action='TOGGLE')

    # Run the cleanup_mesh function
    cleanup_mesh()

    # Deselect all objects in case they were not deselected automatically
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    ```

    Note: This function assumes that there are at least two cubes selected and that they can be joined into one. The "interior faces" selection is based on the Z-axis normal, so it may not work perfectly for all meshes.
    ```"""
    ```