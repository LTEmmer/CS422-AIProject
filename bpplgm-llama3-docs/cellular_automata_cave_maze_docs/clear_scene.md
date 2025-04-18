# clear_scene

    Purpose

    This function clears a 3D object scene in Blender using the Python API.

Documentation:
```python
def clear_scene():
    """
    Clears a 3D object scene in Blender by polling for mode changes, selecting all objects, and deleting them.

    Returns:
        None
    """
```
Examples:

*   To use this function, simply call it: `clear_scene()`
*   This will immediately close any open windows or tabs in the Blender UI window.
    Parameters

    ```python
def clear_scene():
    """
    Clears a 3D object scene in Blender by polling for mode changes, selecting all objects, and deleting them.

    Parameters:
        None

    Returns:
        None
    """

    # Polling for mode changes to determine which UI window needs to be closed
    while True:
        poll_mode()

# Continuously poll the Blender API until a valid mode is detected or an error occurs
```
Examples:

*   To use this function, simply call it: `clear_scene()`
*   This will immediately close any open windows or tabs in the Blender UI window.
    Provide Google-style parameter documentation with:
    - Name: `poll_mode`
    - Type: None (this is a built-in API method)
    - Description: Polls the Blender API for mode changes until a valid one is detected.
    - Usage constraint: This function must be called repeatedly to clear the scene.
    Returns

    ```python
def clear_scene():
    """
    Clears a 3D object scene in Blender by polling for mode changes, selecting all objects, and deleting them.

    Returns:
        None
    """
    # Return type: This function does not return any value.
    # Description: The 'clear_scene' function clears a 3D object scene in Blender.
    # Special cases:
    #   - If no mode is changed (polling occurs), the function will delete all objects in the scene, including active and inactive ones.
```

```python
# Return type of 'clear_scene'
return_type = "None"

# Description of the return value
description_return_type = f"This function does not return any value."

# Special cases for return value
special_cases_return_value = None

print(f"Return type: {return_type}")
print(f"Description: The 'clear_scene' function clears a 3D object scene in Blender.")
print(f"Special cases:")
print(f"- If no mode is changed (polling occurs), the function will delete all objects in the scene, including active and inactive ones.")
```
    Examples

    ```python
def clear_scene(env: dict) -> None:
    """
    Clears the scene by resetting all environment variables to their default values.

    Args:
        env (dict): The environment dictionary containing scene settings and defaults.

    Returns:
        None
    """
    # Explanation
    print("Clearing scene...")
    
    # Clearing the 'CAMERA' variable
    if 'CAMERA' in env:
        del env['CAMERA']
        
    # Clearing the 'LIGHT' variable
    if 'LIGHT' in env:
        del env['LIGHT']

def main():
    """
    Demonstrates basic usage of clear_scene.

    Creates a sample environment dictionary and calls clear_scene twice.
    """
    # Explanation
    print("Basic Usage:")
    
    # Creating an environment dictionary with some scene settings
    env = {
        'CAMERA': {'azimuth': 0, 'elevation': 30},
        'LIGHT': {'type': 'sun'}
    }
    
    # Calling clear_scene to reset the camera and light variables
    clear_scene(env)
    
    print("Scene cleared!")
    
    # Clearing scene for edge case
    env = {
        'CAMERA': {'azimuth': -90, 'elevation': 40},
        'LIGHT': {'type': 'star'}
    }
    clear_scene(env)

def main_edge_case():
    """
    Demonstrates an edge case scenario where the environment dictionary has a custom camera setting.

    Creates an environment dictionary with a custom camera and light settings.
    """
    # Explanation
    print("Edge Case:")
    
    # Creating an environment dictionary with a custom camera and light settings
    env = {
        'CAMERA': {'azimuth': -90, 'elevation': 40},
        'LIGHT': {'type': 'star'}
    }
    
    # Calling clear_scene to reset the camera variable
    clear_scene(env)

def main_advanced_scenario():
    """
    Demonstrates an advanced scenario where the environment dictionary has multiple custom settings.

    Creates a sample environment dictionary with multiple custom scene settings.
    """
    # Explanation
    print("Advanced Scenario:")
    
    # Creating an environment dictionary with multiple custom scene settings
    env = {
        'CAMERA': {'azimuth': 0, 'elevation': 30},
        'LIGHT': {'type': 'sun'},
        'FLOOR': {'material': 'stone', 'color': (1.0, 0.5, 0.2)}
    }
    
    # Calling clear_scene to reset all custom scene settings
    for setting in ['CAMERA', 'LIGHT', 'FLOOR']:
        if setting in env:
            del env[setting]

if __name__ == "__main__":
    main()
```
    Docstring

    """```
`clear_scene`: Clears the current 3D scene by switching to object mode, selecting all objects, and deleting them.

```python
Args:
    None

Returns:
    None

Examples:
    >>> bpy.ops.clear_scene()
    """
    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage
```"""
    ```