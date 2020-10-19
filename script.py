#!/usr/bin/python3

import os
from sys import argv
from shutil import copyfile

print(os.environ["HOME"])

if __name__ == "__main__":
    offset = 0
    try:
        if argv[1] == "copy":
            offset = 1
            print("Copying file system files to repo")
        elif argv[1] == "install":
            offset = -1
            print("Installing files locally")
    except IndexError:
        print(f"Usage: {argv[0]} <install|copy>")
        exit(1)
    with open("filelist") as file:
        for item in file.readlines():
            files = item.strip().split(" ")
            files = (os.environ["HOME"] + "/" + files[0], "./" + files[1])[::offset]
            os.makedirs("/".join(files[1].split("/")[:-1]), exist_ok=True)
            copyfile(files[0], files[1])