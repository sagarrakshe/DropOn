# Notifier example from tutorial
#
# See: http://github.com/seb-m/pyinotify/wiki/Tutorial
#
import pyinotify
import urllib2
from notify import *
from Tkinter import *
import Image,ImageTk
import choose
import os

wm = pyinotify.WatchManager() # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE # watched events

Images=['.jpg','.gif','.jpeg','.png']
Videos=['.flv','.mp4','.mkv']
choices=list()

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.113.99',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def distinguish(filePath):
    File=open(filePath,"r")
    content=File.read()
    if "@" in content and ".com" in content:
        #print 'This is an email id'
        #print 'email will be sent to this id via ur gmail'
        return "emailid"
    elif "youtube" in content:
        return "youtube"
    elif any(ext in filePath for ext in Images):
        return "image"
    else:
        return "regular"

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        global choices
        #print "Creating:", event.pathname
        if event.pathname.split("/")[0]=='.':
            print "Hidden file: %s" ,event.pathname
        else:
            #notify(event.pathname.split("/").pop())
            print distinguish(event.pathname)
            print choose.choose()
            os.remove(event.pathnam)
        #print internet_on()
        
    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname
        
    def process_IN_MODIFY(self, event):
        print "Modfying:", event.pathname
        
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/sagar/SocialFS', mask, rec=True)
notifier.loop()
