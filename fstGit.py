import os
import master as mstr
import custom as cstm
import subprocess as process


#master
def gitMaster(path):
    mstr.init(path)

def gitCustom(path):
    cstm.init(path)

def menu(path):
    print("")
    print("")
    print("1. Master")
    print("2. Custom")
    print("cd ...PATH - Locate GIT folder")
    print("")
    choice = raw_input("# ")

    if choice == "1":
        gitMaster(path)
        menu("n")
    if choice == "2":
        gitCustom(path)
        menu("n")
    if choice == "cd":
        path = raw_input("Path: ")
        os.chdir(path)
        process.call(["ls"])
        menu(path)

menu("n")
