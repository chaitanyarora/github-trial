import bpy
from datetime import datetime
import os


bpy.ops.preferences.addon_enable(module='animation_tool')
enabled_addons = bpy.context.preferences.addons.keys()
for addon in enabled_addons:
    print(addon)


# Iterate over all registered classes
for cls in bpy.types.Panel.__subclasses__():
    if 'Drone Setup (' in cls.bl_label: 
        version = (cls.bl_label.split('(')[1][:-1])
        print(version)

cwd = os.path.dirname(os.path.abspath(__file__))

print("pehla", cwd)

# cwd = os.path.abspath(os.path.join(cwd, os.pardir, os.pardir))
print("pehla", cwd)

# Create a file 
log_file = os.path.join(cwd, f'test_report_{version}.txt')

# Panel: Formation

# Section: Drone Setup

# Part 1: (Inputs)




bpy.context.scene.my_tool.drone.total_spheres = 20
bpy.context.scene.my_tool.drone.total_rows = 10
bpy.context.scene.my_tool.drone.x_diff = 1.00
bpy.context.scene.my_tool.drone.y_diff = 1.00

# Part 2: Sphere Grid
bpy.ops.object.sphere_grid()

# # Test 1: (Sphere Grid) Check if spheres are added successfully
if bpy.data.objects.get('1') or bpy.data.objects.get('1EL'):
    print("BHAI HAIIIIIII")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, 'a') as file:
        file.write(f'{timestamp} Test passed ✅ - sphere grid\n')
else:
    print("BHAI HAIIIIIII partyyyy NOOO")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, 'a') as file:
        file.write(f'{timestamp} Test failed ❌ - sphere grid\n')


# Part 3: Reset
bpy.ops.object.reset_scene()

# Test 2: (Reset) Check if collection is empty or not
if len(bpy.data.collections)==0:
    print("BHAI HAIIIIIII partyyyy")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, 'a') as file:
        print("YOOOOOOOOYOYOYOY")
        file.write(f'{timestamp} Test passed ✅ - reset\n')
else:
    print("BHAI HAIIIIIII NOOOO")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_file, 'a') as file:
        file.write(f'{timestamp} Test failed ❌ - reset\n')