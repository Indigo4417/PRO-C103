import time
import os , shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ="C:/Users/Thomas/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
    
    def on_deleted(self,event):
        print('The file has been deleted')
        
    def on_modified(self, event):
        print('The file has been modified')
        
    def on_move(self,event):
        print('The file has been moved')


event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler , from_dir ,recursive=True)
observer.start()

while True:
    time.sleep(2)
    print("Running....")
