import subprocess


def execute_script(script_path, *args):
    try:
        # Construct the command to run the script with arguments
        command = ['python', script_path] + list(args)

        # Execute the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing the script: {e}")
    except FileNotFoundError:
        print("The specified script file does not exist.")


import os


def find_python_files(folder_path):
    python_files = []
    try:
        # List all files in the folder
        files = os.listdir(folder_path)

        # Filter out the .py files
        python_files = [file for file in files if file.endswith(".py")]
    except FileNotFoundError:
        print("The specified folder does not exist.")
    except PermissionError:
        print("Permission denied to access the folder.")

    return python_files

folder_path = "C:\\Users\\diaco\\PycharmProjects\\TssProj"
script_path = "main.py"

py_files = find_python_files(folder_path)

print("Python files found:")
for file in py_files:
    print(file)
    execute_script(script_path, folder_path + '\\' + file)
