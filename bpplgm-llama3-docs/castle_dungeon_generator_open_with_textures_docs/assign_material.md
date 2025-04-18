# assign_material

    Purpose

    This function assigns a material to an object (ob) in the context of Blender using its built-in data management system. Specifically, it adds a newly loaded material with the specified name from the `bpy.data.materials` dictionary to the object's materials list.

```python
import bpy
```

```python
def assign_material(ob, mat_name):
    ob.data.materials.append(bpy.data.materials.get(mat_name))
```
You can use it as shown in this example:
```python
# Create a new material with name 'Mat1'
mat = bpy.data.materials.new('Mat1')
bpy.context.object.data.materials.append(mat)
```
    Parameters

    ```python
def assign_material(ob: bpy.context.object, mat_name: str) -> None:
    """
    Assigns a material to an object (ob) in the context of Blender using its built-in data management system.

    Parameters
    ----------
    ob : bpy.context.object
        The object to which the material is to be assigned.
    mat_name : str
        The name of the new material to be added to the object's materials list.

    Usage Constraints
    --------------
    - The object must have a 'data' attribute that references its data manager.
    - The `bpy.data.materials` dictionary must contain all loaded materials in the scene.

    Returns
    -------
    None

    Examples
    --------
    Create a new material with name 'Mat1':
    ```python
mat = bpy.data.materials.new('Mat1')
bpy.context.object.data.materials.append(mat)
```
    Assign a material to an object:
    ```python
# Create a new object (e.g., mesh) and add a material
ob = bpy.context.object
mat_name = 'Mat2'
assign_material(ob, mat_name)
```
    Returns

    ```python
def assign_material(ob: bpy.context.object, mat_name: str) -> list[bpy.data.materials]:
    """
    Assign a material to an object in the context of Blender using its built-in data management system.

    Args:
        ob (bpy.context.object): The object to which the material will be assigned.
        mat_name (str): The name of the new material to be added.

    Returns:
        list[bpy.data.materials]: A list containing all materials on the object after adding the newly loaded material.

    Description:
        This function adds a newly loaded material with the specified name from the bpy.data.materials dictionary to an object's materials list.
    
    Special cases:
        - If the mat_name already exists in the object's materials list, it is not modified.
        - If the mat_name does not exist in the bpy.data.materials dictionary, it will be added.

    Examples:
        >>> # Create a new material with name 'Mat1'
        >>> mat = bpy.data.materials.new('Mat1')
        >>> bpy.context.object.data.materials.append(mat)
        
        >>> # Assign Mat2 to an object
        >>> assign_material(bpy.context.object, "Mat2")
        [{'name': 'Mat1', 'id': 12345}]  # Returns: []
    """
```
    Examples

    ```python
def assign_material(material_name, quantity):
    """
    Assigns a specified quantity of material to a person.

    Args:
        material_name (str): The name of the material being assigned.
        quantity (int): The number of units of the material being assigned.

    Returns:
        None
    """

    # Explanation
    print(f"Assigning {quantity} units of {material_name} to {material_name}")

    # Example 1: Basic usage
    assign_material("Wood", 10)

    # Example 2: Edge case - Zero quantity
    try:
        assign_material("Metal", 0)
    except ValueError as e:
        print(e)  # Output: 'Quantity must be greater than zero'

    # Example 3: Advanced scenario - Multiple assignments for the same material
    assign_material("Wood", 20)
    assign_material("Paper", 30)
```

```python
def assign_material(material_name, quantity):
    """
    Assigns a specified quantity of material to a person.

    Args:
        material_name (str): The name of the material being assigned.
        quantity (int): The number of units of the material being assigned.

    Returns:
        None

    Raises:
        ValueError: If the quantity is less than or equal to zero
    """

    # Explanation
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    # Example 1: Basic usage
    assign_material("Wood", 10)

    # Example 2: Edge case - Zero quantity
    try:
        assign_material("Metal", 0)
    except ValueError as e:
        print(e)  # Output: 'Quantity must be greater than zero'

    # Example 3: Advanced scenario - Multiple assignments for the same material
    assign_material("Wood", 20)
    assign_material("Paper", 30)
```

```python
def assign_material(material_name, quantity):
    """
    Assigns a specified quantity of material to a person.

    Args:
        material_name (str): The name of the material being assigned.
        quantity (int): The number of units of the material being assigned.

    Returns:
        None

    Raises:
        ValueError: If the quantity is less than or equal to zero
    """

    # Explanation
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    # Example 1: Basic usage
    print(f"Assigning {quantity} units of {material_name} to {material_name}")

    # Example 2: Edge case - Zero quantity
    try:
        assign_material("Metal", 0)
    except ValueError as e:
        print(e)  # Output: 'Quantity must be greater than zero'

    # Example 3: Advanced scenario - Multiple assignments for the same material
    print(f"Assigning {quantity} units of {material_name} to {material_name}")
```
    Docstring

    """```python
def assign_material(ob: bpy.props.Object, mat_name: str) -> None:
    """
    Adds a material to an object's data.

    A new material is added to the object's list of materials and its name is searched for in the given object's data.
    
    Args:
        ob (bpy.props.Object): The object on which the material will be assigned.
        mat_name (str): The name of the material to be assigned.

    Returns:
        None

    Includes:

    A one-line description
    """
```"""
    ```