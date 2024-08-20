import subprocess

blender_executable = r"/home/runner/work/github-trial/github-trial/blender-4.2.0-linux-x64/blender"
addon_script = "/home/runner/work/github-trial/github-trial/install_addon.py"

# Call Blender with the script
subprocess.run([blender_executable, '--background', '--python', addon_script])
