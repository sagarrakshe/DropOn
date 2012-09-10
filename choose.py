from Tkinter import *
import Image,ImageTk

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

def choose():
    global root
    global choices
    del choices[:]
    root=Tk()
    #root.configure(background="white")
    #root.overrideredirect(1)
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    position=str(width/7)+'x'+str(int(height/2.2))+'+'+str((width/3))+'+'+str((height/4))
    root.geometry(position)

    fb_check = Checkbutton(root,command=(lambda: append("Facebook")))
    FB = Image.open('images/facebook-icon.png')
    FB = ImageTk.PhotoImage(FB)

    tr_check = Checkbutton(root,command=(lambda: append("twitter")))
    TR = Image.open('images/twitter-icon.png')
    TR = ImageTk.PhotoImage(TR)

    gm_check = Checkbutton(root,command=(lambda: append("gmail")))
    GM = Image.open('images/gmail-icon.png')
    GM = ImageTk.PhotoImage(GM)

    yt_check = Checkbutton(root,command=(lambda: append("youtube")))
    YT = Image.open('images/youtube-icon.png')
    YT = ImageTk.PhotoImage(YT)
    
    Label(root, image=FB).grid(row=1,column=1, padx=20, pady=20)
    fb_check.grid(row=1,column=2, pady=20, padx=0)
    Label(root, text="POST").grid(row=1, column=3, padx=10)
    
    Label(root, image=TR).grid(row=2,column=1, padx=20, pady=20)
    tr_check.grid(row=2,column=2, pady=20)
    Label(root, text="TWEET").grid(row=2, column=3, padx=10)
    
    Label(root, image=GM).grid(row=3,column=1, padx=20, pady=20)
    gm_check.grid(row=3,column=2, pady=20)
    Label(root, text="MAIL").grid(row=3, column=3, padx=10)
    
    Label(root, image=YT).grid(row=4,column=1, padx=20, pady=20)
    yt_check.grid(row=4,column=2, pady=20)
    Label(root, text="VIDEO").grid(row=4, column=3, padx=10)

    Button(root, text="OK", command=display).grid(row=5, column=2)
    root.mainloop()

    return choices
