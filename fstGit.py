import os
import sys
import master as mstr
import custom as cstm
import subprocess as process


path = str(sys.argv)

#master
def gitMaster(path):
    mstr.init(path)

def gitCustom(path):
    cstm.init(path)

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
