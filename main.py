import subprocess
import os
import time
import pyautogui as p
from pynput.keyboard import Controller
keyboard = Controller()


def run_powershell_command(command):
    try:
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        print("SUCCESSFULLY EXECUTED")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error executing PowerShell command:")
        print(e)
        print("Command:", e.cmd)
        print("Return code:", e.returncode)
        print("Error message:")
        print(e.stderr)
        return None
    
# /////////////////////////////////////////////////////////////////////////////////////////////////


def runserver(folder_path,folder_name,project_name):
    # run_command=f"cd ~;"
    # run_command+=f" cd {folder_path};"
    # run_command+=f" cd {folder_name} ;"
    # run_command+=f" cd {project_name} ;"
    # run_command+=f" python manage.py runserver;"
    home_directory = os.path.expanduser("~")
    full_path = os.path.join(home_directory, folder_path, folder_name, project_name)
    run_command = rf"cd {full_path}"
    p.hotkey('win','r')
    p.write('powershell')
    p.hotkey('enter')
    time.sleep(2)
    keyboard.type(run_command)
    p.hotkey('enter')
    time.sleep(1)
    keyboard.type("python manage.py runserver;")
    p.hotkey('enter')

# /////////////////////////////////////////////////////////////////////////////////////////////////




# Example usage:
print("-------------------------------------------------------")
folder_path="Documents/test"
folder_name="project_folder"
project_name="project"
app_name="app"
# folder_name=input("Enter your folder name: ") 
# project_name=input("Enter your project name: ")
print("-------------------------------------------------------")
command_to_run=f"cd ~; cd {folder_path};"
command_to_run += f"mkdir {folder_name}; cd {folder_name} ;"
# print("***********************  Folder created  ***********************")
command_to_run+="python -m venv venv ;"
command_to_run+="./venv/Scripts/activate ;"
# print("***********************  venv active  ***********************")
command_to_run+="pip install django ;"
# print("***********************  Django installed  ***********************")
command_to_run+=f"django-admin startproject {project_name} ;"
# print(f"***********************  PROJECT {project_name} CREATED  ***********************")
command_to_run+=f"cd {project_name} ;"
command_to_run+="python manage.py migrate;"
command_to_run+=f"python manage.py startapp {app_name} ;"
# print(f"***********************  APP {app_name} CREATED  ***********************")



output = run_powershell_command(command_to_run)
if output:
    print("PowerShell Output:")
    print(output)

runserver_prompt=input("do you want to run the server? (this will open your powershell so do not worry) : ")
if "y" in str(runserver_prompt).lower():
    runserver(folder_path,folder_name,project_name)