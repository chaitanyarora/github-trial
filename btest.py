import subprocess
import os

cwd = os.path.dirname(os.path.abspath(__file__))
print('1', cwd)

blender_executable = r"/home/runner/work/github-trial/github-trial/blender-4.2.0-linux-x64/blender"
blend_file_paths = [os.path.join(cwd, 'test_drone.blend')]
print('2', blend_file_paths)
test_script_paths = [os.path.join(cwd, 'test_drone.py')]
print('3', test_script_paths)


def test():
    for x in range(len(test_script_paths)):
        blender_command = [blender_executable, blend_file_paths[x], '-b','-P', test_script_paths[x]]
        try:
            print(f'Started testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')
            result = subprocess.run(blender_command, stdout=subprocess.PIPE, text=True, check=True)
            print(result.stdout)
            
        except subprocess.CalledProcessError as e:
            print("Error:", e)

        print(f'Done testing - {test_script_paths[x].rsplit("test_", 1)[-1]}')

if __name__ == '__main__':
    test()