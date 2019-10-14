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


#Initializes Watcher via watchdog Module
class Handler(FileSystemEventHandler):
        @staticmethod
        def on_any_event(event):
            if event.is_directory:
                return None

#If File was modified -> Gets name of file
#-> Trys Commit -> Branch -> Push
            elif event.event_type == 'modified':
                arr = []
                print(event)
                arr.append(event)
                print(arr)
                time.sleep(4)
                print("STUFF MODIFIED")
                os.system("git status")
                commit()
                autoBranch()
                push()

def push():
    rand = random.randint(1,9)
    try:
        os.system("git push origin auto-master")
        print("Pushing files to auto-master...")
        os.system("git status")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
    status = process.check_output(["git", "push", "origin", "auto-master"], stderr=STDOUT)
    if "Everything up-to-date" in str(status):
        print("####ERROR")
        os.system("git checkout -f -b auto-master%s" % rand)
        #Merge / New Branch


def autoBranch():
    try:
        os.system("git checkout -b auto-master")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
        if "A branch named" in str(errormsg) and "already exists" in str(errormsg):
            os.system("git checkout -f auto-master")


def commit():
    try:
        status = process.check_output(["git", "status"], stderr=STDOUT)
        print(str(status))
        time.sleep(4)
        if "modified" in str(status):
            print("Somethings modified")
            print(status)
            autoBranch()
            os.system("git add *")
            os.system("git commit -m %s" % "auto-pushed_please_merge")
            push()
        else:
            print("No modified Data found")
            quit()
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
