import subprocess

####### Code made with the help of ChatGPT #######
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


folder_path = ".//"
script_path = "java_metrics.py"

def find_java_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                print(file_path)
                execute_script(script_path, file_path)

find_java_files("..\\Tss_Test")
