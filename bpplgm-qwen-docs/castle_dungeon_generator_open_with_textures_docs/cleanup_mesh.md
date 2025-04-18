# cleanup_mesh

    Purpose

    The function `cleanup_mesh()` performs a series of operations on Blender objects to clean up and prepare them for further processing. It selects all cubes, joins them into one mesh, enters edit mode, removes doubles to reduce vertex count, de-selects the mesh, exits edit mode, and returns the cleaned-up mesh data.
    Parameters

    ```python
def cleanup_mesh():
    """
    Performs a series of operations on Blender objects to clean up and prepare them for further processing.

    This function selects all cubes, joins them into one mesh, enters edit mode, removes doubles to reduce vertex count,
    de-selects the mesh, exits edit mode, and returns the cleaned-up mesh data.
    
    Returns:
        bpy.types.Mesh: The cleaned-up mesh data from Blender.
    """
    # Select all cubes
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and obj.name.startswith('Cube'):
            obj.select_set(True)
        else:
            obj.select_set(False)

    # Join selected objects into one mesh
    bpy.ops.object.join()

    # Enter edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Remove doubles to reduce vertex count
    bpy.ops.mesh.remove_doubles()

    # De-select the mesh
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Return the cleaned-up mesh data
    return bpy.context.active_object.data
```
    Returns

    ```python
def cleanup_mesh():
    """
    This function performs a series of operations on Blender objects to clean up and prepare them for further processing. It selects all cubes,
    joins them into one mesh, enters edit mode, removes doubles to reduce vertex count, de-selects the mesh, exits edit mode, and returns the cleaned-up mesh data.

    Returns:
        - bpy.types.Mesh: The cleaned-up mesh data of the joined objects.
    """
    # Select all cubes in the scene
    bpy.ops.object.select_by_type(type='MESH')
    
    # Join the selected cubes into one mesh
    bpy.ops.object.join()
    
    # Enter edit mode for the newly created mesh object
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Remove doubles to reduce vertex count
    bpy.ops.mesh.remove_doubles(use_unselected=False)
    
    # De-select the mesh object
    bpy.ops.object.select_all(action='DESELECT')
    
    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return bpy.context.active_object.data

# Example usage:
# cleaned_mesh = cleanup_mesh()
# print(cleaned_mesh.name)  # Output: Cube (assuming the joined mesh is named "Cube")
```

**Special Cases**:
- If there are no cubes selected, the function will return `None` since there's nothing to join.
- The function assumes that all objects in the selection are cubes and does not handle other types of meshes or objects.
    Examples

    ```python
# Basic usage: Cleans up a mesh by removing unused vertices and edges.
def cleanup_mesh(mesh):
    """
    Cleanup a mesh by removing unused vertices and edges.

    Args:
        mesh (Mesh): The mesh to clean up.

    Returns:
        Mesh: The cleaned-up mesh.
    """
    # Remove unused vertices
    mesh.remove_unused_vertices()

    # Clean up edges by removing any that are not connected to at least one vertex
    mesh.remove_dead_edges()

    return mesh

# Example 1 - Basic usage
mesh = create_mesh(...)  # Assume this function creates a mesh
cleaned_mesh = cleanup_mesh(mesh)
print("Basic Usage:", cleaned_mesh)

# Edge case: Mesh with only one vertex, which should be removed.
edge_case_mesh = create_mesh(..., vertices=[(0, 0, 0)])  # Create a mesh with one vertex
edge_case_cleaned_mesh = cleanup_mesh(edge_case_mesh)
print("Edge Case:", edge_case_cleaned_mesh)

# Advanced scenario: Mesh with complex topology that may need manual cleanup.
advanced_mesh = create_mesh(...)  # Assume this function creates a more complex mesh
advanced_cleaned_mesh = cleanup_mesh(advanced_mesh)
print("Advanced Scenario:", advanced_cleaned_mesh)
```
    Docstring

    """```python
def cleanup_mesh():
    """
    Cleans up a selected mesh by joining all separate cubes into one object,
    removing overlapping vertices, and returning it to an object mode.

    Args:

    Returns:
        The cleaned-up mesh object after processing.
    Examples:

    # Select multiple cube objects
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')

    # Join all selected cubes into one object
    bpy.ops.object.join()

    # Cleanup the joined mesh by removing doubles
    cleaned_mesh = cleanup_mesh()
    """

    # Get all the cubes selected
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')

    # Join all of the separate cube objects into one
    bpy.ops.object.join()

    # Jump into edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Get save the mesh data into a variable
    mesh = bmesh.from_edit_mesh(bpy.context.object.data)

    # Select the entire mesh
    bpy.ops.mesh.select_all(action='SELECT')

    # Remove overlapping verts
    bpy.ops.mesh.remove_doubles()

    # De-select everything in edit mode
    bpy.ops.mesh.select_all(action='DESELECT')

    # Get back out of edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

    return cleaned_mesh
```"""
    ```