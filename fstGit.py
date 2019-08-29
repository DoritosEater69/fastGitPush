import os
import master as mstr
import custom as cstm


#master
def gitMaster():
    mstr.init()

def gitCustom():
    custom.init()

def menu():
    print("")
    print("")
    print("1. Master")
    print("2. Custom")
    print("")
    print("")
    choice = raw_input("# ")

    if choice == "1":
        gitMaster()
    if choice == "2":
        gitCustom()

menu()
