# append_material

    Purpose

    The `append_material` function appends a material from a specified directory to Blender. It uses the `bpy.ops.wm.append` operator, which imports an object or data block by its name and path. The `link=False` parameter ensures that the new material is not linked; it's added as a separate copy in memory.
    Parameters

    ```python
def append_material(directory: str, filepath: str, material_name: str) -> None:
    """
    Appends a material from a specified directory to Blender.

    Parameters:
    - directory (str): The path to the directory containing the material file.
    - filepath (str): The full path to the material file, including its filename.
    - material_name (str): The name of the material to append in Blender.

    Usage Constraints:
    - Ensure that the directory and filepath are correct paths to valid Blender material files.
    - Material names must not already exist in Blender to avoid duplication.
    - This function will add a new copy of the material, not link it to an existing object.
    """
```

Examples:
```python
append_material('/path/to/materials/', '/path/to/materials/MyMaterial.blend', 'MyMaterial')
```
    Returns

    ```python
def append_material(directory_path):
    """
    Appends a material from a specified directory to Blender.

    Args:
        directory_path (str): The path to the directory containing the material file(s).

    Returns:
        list: A list containing messages indicating whether the material was successfully appended or not.
    """

    # Create an empty list to store messages
    message_list = []

    # Check if the directory path is valid
    if directory_path and os.path.isdir(directory_path):
        # Loop through all files in the directory
        for filename in os.listdir(directory_path):
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)
            
            try:
                # Import the material using bpy.ops.wm.append
                bpy.ops.wm.append(filepath=file_path, link=False)
                message_list.append(f"Material '{filename}' appended successfully.")
            except Exception as e:
                # Log an error if appending fails
                message_list.append(f"Failed to append '{filename}': {e}")

    return message_list

# Example usage:
messages = append_material('/path/to/materials')
for message in messages:
    print(message)
```

This function takes a directory path, attempts to append materials from that directory to Blender, and returns a list of messages indicating whether each attempt was successful or if an error occurred. If the directory does not exist or no files are found, it will return an empty list.
    Examples

    ```python
# Basic usage: Appending a material to a list
materials = []
append_material(materials, "Steel")
print(materials)  # Output: ['Steel']

# Edge case: Appending an empty string to avoid list modification
empty_materials = ["Iron"]
append_material(empty_materials, "")
print(empty_materials)  # Output: ['Iron', '']

# Advanced scenario: Using append_material in a more complex context
inventory = []
append_material(inventory, "Gold")
append_material(inventory, "Silver")
append_material(inventory, "Platinum")

def process_inventory(items):
    total_value = 0
    for item in items:
        total_value += calculate_value(item)
    return total_value

calculate_value = lambda x: 100 if x == "Gold" else 50 if x == "Silver" else 200 if x == "Platinum" else 0

print(process_inventory(inventory))  # Output: 600
```
    Docstring

    """```python
def append_material(directory, filepath, material_name):
    """
    Append a material from the given directory to the current scene.

    Args:
        directory (str): The path to the directory containing the material files.
        filepath (str): The full path of the material file to be appended.
        material_name (str): The name of the material to append.

    Returns:
        None: This function does not return any value.

    Examples:
    >>> import bpy
    >>> from pathlib import Path

    # Directory and file paths
    directory = Path("C:/Path/To/Materials")
    filepath = str(directory / "new_material.blend")
    material_name = "NewMaterial"

    # Append the material
    append_material(directory, filepath, material_name)

    # Verify that the material is in the scene
    assert bpy.data.materials.get(material_name) is not None
    """
```"""
    ```