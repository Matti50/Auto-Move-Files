#!/usr/bin/python

import sys
import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ORIGIN = sys.argv[1]
DESTINY = sys.argv[2]

class Watcher:

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler,ORIGIN,recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == "created" or event.event_type == "modified":
           files = os.listdir(ORIGIN)
           for f in files:
               os.system("mv " + ORIGIN + "/" + f + " " + DESTINY)


        
if __name__ == "__main__":
    w = Watcher()
    w.run()
    
        
