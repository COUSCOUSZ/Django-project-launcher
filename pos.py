import pyautogui as pgui
import time
from tkinter.filedialog import askdirectory
from pynput.keyboard import Controller
keyboard = Controller()

print("-------------------------------------------------------")
folder_path=askdirectory(title='My Title',mustexist=True)
folder_name=input("Enter your folder name: ") 
project_name=input("Enter your project name: ")
app_name=input("Enter your app name: ")
static_folder_prompt=input("do you want to create a static folder? (Y or N) :")
template_folder_prompt=input("do you want to create a template folder? (Y or N) :")
runserver_prompt=input("do you want to run the server? (Y or N) :")

# folder_name="folder"
# project_name="proj"
# app_name="app"
print("-------------------------------------------------------")

pgui.hotkey('win','r')
pgui.write('cmd')
pgui.hotkey('enter')
time.sleep(2)


keyboard.type(f'cd {folder_path}')
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type(f'mkdir {folder_name}')
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type(f'cd {folder_name}')
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type("python -m venv venv")
pgui.hotkey('enter')

keyboard.type("cd venv\Scripts")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type("activate")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type("pip install django")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type("cd ..\..")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type(f"django-admin startproject {project_name}")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type(f"cd {project_name} ")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type("python manage.py migrate")
pgui.hotkey('enter')
time.sleep(0.7)

keyboard.type(f"python manage.py startapp {app_name} ")
pgui.hotkey('enter')
time.sleep(0.7)

if "y" in str(static_folder_prompt).lower():
    keyboard.type("mkdir static")
    pgui.hotkey('enter')
    time.sleep(0.7)

if "y" in str(template_folder_prompt).lower():
    keyboard.type(f"cd {app_name}")
    pgui.hotkey('enter')
    time.sleep(0.7)
    keyboard.type(f"mkdir templates")
    pgui.hotkey('enter')
    time.sleep(0.7)


keyboard.type("cd ..")
pgui.hotkey('enter')
time.sleep(0.7)

if "y" in str(runserver_prompt).lower():
    keyboard.type("python manage.py runserver")
    pgui.hotkey('enter')
    time.sleep(0.7)



