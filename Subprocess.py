# Subprocess class that returns user file directory input
from tkinter import filedialog
import os

class Subprocess:

    def __init__(self):
        pass

    # Returns User Directory
    def ask_user_folder(self):
        return filedialog.askdirectory()
    
    # Returns File URL
    def ask_file(self) -> str:
        return filedialog.askopenfilename(filetypes=(("Executable files", ""),("Any file","*")))

    def find_path(self, dir_name:str, base:str) -> str:
        dir_list = []
        for root, dirs, _ in os.walk(base):
            for dir in dirs:
                if dir == dir_name:  
                    # First encounter is returned
                    dir_list.append(os.path.abspath(os.path.join(root, dir)))
    
        return dir_list
a = Subprocess()
file_dir = a.ask_file()
file_dir = file_dir.split("/")[-1]
folder_dir = a.ask_user_folder()
path_to_contents = a.find_path(file_dir,folder_dir)
print(path_to_contents)