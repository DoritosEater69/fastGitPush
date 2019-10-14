import os
import time
import sys
import master as mstr
import custom as cstm
import watcher as wtch
import subprocess as process

try:
    path = str(sys.argv[1])

    #Later when Implemented as Terminal Command (sets path to current path)
    #path = os.system(pwd)
    # for file in os.listdir(path):
    #     print(file)
    #     if ".git" in file:
    #         print("This is a GIT Repo")
    #     else:
    #         print("This is not a GIT Repo")

except Exception as e:
    if "list index out of range" in str(e):
        print("usage: python fstGit.py PATH OF GIT FOLDER")
        #Usage if added as terminal command
        #print("usage: fstGit PATH OF GIT FOLDER/CURRENT Path")
        time.sleep(3)
        os.system("clear")
        quit()


def gitMaster(path):
    print(mstr.init(path))

def gitCustom(path):
    print(cstm.init(path))

def gitWatch(path):
    wtch.init()

def menu():
    os.system("git checkout master")
    print("")
    print("1. Master")
    print("2. Custom")
    print("3. Watcher")
    print("")
    choice = raw_input("# ")

    if choice == "1":
        gitMaster(path)
        menu()
    if choice == "2":
        gitCustom(path)
        menu()
    if choice == "3":
        gitWatch(path)
        menu()

menu()
