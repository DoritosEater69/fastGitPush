import os
import watchdog
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess as process
from subprocess import Popen, PIPE
import sys
from subprocess import check_output, STDOUT, CalledProcessError


#Initializes Watcher via watchdog Module
class Watcher():
    os.system("clear")
    path = str(sys.argv[1])
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(15)
        except:
            self.observer.stop()
            print("Error!")

        self.observer.join()

    def stop(self):
        event_handler = Handler()
        self.observer.stop()



def sliceEvent(event):
    fullEvent = []
#Event set to String and Splitted by space -> Path of modified File sliced out
    split = str(event).split(" ")
    for value in split:
        fullEvent.append(value)
    #print(fullEvent[1])
    return fullEvent[1]

#Initializes Watcher via watchdog Module
class Handler(FileSystemEventHandler):
        @staticmethod
        def on_any_event(event):
            if event.is_directory:
                return None
#If File was modified -> Gets name of file
#-> Trys Commit -> Branch -> Push
            elif event.event_type == 'modified':
                eventFiles = sliceEvent(event)
                print("File ", eventFiles, " was modified.")
                time.sleep(4)
                os.system("clear")
                commit(eventFiles)


#Pushes with randBranch to auto-Master -> if everything up to date -> use randBranch
def autoBranch():
    rand = random.randint(1,100)
    try:
        randBranch = "auto-master%s" % rand
        fullBranch = os.system("git checkout -b %s" % randBranch)
        return randBranch
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
        if "A branch named" in str(errormsg) and "already exists" in str(errormsg):
            randBranch = "auto-master%s" % rand
            fullBranch = os.system("git checkout -b %s" % randBranch)
            return randBranch

#Commit of Changes -> if Data was modified -> name of File attached to commit message -> push
def commit(eventFiles):
    try:
        status = process.check_output(["git", "status"], stderr=STDOUT)
        print(str(status))
        time.sleep(4)
        if "modified" in str(status):
            print(eventFiles, " modified")
            print(status)
            os.system("git add *")
            #os.system("git commit -m %s" % eventFiles)
            os.system("git commit -m test")
            push(autoBranch(), eventFiles)
        else:
            print("No modified Data found. Keep on working!")
            print("use control + c to quit the Program")
            print("end")
            Watcher().stop()
            init()
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)


#Pushes with randBranch to random Branch name -> if everything up to date -> use randBranch
def push(randBranch, eventFiles):
    try:
        #status = process.check_output(["git", "push", "origin", "%s" % randBranch], stderr=STDOUT)
        os.system("git push origin %s" % randBranch)
        print("Pushing files to auto-master...")
        checkStatus = process.check_output(["git", "status"], stderr=STDOUT)
        print("Status: ", checkStatus)
        time.sleep(4)
        if "Everything up-to-date" in str(checkStatus):
            print("end")
            Watcher().stop()
            init()
        if "Changes to be committed" in str(checkStatus):
            os.system("git add *")
            #os.system("git commit -m %s" % eventFiles)
            os.system("git commit -m test")
            os.system("git push origin %s" % randBranch)
            print("Pushing files to ", randBranch, " ...")
            os.system("git status")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        if "A branch named" in str(errormsg):
            print("error", errormsg)
            quit()

#Merge / New Branch


def init():
#Checks if more than 10 branches -> if so -> Delete them
    cleanUp()
    print("")
    print("")
    print("Auto Watcher (Auto-Branch)")
    print("Your Changes will be saved to the Auto-Branch.")
    print("After you are done with your work, everything needs to get merged together.")
    print("")
    print("")
    w = Watcher()
    w.run()

#TESTEN!!! Careful
def cleanUp():
    try:
        #git branch | grep -v '^*' | xargs git branch -d
        os.system("git branch | wc -l >tmp")
        print(open('tmp', 'r').read())
        # test = process.Popen(["git", "branch", "|", "wc", "-l"], stdout=PIPE)
        # test = test.communicate()
        # print(str(test))
        #branches = process.check_output(["git", "branch", "|", "wc", "-l"], stderr=STDOUT)
        #print(branches)
        # if int(branches) > 10:
        #     print("Delete!")
        #     os.system("git checkout master")
#Deletes Branches that have been merged to master
            #os.system("git branch | grep -v '^*' | xargs git branch -d")
    except process.CalledProcessError as e:
        print("Error: ", e.output)
    # else:
    #     pass

