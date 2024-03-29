import os
import subprocess as process
from subprocess import check_output, STDOUT, CalledProcessError


def push(message, path, branch):
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % message)

    try:
        process.check_output(["git", "push", "origin", branch], stderr=STDOUT)
        print("Process: ", process)
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)

    # process.check_output(["git", "push", "origin", branch], stderr=STDOUT)
    # log = error.output, error.returncode, error.Message

        if "src refspec" and "does not match any" in str(errormsg):
            print("Creating new Branch...")
            os.system("git checkout -b %s" % branch)
            os.system("git push origin %s" % branch)

        if "A branch named" and "already exists" in str(errormsg):
            print("Branch is already existing")
            os.system("git checkout %s" % branch)

        os.system("git checkout -b %s" % branch)
        os.system("git push origin %s" % branch)
        state = " pushed " + path + " with commit Message: " + message + " to Branch: " + branch
        return state

def init(path):
    path = path
    print(path)
    commitMsg = raw_input("Commit Message: ")
    branch = raw_input("Branch name")
    push(commitMsg, path, branch)
