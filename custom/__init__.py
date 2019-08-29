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

    if "src refspec" and "does not match any" in str(errormsg):
        print("WE GOT NO BRANCH HERE BOY")
        os.system("git checkout -b %s" % branch)
        os.system("git push origin %s" % branch)
    if "src refspec" and "does not match any" in str(errormsg):
        print("WE GOT THE SAME BRANCH HERE BOY, RENAME IT")


        state = "pushed", path, "with commit Message: ", message, "to Branch: ", branch
        return state

def init():
    path = '/Applications/MAMP/htdocs/git/_programming/tools/python/fastGitPush/'
    commitMsg = raw_input("Commit Message: ")
    branch = raw_input("Branch name")
    #If branch not there -> react and create branch or push to master

    for file in os.listdir(path):
        print(file)
    #if .git in Directory -> Do it / If not create git repo first

    push(commitMsg, path, branch)
