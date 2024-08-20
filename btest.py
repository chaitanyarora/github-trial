import subprocess
import os


cwd = os.path.dirname(os.path.abspath(__file__))

blender_executable = os.environ.get("PATH")
print("BUNTTUTBUBUD", os.environ.get("PATH"))
blend_file_paths = [os.path.join(cwd, 'test_input', 'test_drone.blend')]
test_script_paths = [os.path.join(cwd, 'test_cases', 'test_drone.py')]

def test():
    for x in range(len(test_script_paths)):

        blender_command = [blender_executable, blend_file_paths[x], '-P', test_script_paths[x]]

        try:
            #To read the console output
            # result = subprocess.run(blender_command, stdout=subprocess.PIPE, text=True, check=True)
            print(f'Started testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')
            # print(result.stdout)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        print(f'Done testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')

if __name__ == '__main__':
    test()