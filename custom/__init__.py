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
            print("WE GOT NO BRANCH HERE BOY")
            os.system("git checkout -b %s" % branch)
            os.system("git push origin %s" % branch)

        if "A branch named" and "already exists" in str(errormsg):
            print("WE ALREADY GOT THIS BRANCH HERE BOY")
            os.system("git checkout %s" % branch)

        colorred = "\033[1;31;40m]"
        colorwhite = "\\033[0m 1;31;40m"
        state = {"pushed ", path, " ", " with commit Message: ", message, " to Branch: ", branch}


def init(path):
    path = path
    print(path)
    commitMsg = raw_input("Commit Message: ")
    branch = raw_input("Branch name")
    #If branch not there -> react and create branch or push to master

    for file in os.listdir(path):
        print(file)
    #if .git in Directory -> Do it / If not create git repo first

    push(commitMsg, path, branch)
