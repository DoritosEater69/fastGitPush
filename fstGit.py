import os

path = '/Applications/MAMP/htdocs/git/_programming/tools/python/fastGitPush/'
commitMsg = raw_input("Commit Message: ")

for file in os.listdir(path):
    print(file)
#if .git in Directory -> Do it / If not create git repo first



os.system("cd %s" % path)
os.system("git add *")
os.system("git commit -m %s" % commitMsg)
os.system("git push origin master")
