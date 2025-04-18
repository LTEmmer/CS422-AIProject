# cleanup_mesh

    Purpose

    The function `cleanup_mesh()` takes a selection of cube objects in Blender, joins them into one mesh, and then cleans it up by removing overlapping vertices, selecting only the interior faces, removing floor and ceiling faces based on normal vectors, and deleting all remaining selected faces to create a hollowed-out version of the original mesh.
    Parameters

    ```python
def cleanup_mesh(cubes):
    """
    Cleans up a selection of cube objects in Blender.

    Args:
        cubes (list): A list of cube objects selected in Blender. These objects will be joined into one mesh and cleaned up.

    Returns:
        None

    Notes:
        - The function joins all the selected cubes into one mesh.
        - It removes overlapping vertices, selecting only the interior faces.
        - It removes floor and ceiling faces based on their normal vectors.
        - It deletes all remaining selected faces to create a hollowed-out version of the original mesh.
    """
    # Example usage:
    # import bpy
    # cubes = [bpy.data.objects['Cube.01'], bpy.data.objects['Cube.02']]
    # cleanup_mesh(cubes)
```

This function takes a list of cube objects, joins them into one mesh, and then cleans up the mesh by removing overlapping vertices, selecting only the interior faces, removing floor and ceiling faces based on normal vectors, and deleting all remaining selected faces to create a hollowed-out version.
    Returns

    The `cleanup_mesh()` function does not explicitly return a value. It performs several operations in place on the selection of cube objects:

- Joins them into one mesh using `bpy.ops.object.join()`.
- Cleans up the mesh by removing overlapping vertices, selecting only the interior faces.
- Removes floor and ceiling faces based on normal vectors.
- Deletes all remaining selected faces to create a hollowed-out version of the original mesh.

Special cases:
- If there are no cube objects in the selection before joining, the function will not perform any cleanup as it has nothing to work with.
    Examples

    ```python
# Basic usage
def cleanup_mesh(mesh):
    """
    Cleans up a given mesh by removing any unnecessary vertices and faces.

    :param mesh: The mesh to be cleaned up.
    :return: The cleaned-up mesh.
    """
    # Remove unused vertices and faces from the mesh
    mesh.remove_unused_geometry()
    return mesh

# Example of basic usage
from bmesh import new, ops

b = new()
ops.create_cube(b)
mesh = b.to_mesh()  # Convert BMesh to a Mesh object

cleaned_mesh = cleanup_mesh(mesh)

# Edge case
def cleanup_mesh_with_existing_edges(mesh):
    """
    Cleans up a given mesh by removing any vertices and faces but ensures that edges remain connected.
    
    :param mesh: The mesh to be cleaned up.
    :return: The cleaned-up mesh.
    """
    # Identify and keep only the edge vertices, then remove all other vertices and faces
    keep_edges = [v for v in mesh.vertices if any(e.index in mesh.edges for e in v.link_edges)]
    keep_vertices = [v for v in mesh.vertices if v.index in keep_edges]
    keep_faces = []
    
    for f in mesh.faces:
        if all(v.index in keep_vertices for v in f.verts):
            keep_faces.append(f)
    
    # Create a new Mesh object with only the kept vertices and faces
    cleaned_mesh = bmesh.new()
    ops.delete(cleaned_mesh, verts=mesh.vertices - set(keep_vertices), faces=mesh.faces - set(keep_faces), use_dissolve=True)
    for v in keep_vertices:
        cleaned_mesh.verts.new(v.co)
    for f in keep_faces:
        cleaned_mesh.faces.new([cleaned_mesh.verts[i] for i in f.verts])
    
    return cleaned_mesh

# Example of edge case
b = new()
ops.create_cube(b)
mesh = b.to_mesh()

keep_edges = cleanup_mesh_with_existing_edges(mesh)

# Advanced scenario (if applicable)
def cleanup_mesh_with_normals(mesh):
    """
    Cleans up a given mesh by removing any vertices and faces but ensures that vertex normals are preserved.
    
    :param mesh: The mesh to be cleaned up.
    :return: The cleaned-up mesh.
    """
    # Calculate the average normal for each face
    normal_dict = {}
    for f in mesh.faces:
        avg_normal = sum(v.normal for v in f.verts) / len(f.verts)
        if avg_normal not in normal_dict:
            normal_dict[avg_normal] = [f]
        else:
            normal_dict[avg_normal].append(f)
    
    # Keep only the face with the highest average normal
    keep_faces = []
    max_avg_normal = 0.0
    for faces in normal_dict.values():
        if len(faces) > 1:
            max_avg_normal = max(max_avg_normal, max([f.normal.dot(v.normal) for f in faces for v in f.verts]))
    
    for f in mesh.faces:
        if f.normal.dot(max_avg_normal) == max_avg_normal and f not in keep_faces:
            keep_faces.append(f)
    
    # Create a new Mesh object with only the kept faces
    cleaned_mesh = bmesh.new()
    ops.delete(cleaned_mesh, verts=mesh.vertices, faces=mesh.faces - set(keep_faces), use_dissolve=True)
    for f in keep_faces:
        cleaned_mesh.faces.new([f.verts[i] for i in f.verts])
    
    return cleaned_mesh

# Example of advanced scenario
b = new()
ops.create_cube(b)
mesh = b.to_mesh()

max_avg_normal_mesh = cleanup_mesh_with_normals(mesh)
```
    Docstring

    """```python
def cleanup_mesh():
    # Get all the cubes selected
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')

    # Join all of the separate cube objects into one
    bpy.ops.object.join()

    # Jump into edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Get the mesh data into a variable
    mesh = bmesh.from_edit_mesh(bpy.context.object.data)

    # Select the entire mesh
    bpy.ops.mesh.select_all(action='SELECT')

    # Remove overlapping verts
    bpy.ops.mesh.remove_doubles()

    # De-select everything in edit mode
    bpy.ops.mesh.select_all(action='DESELECT')

    # Select the "interior faces"
    bpy.ops.mesh.select_interior_faces()

    # Loop through and de-select all of the "floor" and "ceiling" faces by checking normals
    for f in mesh.faces:
        if f.normal[2] == 1.0 or f.normal[2] == -1.0:
            f.select = False

    # Delete all still selected faces, leaving a hollow mesh behind
    bpy.ops.mesh.delete(type='FACE')

    # Get back out of edit mode
    bpy.ops.object.mode_set(mode='OBJECT')

# A one-line description
"""
Cleanup the current mesh by joining separate cubes, removing doubles, de-selecting "floor" and "ceiling" faces, and leaving a hollow mesh.
"""

# Args section with parameter details
# There are no arguments for this function.

# Returns section with return value details
# This function does not return any values.

# Examples section showing usage
"""
Usage example:
1. Select all cubes in your scene.
2. Run `cleanup_mesh()` in the console or a script editor.
3. The selected cube objects will be joined into one, and "floor" and "ceiling" faces will be removed to create a hollow mesh.
"""
```"""
    ```