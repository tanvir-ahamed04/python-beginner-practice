import subprocess
from time import sleep
import tempfile

while True:
    tree_path = r'C:\Windows\System32\tree.exe'
    subprocess.Popen('start cmd /k cd %s & tree /f' % tree_path, shell=True)
    subprocess.Popen('start run.tree', shell=True)
    subprocess.Popen('start cmd', shell=True)
    subprocess.Popen('calc.exe')
    # with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
    #     temp_file.write("Assalamu alaikum (: \n valo achen ? ")
    # process = subprocess.Popen(['notepad', temp_file.name])
    # process.wait() 
    # with open(temp_file.name, 'r') as f:
    #     content = f.read()
    #     print("Content written to Notepad and read back:", content)

    # # Clean up: Delete the temporary file
    # import os
    # os.remove(temp_file.name)
    sleep(1)
    
    