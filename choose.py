from Tkinter import *
import Image, ImageTk

choices=list()
global root
def append(string):
    global choices
    if string in choices:
        choices.remove(string)
    else:
        choices.append(string)

def display():
    global choices
    global root
    root.destroy()
    return choices

def facebook():
    fb = Tk()
    fb.mainloop()
    return

def twitter():
    print "Twitter"
    return

def gmail():
    print "Gmail"
    return

def youtube():
    print "Youtube"
    return 

def choose(app):
    global root
    global choices
    del choices[:]
    #print app
    fb_state='normal'
    tr_state='normal'
    gm_state='normal'
    yt_state='normal'
    
    root=Tk()
    root.overrideredirect(1)
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    position=str(width/7)+'x'+str(int(height/2.2))+'+'+str(int(width/2.5))+'+'+str((height/3))
    root.geometry(position)

    fb_check = Checkbutton(root,command=(lambda: append("facebook")), state=fb_state)
    FB = Image.open('images/facebook-icon.png')
    FB = ImageTk.PhotoImage(FB)

    tr_check = Checkbutton(root,command=(lambda: append("twitter")), state=tr_state)
    TR = Image.open('images/twitter-icon.png')
    TR = ImageTk.PhotoImage(TR)

    gm_check = Checkbutton(root,command=(lambda: append("gmail")), state=gm_state)
    GM = Image.open('images/gmail-icon.png')
    GM = ImageTk.PhotoImage(GM)

    yt_check = Checkbutton(root,command=(lambda: append("youtube")), state=yt_state)
    YT = Image.open('images/youtube-icon.png')
    YT = ImageTk.PhotoImage(YT)
    
    fb_btn=Button(root, image=FB, width=30, height=30, relief=FLAT, command=facebook)
    fb_btn.grid(row=1,column=1, padx=20, pady=20)
    fb_check.grid(row=1,column=2, pady=20, padx=0)
    Label(root, text="POST").grid(row=1, column=3, padx=10)
    
    tr_btn=Button(root, image=TR, width=30, height=30, relief=FLAT, command=twitter)
    tr_btn.grid(row=2,column=1, padx=20, pady=20)
    tr_check.grid(row=2,column=2, pady=20)
    Label(root, text="TWEET").grid(row=2, column=3, padx=10)
    
    gm_btn=Button(root, image=GM, width=30, height=30, relief=FLAT, command=gmail)
    gm_btn.grid(row=3,column=1, padx=20, pady=20)
    gm_check.grid(row=3,column=2, pady=20)
    Label(root, text="MAIL").grid(row=3, column=3, padx=10)
    
    yt_btn=Button(root, image=YT, width=30, height=30, relief=FLAT, command=youtube)
    yt_btn.grid(row=4,column=1, padx=20, pady=20)
    yt_check.grid(row=4,column=2, pady=20)
    Label(root, text="VIDEO").grid(row=4, column=3, padx=10)

    Button(root, text="OK", command=display, relief=FLAT).grid(row=5, column=2)
    root.mainloop()

    return choices

#def check(filetype, filepath):
    
