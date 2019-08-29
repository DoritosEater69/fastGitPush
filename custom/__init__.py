import os


def push(message, path, branch):
    try:
        os.system("cd %s" % path)
        os.system("git add *")
        os.system("git commit -m %s" % message)
        os.system("git push origin %s" % branch)
    except Exception as e:
        print("Error: ", e)

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
