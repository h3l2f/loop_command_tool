import platform
import os

print("Welcome to loop command tool")
print("ver. 0.1")
print("project page : https://tmhhd.cf/project/loop_command_tool")
print("----------------------------------")
while True:
    file = input("type the name of the new file: ")
    if file != "":
        break
    else:
        pass
filepath = "%HOMEPATH%/command/" if platform.system() == "Windows" else "~/command/"
file = filepath + file
cm = input("Enter One command you want to run: ")

while True:
    lib = input("Enter Necessary library (one library every once) {use N to end}: ")
    if lib == "N":
        library = ""
        break
    else:
        pass
    library = f"\nimport {lib}"
content = f"""{library}
import time
import argparse
import os
from datetime import datetime

#sys_time = datetime.now().time()
parser = argparse.ArgumentParser()

# Define command-line arguments
parser.add_argument('-t', type=str)
# Parse the command-line arguments
args = parser.parse_args()

in_time = args.t
in_time = float(in_time)
in_time = in_time*60

while True:
    os.system('{cm}')
    print(f'ran {cm} successfully')
    time.sleep(in_time)

"""
try:
    with open(file,'w') as f:
        f.write(content)
except FileNotFoundError:
    os.system(f"mkdir {filepath}")
    if platform.system() == "Windows":
        os.system(f"type nul > {file}")
    else:
        os.system(f"touch {file}")
        file = os.path.expanduser(file)
    with open(file,'w') as f:
        f.write(content)
if platform.system() == "Windows":
    print(f"Successfully. Your file saved in {filepath}")
else:
    print(f"Successfully. Your file saved in {filepath}")
