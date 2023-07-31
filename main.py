import subprocess,os

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

# Example usage:
print("-------------------------------------------------------")
folder_name="folder"
project_name="project"
app_name="app"
# folder_name=input("Enter your folder name: ") 
# project_name=input("Enter your project name: ")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
command_to_run=""
command_to_run = f"mkdir {folder_name}; cd {folder_name} ;"
print("***********************  Folder created  ***********************")
command_to_run+=f"python -m venv venv ;"
command_to_run+=f"./venv/Scripts/activate ;"
# command_to_run+=f"ls ;"
print("***********************  venv active  ***********************")
command_to_run+=f"pip install django ;"
print("***********************  Django installed  ***********************")
command_to_run+=f"django-admin startproject {project_name} ;"
print(f"***********************  PROJECT {project_name} CREATED  ***********************")
command_to_run+=f"cd project ;"
command_to_run+=f"python manage.py migrate;"
command_to_run+=f"python manage.py startapp {app_name} ;"
print(f"***********************  APP {app_name} CREATED  ***********************")
command_to_run+=f"python manage.py runserver;"
print("http://127.0.0.1:8000/")




output = run_powershell_command(command_to_run)

if output:
    print("PowerShell Output:")
    print(output)
