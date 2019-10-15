import os
import watchdog
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess as process
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
                os.system("clear")
                autoBranch()
                os.system("clear")
                push()

def push(randBranch):
    try:
        os.system("git push origin %s" % randBranch)
        print("Pushing files to auto-master...")
        os.system("git status")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
    status = process.check_output(["git", "push", "origin", "auto-master"], stderr=STDOUT)
    if "Everything up-to-date" in str(status):
        os.system("git push origin %s" % randBranch)
#Merge / New Branch


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


def commit(eventFiles):
    try:
        status = process.check_output(["git", "status"], stderr=STDOUT)
        print(str(status))
        time.sleep(4)
        if "modified" in str(status):
            print(eventFiles, " modified")
            print(status)
            os.system("git add *")
            os.system("git commit -m %s" % "auto-pushed_please_merge")
            push(autoBranch())
        else:
            print("No modified Data found. Keep on working!")
            print("use control + c to quit the Program")
            quit()
            exit()
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)

def init():
    print("")
    print("")
    print("Auto Watcher (Auto-Branch)")
    print("Your Changes will be saved to the Auto-Branch.")
    print("After you are done with your work, everything needs to get merged together.")
    print("")
    print("")
    w = Watcher()
    w.run()
