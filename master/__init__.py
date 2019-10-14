# -*- coding: utf-8 -*-
import os
import time
import subprocess as process
from subprocess import check_output, STDOUT, CalledProcessError

def push(message, path):
    os.system("clear")
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % message)

    try:
        process.check_output(["git", "push", "origin", "master"], stderr=STDOUT)
        print("Process: ", process)
    except CalledProcessError as error:
        os.system("clear")
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)

        if "Updates were rejected because a pushed branch tip is behind its remote" in str(errormsg):
            os.system("clear")
            print("Pushed Branch Tip Behind Remote")
            choice = raw_input("Local state will be saved into master-backup Branch! Y/N")
            if choice.upper() == "Y":
                os.system("clear")
                os.system("git checkout -b master-backup")
                os.system("git push origin master-backup")
                print("Please Merge the States together if needed")
                time.sleep(3)
                os.system("git checkout master")
                os.system("git push origin master")
                os.system("clear")
                repoURL = os.system("git config --get remote.origin.url")
                print(repoURL)
                quit()
            if choice.upper() == "N":
                os.system("clear")
                print("Exiting Program... ")
                time.sleep(2)
                quit()

        if "Updates were rejected because the remote contains work that you" in str(errormsg):
            os.system("clear")
            print('Updates were rejected because the remote contains work that you do not have')
            choice = raw_input("Solve conflict by pulling and pushing? Y/N")
            if choice.upper() == "Y":
                repoURL = os.system("git config --get remote.origin.url")
                print(repoURL)
                raw_input("prompt")
                os.system("git remote add origin %s" % repoURL)
                os.system("git pull origin master")
                os.system("git push origin master")
            if choice.upper() == "N":
                print("Exiting Program... ")
                time.sleep(2)
                quit()

    os.system("clear")
    state = ["Folder: " , path, "Message: " , message, " to Branch: master"]
    return ''.join(state)

def init(path):
    path = path
    print(path)
    commitMsg = raw_input("Commit Message: ")
    push(commitMsg, path)
    return push(commitMsg, path)
