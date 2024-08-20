import subprocess
import os


cwd = os.path.dirname(os.path.abspath(__file__))

blender_executable = r"/home/runner/work/github-trial/github-trial/blender-4.2.0-linux-x64/blender-launcher"
print("BUNTTUTBUBUD", blender_executable)
blend_file_paths = [os.path.join(cwd, 'test_drone.blend')]
print("BLEND FILE PATH", blend_file_paths)
test_script_paths = [os.path.join(cwd, 'test_drone.py')]
print("TEST SC FILE PATH", test_script_paths)

def test():
    for x in range(len(test_script_paths)):

        blender_command = [blender_executable, blend_file_paths[x], '-b','-P', test_script_paths[x]]
        print("BLENDER_COMMAN", blender_command)

        try:
            #To read the console output
            result = subprocess.run(blender_command, stdout=subprocess.PIPE, text=True, check=True)
            print(f'Started testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')
            print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        print(f'Done testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')

if __name__ == '__main__':
    test()