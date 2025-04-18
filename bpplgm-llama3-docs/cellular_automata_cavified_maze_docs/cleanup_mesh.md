# cleanup_mesh

    Purpose

    This function is designed to clean up and prepare a 3D object's mesh by removing overlapping vertices, selecting only interior faces, de-selecting floor and ceiling faces with normals above or below the z-axis, and finally deleting any remaining selected faces. 

**Functionality:**

- Selects all meshes in the scene, joins them together into one
- Switches to edit mode for precise mesh manipulation
- Extracts mesh data from the current object using `bmesh.from_edit_mesh`
- Selects all vertices of the mesh in edit mode
- Removes duplicate and redundant vertices by applying `bpy.ops.mesh.remove_doubles`
- De-selects all faces not part of the interior (floor and ceiling)
- Deletes any still selected face, leaving a hollow shape behind
    Parameters

    ```python
def cleanup_mesh(meshes):
    """
    Clean up and prepare a 3D object's mesh by removing overlapping vertices,
    selecting only interior faces, de-selecting floor and ceiling faces with normals above or below the z-axis,
    and finally deleting any remaining selected faces.

    Parameters:
    meshes (list): A list of Mesh objects in the scene.

    Returns:
        None
    """
```

**Functionality:**

- Selects all meshes in the scene, joins them together into one
- Switches to edit mode for precise mesh manipulation
- Extracts mesh data from the current object using `bmesh.from_edit_mesh`
- Selects all vertices of the mesh in edit mode
- Removes duplicate and redundant vertices by applying `bpy.ops.mesh.remove_doubles`
- De-selects all faces not part of the interior (floor and ceiling)
- Deletes any still selected face, leaving a hollow shape behind
    Returns

    ```python
def cleanup_mesh():
    """
    Cleans up and prepares a 3D object's mesh by removing overlapping vertices,
    selecting only interior faces, de-selecting floor and ceiling faces with normals
    above or below the z-axis, and finally deleting any remaining selected faces.

    Returns:
        list: A list of selected faces after cleaning up and preparing the mesh.
    """
    # Select all meshes in the scene, join them together into one
    selected_meshes = bpy.context.scene.objects.values()

    # Switch to edit mode for precise mesh manipulation
    bpy.ops.object.mode_set(mode='EDIT')

    # Extract mesh data from the current object using bmesh.from_edit_mesh
    bmesh = bpy.data.meshes.new('MeshData')
    mdata = bpy.data.meshes.new('MeshData')
    bm = bpy.data.batched_objects.new()

    for obj in selected_meshes:
        # Select all vertices of the mesh in edit mode
        mdata.vertices.extend(obj.location.iteritems())

        # Remove duplicate and redundant vertices by applying bpy.ops.mesh.remove_doubles
        obj.select_set(type=bpy.types.VERTEX)
        obj.select_by_type(bpy.types.VERTEX, type='SELECTED')

    # De-select all faces not part of the interior (floor and ceiling)
    for face in bm.faces.values():
        if not any(face.start == face.end or face.start == face.begin for start in face):
            face.select_set(type=bpy.types.FACE, use_index=True)

    # Delete any still selected face, leaving a hollow shape behind
    for obj in selected_meshes:
        obj.select_set(type=bpy.types.VERTEX)
        obj.select_by_type(bpy.types.VERTEX, type='SELECTED')
        if not obj.is_linked:
            obj.select_add(type=bpy.types.VERTEX, use_index=True)

    # Return the list of selected faces after cleaning up and preparing the mesh
    return mdata.vertices
```
    Examples

    ```python
def cleanup_mesh(mesh):
    """
    Cleans up a mesh by removing any redundant nodes.

    This function takes a 3D mesh as input and removes any duplicate edges and faces.
    It also removes any self-intersections, which can occur when a face intersects itself.
    Finally, it sets all vertices to their minimum z value if they are outside of the view frustum.

    Args:
        mesh: A 3D mesh object with attributes for points, normals, indices, and texture coordinates

    Returns:
        None
    """

    # Remove redundant edges by sorting them in ascending order
    edges = sorted((edge[0], edge[1]) for edge in mesh.edges)
    
    # Create a set to store unique vertex indices
    vertices = set()
    
    # Iterate over each edge and add it to the set of unique vertices
    for edge in edges:
        if (vertex1 := vertices.add(mesh.vertices[edge[0]]) and 
            vertex2 := vertices.add(mesh.vertices[edge[1]])):
            
            # Set face normals to be the negative of the normal vectors
            mesh.faces[edge] = [-mesh.normals[vertex1], -mesh.normals[vertex2]]
    
    # Remove self-intersections by checking if any face intersects itself
    for i, faces in enumerate(mesh.faces):
        for j in range(i + 1, len(faces)):
            edge1 = (faces[i][0], faces[i][1])
            edge2 = (faces[j][0], faces[j][1])

            # Check if the edges are parallel or skew
            if np.linalg.norm(np.cross(edge1[1] - edge1[0], edge2[1] - edge2[0])) == 0:
                mesh.faces[i] = []
                break

    # Set vertices to their minimum z value if they are outside of the view frustum
    view_frustum = np.array(mesh.vertices[-1]) + np.array(mesh.vertices)[:, -1]
    vertices_min_z = np.minimum(view_frustum, mesh.vertices)
    
    # Set all points in the vertex set to the minimum z value
    for point in vertices:
        mesh.vertices[point] = vertices_min_z
    
```
    Docstring

    """```python
def cleanup_mesh():
    """
    Cleans up a mesh object by selecting all objects, removing doubles, deleting face edges,
    and returning to the object mode.

    A one-line description:
        This function takes a mesh object as input, cleans it up, and returns it in a clean state.
"""

Args section with parameter details:
    - `bpy`: The Python API for Blender, an open-source 3D creation software.
    - `mesh`: The mesh object to be cleaned up.

Returns section with return value details:
    - A string describing the mesh's updated shape and data.

Examples section showing usage:
```python
# Usage example
cleanup_mesh()
print(bpy.context.object.data)
```
```
# Example usage demonstrating cleanup of mesh objects
for obj in bpy.context.scene.objects:
    if obj != bpy.context.object:  # ignore own object
        print(f"Cleaning up {obj.name}")
        cleanup_mesh()
```"""
    ```