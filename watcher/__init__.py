import os
import watchdog
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess as process
import sys
from subprocess import check_output, STDOUT, CalledProcessError



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
                time.sleep(2)
        except:
            self.observer.stop()
            print("Error!")

        self.observer.join()


class Handler(FileSystemEventHandler):
        @staticmethod
        def on_any_event(event):
            if event.is_directory:
                return None

            elif event.event_type == 'modified':
                print("STUFF MODIFIED")
                os.system("git status")
                commit()
                autoBranch()
                push()

def push():
    try:
        os.system("git push origin auto-master")
        print("Pushing files to auto-master...")
        os.system("git status")
    except CalledProcessError as error:
        errormsg = error.output, error.returncode, error.message
        print("error", errormsg)
        if "Everything up-to-date" in str(errormsg):
            print("####ERROR")


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
        if "modified" in str(status):
            print("Somethings modified")
            print(status)
            autoBranch()
            os.system("git add *")
            os.system("git commit -m %s" % "auto-master%20pushed%20-%20please%20merge")
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
