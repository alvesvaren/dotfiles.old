#!/usr/bin/python3

import os
import subprocess
from sys import argv, stdout
from shutil import copyfile

def confirm(msg: str, default: bool = False) -> bool:
    try:
        value = input(f"{msg} [{'Y/n' if default else 'y/N'}] ").strip().lower()
    except KeyboardInterrupt:
        print()
        return False
    return value in ["yes", "y"] or (default and not value)

if __name__ == "__main__":
    offset = 0
    try:
        if argv[1] == "copy":
            offset = 1
            print("Copying file system files to repo")
        elif argv[1] == "install":
            offset = -1
            print("Installing files locally")
            if not confirm("Continue?", True):
                exit(2)
    except IndexError:
        print(f"Usage: {argv[0]} <install|copy>")
        exit(1)
    with open("filelist") as file:
        for item in file.readlines():
            files = item.strip().split(" ")
            files = (os.environ["HOME"] + "/" + files[0], "./files/" + files[1])[::offset]
            os.makedirs("/".join(files[1].split("/")[:-1]), exist_ok=True)
            copyfile(files[0], files[1])
    
    process_stdout = subprocess.Popen("lsb_release -is", shell=True, stdout=subprocess.PIPE).stdout.read()
    if offset == -1 and os.path.isfile("/usr/bin/yay"):
        print("Found yay in binary folder...")
        with open("pkglist") as file:
            if confirm("Would you like to install packages too?"):
                os.system("yay --noconfirm -S " + " ".join([i.strip() for i in file.readlines()]))

