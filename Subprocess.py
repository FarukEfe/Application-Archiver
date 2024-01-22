# Subprocess class that opens FileExplorer and returns user input

import subprocess as proc
from tkinter import filedialog
import time as t

class Subprocess:

    def __init__(self):
        pass
    
    # Returns File URL
    def execute(self) -> str:
        return filedialog.askopenfilename(filetypes=(("Executable files", ""),("Any file","*")))

a = Subprocess()
res = a.execute()
print(res)