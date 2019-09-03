import os
import time
import subprocess as process
from subprocess import check_output, STDOUT, CalledProcessError


def push(path):
    print("#")

def commit(path):
    try:
        gitAnswer = process.check_output(["git", "status"], stderr=STDOUT)
        print(str(gitAnswer))
        if "modified" in str(gitAnswer):
            print("Somethings modified")
            print(gitAnswer)
            os.system("git add *")
            os.system("git commit -m %s ")
        # if "Changes not staged for commit" in str(process):
        #     print("Something changed")
        #     os.system("git add *")
        #     os.system("git commit -m %s" )
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
    commit(path)
