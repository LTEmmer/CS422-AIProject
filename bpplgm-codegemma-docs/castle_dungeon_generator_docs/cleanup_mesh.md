# cleanup_mesh

    Purpose

    ```python
    def cleanup_mesh():
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
    ```
    ```python
    def cleanup_mesh():
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
    # remove overlapping ve
    Parameters

    ```
    ```python
    def cleanup_mesh():
    # get all the cubes selected
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.ob
    Returns

    Describe why, if any, the code has been simplified.

    Provide a list of potential changes to the code.

    Provide suggestions for improving the readability of the code.

    Provide suggestions for improving the readability of the code.

    Provide suggestions for improving the readability of the code.
    Examples

    ```python
import numpy as np
import scipy.spatial as spt
from scipy.spatial.qhull import Voronoi
import open3d as o3d
import trimesh

def cleanup_mesh(self, mesh_input: o3d.geometry.TriangleMesh):
    """
    Clean up a Mesh.

    Args:
        mesh_input (o3d.geometry.TriangleMesh): TriangleMesh
            TriangleMesh to be cleaned.

    Returns:
        o3d.geometry.TriangleMesh: Cleaned Mesh

    Raises:
        NotImplementedError: The mesh input is not TriangleMesh.

    """
    if not isinstance(mesh_input, o3d.geometry.TriangleMesh):
        raise NotImplementedError(
            "The mesh input is not TriangleMesh."
        )

    return mesh_input


def create_mesh_from_point_cloud(self, cloud_input: o3d.geometry.PointCloud,
                                 normals_input: o3d.utility.Vector3dVector = None,
                                 voxel_size: float = 0.001,
                                 ransac_ransac_n: int = 3,
                                 ransac_distance_threshold: float = 0.01,
                                 use_normals: bool = True,
                                 use_colors: bool = True,
                                 compute_poisson_mesh: bool = True,
                                 compute_mesh: bool = True,
                                 compute_simplification: bool = True,
                                 compute_simplification_iter: int = 0,
                                 compute_simplification_threshold: float = 0.0,
                                 compute_simplification_type: str = "poisson",
                                 compute_simplification_normalize: bool = True,
                                 compute_simplification_vertex_num: int = 1000,
                                 compute_simplification_vertex_
    Docstring

    """If there is no example code then omit this section.

    :param self: context
    :type self: Blender context
    :param name: name of object selected
    :type name: string
    :param size: size of mesh selected
    :type size: float
    :rtype: None
    """
    ```

    """
    def cleanup_mesh():
    # get all the cubes selected
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    # join all of the separate cube objects into one
    bpy.ops.object.join()
    # jump into edit mode
    bpy.ops.object.mode_set(mode='EDIT')
    # get save the mesh data into a variable
    mesh = bmesh.from_edit_mesh("""
    ```