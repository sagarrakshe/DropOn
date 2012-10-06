#! /usr/bin/python

from notify import *
from Tkinter import *
import pyinotify
import urllib2
import choose
import social
import os

wm = pyinotify.WatchManager() # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE # watched events

Images=['.jpg','.gif','.jpeg','.png']
Videos=['.flv','.mp4','.mkv']
choices=list()

def distinguish(filePath):
    File=open(filePath,"r")
    content=File.read()
    filePath=filePath.split('/').pop()
    #print filePath
    if content.find('@')>=0 and content.find('.com')>=0:
        #print 'This is an email id'
        #print 'email will be sent to this id via ur gmail'
        return "emailid"
    elif content.find('youtube')>=0:
        return "youtube"
    elif any(ext in filePath for ext in Images):
        return "image"
    elif any(ext in filePath for ext in Videos):
        return "video"
    elif filePath.count('.pdf'):
        print "This is a pdf file and being removed"
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
            filetype=distinguish(event.pathname)
            social.update(choose.choose(filetype), filetype, event.pathname)
            os.remove(event.pathname)
        #print internet_on()
        
    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname
        
    def process_IN_MODIFY(self, event):
        print "Modfying:", event.pathname
        
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/home/sagar/SocialFS', mask, rec=True)
notifier.loop()
