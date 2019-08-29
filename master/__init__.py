import os

def push(message, path):
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % message)
    os.system("git push origin master")

    state = "pushed", path, "with commit Message: ", message, "to Master"
    return state

def init(path):
    print(path)
    if len(path) > 1:
        path = '/_backup/htdocs/git/_programming/tools/python/fastGitPush'
    else:
        path = path
    commitMsg = raw_input("Commit Message: ")

    for file in os.listdir(path):
        print(file)
    #if .git in Directory -> Do it / If not create git repo first

    push(commitMsg, path)
