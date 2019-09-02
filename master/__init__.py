import os
import time
import subprocess as process
from subprocess import check_output, STDOUT, CalledProcessError

def push(message, path):
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % message)

    try:
        process.check_output(["git", "push", "origin", "master"], stderr=STDOUT)
        print("Process: ", process)
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)

    if "Updates were rejected because a pushed branch tip is behind its remote" in str(errormsg):
        print("PUSHED BRANCH TIP BEHIND REMOTE")
        choice = raw_input("Local state will be saved into master-backup Branch! Y/N")
        if choice == "Y" or choice == "y":
            os.system("git checkout -b master-backup")
            os.system("git push origin master-backup")
            print("Please Merge the States together if needed")
            time.sleep(3)
            os.system("git checkout master")
            os.system("clear")
            repoURL = os.system("git config --get remote.origin.url")
            print(repoURL)
            quit()
        if choice == "N" or choice == "n":
            print("Exiting Program... ")
            time.sleep(2)
            quit()
    os.system("git push origin master")

    if "Updates were rejected because the remote contains work that you" in str(errormsg):
        repoURL = os.system("git config --get remote.origin.url")
        print(repoURL)
        raw_input("prompt")
        os.system("git remote add origin repoURL")
        os.system("git pull origin master")
        os.system("git push origin master")


    state = {"Folder: " + path, "Message: " + message, " to Branch: master"}
    return state

def init(path):
    path = path
    print(path)
    commitMsg = raw_input("Commit Message: ")

    for file in os.listdir(path):
        print(file)
    #if .git in Directory -> Do it / If not create git repo first

    push(commitMsg, path)

    return push(commitMsg, path)
