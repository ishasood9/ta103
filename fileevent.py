import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Event Handler Class
class FileMovementHandler(FileSystemEventHandler):
    event_handler=FileMovementHandler()
    #code to handle new file creation event in a directory
        #initialze event handler
   


from_dir="C:\Users\Lenovo\Desktop"
#Event handler class
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)


#Initialze Event HAndler class
event_handler=FileMovementHandler()

#Initialze observer
observer=Observer()

#Schedule the observer
observer.schedule(event_handler,from_dir,recursive=True)

#Start the observer
observer.start()

while True:
    time.sleep(2)
    print("running.....")
