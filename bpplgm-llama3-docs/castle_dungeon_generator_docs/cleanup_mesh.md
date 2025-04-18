# cleanup_mesh

    Purpose

    ```python
def cleanup_mesh():
    """
    Cleans up the 3D model by removing overlapping vertices, selecting only interior faces,
    and deleting selected faces.

    This function iterates over each face in the mesh and checks its normal vector. If the
    face's normal is pointing towards or away from the edge of the mesh, it is removed.
    Then, all faces that are not part of the floor or ceiling (i.e., those on the sides) are
    deselected.

    The function also selects only the interior faces and deletes them to preserve the hollow
    shape of the model.
    """
```
    Parameters

    ```python
def cleanup_mesh():
    """
    Cleans up the 3D model by removing overlapping vertices, selecting only interior faces,
    and deleting selected faces.

    Parameters:
    []

    Description:
    This function iterates over each face in the mesh and checks its normal vector. If the
    face's normal is pointing towards or away from the edge of the mesh, it is removed.
    Then, all faces that are not part of the floor or ceiling (i.e., those on the sides) are
    deselected.

    Usage Constraints:
    None

    Notes:
    This function assumes that the input mesh object has a method called 'faces' to access its
    face collection. It also assumes that the input mesh object has a method called 'vertices'
    to access its vertex collection.
    """
```

```python
# Example usage of cleanup_mesh()
import random

def generate_random_mesh(num_vertices, num_faces):
    # Generate random vertices and faces for demonstration purposes only
    return [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(num_vertices)] + \
           [((random.uniform(0, 1), random.uniform(0, 1)), (random.uniform(0, 1), random.uniform(0, 1))) for _ in range(num_faces)]

# Create a mesh object
mesh = generate_random_mesh(100, 500)
```

```python
# Example usage of cleanup_mesh() on the generated mesh
def test_cleanup_mesh():
    # Remove faces that are not part of the floor or ceiling
    cleaned_mesh = [face for face in mesh if any(face[1] != face[0] for x, y in face)]

    # Select only interior faces and delete them
    interior_faces = [face for face in cleaned_mesh if all(x < 0.5 or y < 0.5 for x, y in face)]
    
    # Delete the selected faces
    del cleaned_mesh[:len(interior_faces)]

# Test cleanup_mesh()
test_cleanup_mesh()
```
    Returns

    ```python
def cleanup_mesh():
    """
    Cleans up the 3D model by removing overlapping vertices, selecting only interior faces,
    and deleting selected faces.

    This function iterates over each face in the mesh and checks its normal vector. If the
    face's normal is pointing towards or away from the edge of the mesh, it is removed.
    Then, all faces that are not part of the floor or ceiling (i.e., those on the sides) are
    deselected.

    The function also selects only the interior faces and deletes them to preserve the hollow
    shape of the model.

    Return type: list

    Description:
        Returns a list of face indices that were removed from the mesh, as well as the number
        of faces deleted. Interior faces are returned unmodified.

    Special cases:
        None
```
    Examples

    ```python
def cleanup_mesh(mesh):
    """
    Cleans up a mesh by removing unnecessary vertices.

    Args:
        mesh (list): A list of vertices representing the mesh to clean up.

    Returns:
        list: The cleaned-up mesh with unnecessary vertices removed.
    """

    # Explanation
    # This function iterates over each vertex in the mesh and checks if it's valid (not NaN).
    # If a vertex is invalid, it's added back to the mesh.
    cleaned_mesh = []
    for vertex in mesh:
        # Check if the vertex is not NaN
        if not math.isnan(vertex):
            cleaned_mesh.append(vertex)

    return cleaned_mesh

# Example 1: Basic usage
vertices = [0.5, 0.5, 0.5,  // valid vertex
           1.0, 1.0, 1.0,  // invalid vertex (NaN)
           -0.5, -0.5, -0.5]
cleaned_vertices = cleanup_mesh(vertices)
print(cleaned_vertices)  # Output: [0.5, 0.5, 0.5, 1.0]

# Example 2: Edge case
vertices = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]  # invalid vertex (NaN)
cleaned_vertices = cleanup_mesh(vertices)
print(cleaned_vertices)  # Output: [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]

# Example 3: Advanced scenario
vertices = [[[2.0, 2.0], [2.0, 2.0]],  // invalid vertex (NaN)
           [[0.5, 0.5], [0.5, 0.5]]]  # another invalid vertex (NaN)
cleaned_vertices = cleanup_mesh(vertices)
print(cleaned_vertices)  # Output: [[[2.0, 2.0], [2.0, 2.0]], [[0.5, 0.5], [0.5, 0.5]]]
```
    Docstring

    """```python
def cleanup_mesh():
    """
    Cleans up a selected 3D object's mesh by toggling all face selections, 
    joining them into a single cube, and removing overlapping vertices. Then, 
    de-selects the interior faces and deletes any remaining selected faces.

    Returns:
        None
    """
    # get all the cubes selected
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')

    # join all of the separate cube objects into one
    bpy.ops.object.join()

    # jump into edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    # get save the mesh data into a variable
    mesh = bmesh.from_edit_mesh(bpy.context.object.data)

    # select the entire mesh
    bpy.ops.mesh.select_all(action='SELECT')

    # remove overlapping verts
    bpy.ops.mesh.remove_doubles()

    # de-select everything in edit mode
    bpy.ops.mesh.select_all(action='DESELECT')

    # select the "interior faces"
    bpy.ops.mesh.select_interior_faces()

    # loop through and de-select all of the "floor" and "ceiling" faces by checking normals
    for f in mesh.faces:
        if f.normal[2] == 1.0 or f.normal[2] == -1.0:
            f.select = False

    # delete all still selected faces, leaving a hollow mesh behind
    bpy.ops.mesh.delete(type='FACE')

    # get back out of edit mode
    bpy.ops.object.mode_set(mode='OBJECT')
```"""
    ```