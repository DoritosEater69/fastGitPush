import os


#master
# path = '/Applications/MAMP/htdocs/git/_programming/tools/python/fastGitPush/'
# commitMsg = raw_input("Commit Message: ")

# for file in os.listdir(path):
    # print(file)
#if .git in Directory -> Do it / If not create git repo first



# os.system("cd %s" % path)
# os.system("git add *")
# os.system("git commit -m %s" % commitMsg)
# os.system("git push origin master")


#custom
path = '/Applications/MAMP/htdocs/git/_programming/tools/python/fastGitPush/'
commitMsg = raw_input("Commit Message: ")
branch = raw_input("Branch name")
#If branch not there -> react and create branch or push to master

for file in os.listdir(path):
    print(file)
#if .git in Directory -> Do it / If not create git repo first


try:
    os.system("cd %s" % path)
    os.system("git add *")
    os.system("git commit -m %s" % commitMsg)
    os.system("git push origin %s" % branch)
except Exception as e:
    print(e)
