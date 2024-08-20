import bpy
import os

def install_addon(addon_path):
    # Ensure the addon path is correct
    addon_path = os.path.abspath(addon_path)
    
    # Install the addon
    bpy.ops.preferences.addon_install(filepath=addon_path)
    
    # Enable the addon
    addon_name = os.path.basename(addon_path).replace(".py", "")
    bpy.ops.preferences.addon_enable(module=addon_name)
    
    # Save user preferences to retain the addon
    bpy.ops.wm.save_userpref()

# Path to your addon (can be a .zip or a folder containing the __init__.py)
addon_path = "/home/runner/work/github-trial/github-trial/animation_tool.zip"

# Run the installation
install_addon(addon_path)
