# Subprocess class that opens FileExplorer and returns user input

import subprocess as proc
import time as t

class Subprocess:

    def __init__(self):
        pass

    def execute(self):
        explorer_proc = proc.run(
                            r'explorer "C:\Users\efefr.USER"'
                            ,capture_output=True
                            ,stderr=proc.PIPE
                            ,check=True
                            )
        while True:
            print(explorer_proc.args)
            print(explorer_proc.returncode)
            print(explorer_proc.stderr)
            print(explorer_proc.stdout)
            t.sleep(1)


a = Subprocess()
a.execute()