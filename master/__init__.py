import os

def push(message, path):
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % message)
    os.system("git push origin master")

def init(path):
    path = path
    print(path)
    commitMsg = raw_input("Commit Message: ")

    for file in os.listdir(path):
        print(file)
    #if .git in Directory -> Do it / If not create git repo first

    push(commitMsg, path)
