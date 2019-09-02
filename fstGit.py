import os
import time
import sys
import master as mstr
import custom as cstm
import subprocess as process

try:
    path = str(sys.argv[1])
except Exception as e:
    if "list index out of range" in str(e):
        print("usage: python fstGit.py PATH OF GIT FOLDER")
        time.sleep(3)
        os.system("clear")
        quit()

#master
def gitMaster(path):
    mstr.init(path)

def gitCustom(path):
    cstm.init(path)
    print(cstm)

def menu():
    print("")
    print("1. Master")
    print("2. Custom")
    print("")
    choice = raw_input("# ")

    if choice == "1":
        gitMaster(path)
        menu()
    if choice == "2":
        gitCustom(path)
        menu()

menu()
