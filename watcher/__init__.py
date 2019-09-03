import os
import time
import subprocess as process
from subprocess import check_output, STDOUT, CalledProcessError


def push():
    try:
        os.system("git push origin auto-master")
        print("Files pushed to auto-master")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
        if "A branch named" in str(errormsg) and "already exists" in str(errormsg):
            os.system("git checkout -f auto-master")


def autoBranch():
    try:
        os.system("git checkout -b auto-master")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
        if "A branch named" in str(errormsg) and "already exists" in str(errormsg):
            os.system("git checkout -f auto-master")


def commit():
    try:
        status = process.check_output(["git", "status"], stderr=STDOUT)
        if "modified" in str(status):
            print("Somethings modified")
            print(status)
            os.system("git add *")
            autoBranch()
            os.system("git commit -m %s" % "auto-master%20pushed%20-%20please%20merge")
            push()
        else:
            print("No modified Data found")
            quit()
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)

def init(path):
    print("")
    print("")
    print("Auto Watcher (Auto-Branch)")
    print("Your Changes will be saved to the Auto-Branch.")
    print("After you are done with your work, everything needs to get merged together.")
    print("")
    print("")
    path = path
    print(path)
    os.system("cd %s" % path)
    commit()
