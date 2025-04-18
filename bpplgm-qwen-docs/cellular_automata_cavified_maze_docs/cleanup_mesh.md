# cleanup_mesh

    Purpose

    The function `cleanup_mesh` takes a set of separate cube objects, merges them into one object, enters edit mode to modify the mesh, removes duplicate vertices, and then deletes all faces with normals in the Z direction (interior faces), leaving only the hollow structure behind. The function is used to clean up a mesh by removing unwanted faces such as floors or ceilings, leaving only the exterior structure.
    Parameters

    ```python
def cleanup_mesh(cubes: List[Cube]) -> None:
    """
    Cleans up a set of separate cube objects into one object by merging them,
    removing duplicate vertices, and deleting all faces with normals in the Z direction.

    Args:
        cubes (List[Cube]): A list of Cube objects to be merged into one mesh.
    
    Usage Constraints:
        - All Cube objects must belong to the same scene or have a common parent node.
        - Ensure that the scene has focus before calling this function.
    """
    # Merge all cube objects into one object
    merged_object = merge_cubes(cubes)
    
    # Enter edit mode for the merged object
    enter_edit_mode(merged_object)
    
    # Remove duplicate vertices from the mesh
    remove_duplicate_vertices()
    
    # Delete faces with normals in the Z direction (interior faces)
    delete_interior_faces()
    
    # Exit edit mode to apply changes
    exit_edit_mode()

def merge_cubes(cubes: List[Cube]) -> Object:
    """
    Merges a list of Cube objects into one Object.

    Args:
        cubes (List[Cube]): A list of Cube objects to be merged.

    Returns:
        Object: The merged object containing all the faces from the input cubes.
    """

def enter_edit_mode(object: Object) -> None:
    """
    Enters edit mode for the given Object.

    Args:
        object (Object): The Object whose edit mode needs to be entered.
    """

def remove_duplicate_vertices() -> None:
    """
    Removes duplicate vertices from the current mesh in edit mode.
    """

def delete_interior_faces() -> None:
    """
    Deletes all faces with normals in the Z direction (interior faces) in edit mode,
    leaving only the exterior structure of the object.
    """

def exit_edit_mode() -> None:
    """
    Exits edit mode, applying any changes made to the mesh.
    """
```

### Examples

```python
# Example usage of cleanup_mesh function with a list of Cube objects
cubes = [Cube(position=(0, 0, 0)), Cube(position=(1, 0, 0)), Cube(position=(2, 0, 0))]
cleanup_mesh(cubes)
```

This code snippet demonstrates how to use the `cleanup_mesh` function with a list of separate cube objects, merging them into one mesh and cleaning it up by removing unwanted faces. The examples provided are hypothetical and should be adapted based on the actual implementation in your environment or application.
    Returns

    ```python
def cleanup_mesh(cube_objects):
    """
    Merge a set of separate cube objects into one object and remove specified unwanted faces.

    The function performs the following actions:
    1. Merges all provided cube objects into one mesh.
    2. Enters edit mode to manipulate the mesh.
    3. Removes duplicate vertices to ensure smooth topology.
    4. Deletes all faces with normals in the Z direction (interior faces).
    This results in a hollow structure of only the exterior structure.

    Returns:
    - None

    Special Cases:
    - If no cube objects are provided, the function does nothing.
    """
```

The `cleanup_mesh` function takes a set of separate cube objects and performs several operations to clean up the mesh by merging them into one object, removing duplicate vertices, and deleting interior faces. The function is used to achieve a hollow structure that represents only the exterior of the mesh. No return value is provided as the function modifies the mesh in-place.
    Examples

    ```python
# Basic usage
# This example demonstrates how to clean up a mesh by removing unnecessary vertices and faces.
import bpy

def cleanup_mesh(obj):
    # Select all edges in the mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Remove unused vertices and edges
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent()
    
    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Example object to clean up
obj = bpy.data.objects['Cube']

# Call the cleanup function
cleanup_mesh(obj)

# Output: The 'Cube' object will have its vertices and edges cleaned up.
```

```python
# Edge case
# This example demonstrates how to handle an edge case where the mesh has a self-intersecting face.
import bpy

def cleanup_mesh(obj):
    # Select all faces in the mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Remove intersecting edges and faces
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent()
    
    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Example object with a self-intersecting face
obj = bpy.data.objects['SelfIntersectCube']

# Call the cleanup function
cleanup_mesh(obj)

# Output: The 'SelfIntersectCube' object will have its self-intersecting face removed.
```

```python
# Advanced scenario
# This example demonstrates how to clean up a mesh by removing specific types of vertices and faces.
import bpy

def cleanup_mesh(obj):
    # Select all edges in the mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Remove unused vertices
    bpy.ops.mesh.remove_doubles()
    
    # Keep only triangle faces
    bpy.ops.mesh.select_mode(type="FACE")
    bpy.ops.mesh.select_all(action='DESELECT')
    for face in obj.data.polygons:
        if len(face.vertices) != 3:
            face.select = True
    bpy.ops.mesh.delete(type='EDGE_FACE')

    # Exit edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Example object with mixed polygon faces
obj = bpy.data.objects['MixedPolygons']

# Call the cleanup function
cleanup_mesh(obj)

# Output: The 'MixedPolygons' object will have its edges and non-triangle faces removed.
```
    Docstring

    """```python
def cleanup_mesh():
    """
    This function cleans up a selection of mesh objects by joining them into one,
    removing overlapping vertices, and then removing floor and ceiling faces to create
    a hollow mesh.

    Args:
        None

    Returns:
        None

    Examples:
    >>> bpy.ops.object.select_all(action='TOGGLE')
    >>> bpy.ops.object.select_all(action='TOGGLE')
    >>> cleanup_mesh()
    """"""
    ```