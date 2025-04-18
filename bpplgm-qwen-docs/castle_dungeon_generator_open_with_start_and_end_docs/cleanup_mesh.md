# cleanup_mesh

    Purpose

    This function cleans up a mesh by joining all selected cubes into one, removing overlapping vertices and resetting the object's mode.
    Parameters

    ```python
def cleanup_mesh(selection):
    """
    This function cleans up a mesh by joining all selected cubes into one, removing overlapping vertices and resetting the object's mode.

    Parameters:
        selection (list): A list of mesh objects to be cleaned up. These should be instances of the 'Mesh' class in your environment.
    
    Usage Constraints:
        - All elements in the 'selection' list must be valid mesh objects.
        - The function will modify the selected meshes directly, so ensure they are not shared elsewhere in your project.
        - The function assumes that all meshes in the selection have compatible geometries for joining and cleaning up.

    Note: This operation may result in changes to the object's mode, such as converting it from 'Edit' to 'Object', and back again.
    """
```

### Examples:
```python
# Example usage
selection = [cube1, cube2]
cleanup_mesh(selection)
```

In this example, `cube1` and `cube2` are mesh objects that need to be cleaned up. The function will join them into one object, remove any overlapping vertices, and reset the mode of the resulting object from 'Edit' to 'Object'.
    Returns

    This function cleans up a mesh by joining all selected cubes into one. It removes overlapping vertices and resets the object's mode.

### Return Type:
- `None`

### Description:
The function performs the following operations on the currently active Blender scene:

1. **Joining Selected Cubes**: If multiple cubes are selected, it combines them into a single mesh.
2. **Removing Overlapping Vertices**: It merges any overlapping vertices to simplify the geometry.
3. **Resetting Object Mode**: It switches back to object mode for further manipulation.

### Special Cases:
- The function does not handle multi-object selections directly; it requires all selected objects to be cubes.
- If no cubes are selected, the function will return immediately without executing any operations.
- Overlapping vertices and faces can cause issues in subsequent operations, so this step is crucial for ensuring clean mesh data.
    Examples

    ```python
# Basic usage: Cleaning up a mesh by removing non-manifold edges and faces

import pymeshlab as ml

def cleanup_mesh(mesh):
    """
    Clean up a given mesh by removing non-manifold edges and faces.

    Args:
        mesh (Mesh): The input Mesh object to be cleaned up.

    Returns:
        Mesh: A cleaned-up version of the input mesh.
    """
    ms = ml.MeshProcessing()
    # Remove non-manifold edges
    ms.remove_non_manifold_edges(mesh)
    # Remove non-manifold faces
    ms.remove_non_manifold_faces(mesh)
    return mesh

# Example usage
mesh = ml.Mesh.from_file('input_mesh.obj')
cleaned_mesh = cleanup_mesh(mesh)
cleaned_mesh.save('output_mesh_cleaned.obj')

# Explanation: This function takes a Mesh object and removes all non-manifold edges and faces,
# returning a new clean version of the mesh. It's useful for preparing meshes for further processing
# or visualization where such features can cause issues.

# Edge case: Using a mesh with no non-manifold edges or faces

def cleanup_mesh_no_edges(mesh):
    """
    Clean up a given mesh by removing non-manifold edges and faces, but only if they exist.

    Args:
        mesh (Mesh): The input Mesh object to be cleaned up.

    Returns:
        Mesh: A possibly cleaned-up version of the input mesh, or the original mesh if no cleanup is needed.
    """
    ms = ml.MeshProcessing()
    # Check for non-manifold edges
    if mesh.has_non_manifold_edges():
        ms.remove_non_manifold_edges(mesh)
    # Check for non-manifold faces
    if mesh.has_non_manifold_faces():
        ms.remove_non_manifold_faces(mesh)
    return mesh

# Example usage
mesh = ml.Mesh.from_file('input_mesh_no_edges.obj')
cleaned_mesh = cleanup_mesh_no_edges(mesh)
if cleaned_mesh != mesh:
    cleaned_mesh.save('output_mesh_cleaned_no_edges.obj')

# Explanation: This function is similar to the basic version but checks if there are any non-manifold edges or faces
# before attempting to remove them. If no cleanup is needed, it returns the original mesh.

# Advanced scenario: Handling meshes with complex topology

def cleanup_complex_mesh(mesh):
    """
    Clean up a given mesh by removing non-manifold edges and faces, and also repairing some topological issues.

    Args:
        mesh (Mesh): The input Mesh object to be cleaned up.

    Returns:
        Mesh: A cleaned-up version of the input mesh, with additional topology repairs.
    """
    ms = ml.MeshProcessing()
    # Remove non-manifold edges
    ms.remove_non_manifold_edges(mesh)
    # Remove non-manifold faces
    ms.remove_non_manifold_faces(mesh)
    # Repair any remaining topological issues (e.g., self-intersections)
    ms.repair_topology(mesh)
    return mesh

# Example usage
mesh = ml.Mesh.from_file('input_complex_mesh.obj')
cleaned_mesh = cleanup_complex_mesh(mesh)
cleaned_mesh.save('output_mesh_cleaned_and_repaired.obj')

# Explanation: This function extends the basic cleanup process by adding the capability to repair complex topological issues
# in the mesh, which might be necessary after removing non-manifold edges and faces. It's useful for preparing meshes that
# require a more robust topological structure for further processing or analysis.
```
    Docstring

    """```python
def cleanup_mesh():
    """
    Cleans up a selected mesh object by joining all separate cubes into one,
    removing duplicate vertices, and de-selecting everything in edit mode.

    Returns:
        None

    Examples:
        >>> bpy.ops.object.select_all(action='TOGGLE')
        >>> bpy.ops.object.select_all(action='TOGGLE')
        >>> bpy.ops.object.join()
        >>> bpy.ops.object.mode_set(mode='EDIT')
        >>> mesh = bmesh.from_edit_mesh(bpy.context.object.data)
        >>> bpy.ops.mesh.select_all(action='SELECT')
        >>> bpy.ops.mesh.remove_doubles()
        >>> bpy.ops.mesh.select_all(action='DESELECT')
        >>> bpy.ops.object.mode_set(mode='OBJECT')
    """
```"""
    ```