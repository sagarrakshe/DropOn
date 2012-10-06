#!/usr/bin/env python
try:
    import gtk, pygtk, os, os.path, pynotify
    pygtk.require('2.0')
except:
    print "Error: need python-notify, python-gtk2 and gtk"

def notify(fileName):
    if not pynotify.init("Timekpr notification"):
        sys.exit(1)

    n = pynotify.Notification("File is created", fileName)
    #n = pynotify.Notification("Moo title", "test", "file:///path/to/icon.png")
    n.set_urgency(pynotify.URGENCY_CRITICAL)
    n.set_timeout(1000) # 10 seconds
    n.set_category("device")

    #Call an icon
    helper = gtk.Button()
    icon = helper.render_icon(gtk.STOCK_DIALOG_WARNING, gtk.ICON_SIZE_DIALOG)
    n.set_icon_from_pixbuf(icon)

    if not n.show():
        print "Failed to send notification"
        sys.exit(1)
