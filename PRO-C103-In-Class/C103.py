import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir ="C:/Users/Thomas/Downloads"
to_dir = "C:/Users/Thomas/Downloadedfiles"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,exention = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            time.sleep(1)
            if exention in value: 
                filename = os.path.basename(event.src_path)
                path1 = from_dir + '/' + filename
                path2 = to_dir + '/' + key 
                path3 = to_dir + '/' + key + '/' + filename
                if os.path.exists(path2):
                    print('Folder exists.')
                    print('The file is being moved.')
                    shutil.move(path1,path3)  
                    time.sleep(1)
                else: 
                    print('Folder is getting created.')         
                    os.makedirs(path2) 
                    print('The file is being moved.')    
                    shutil.move(path1,path3)
                    time.sleep(1)
        # print(event)
        # print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('The program has stopped.')
    observer.stop()
    