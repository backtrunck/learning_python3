import sys
from tkinter import * 
root = Tk()
root.configure(background='black')
win1 = Toplevel( )
win2 = Toplevel( )
# two independent windows
# but part of same process
Button(win1, text='Spam', command=sys.exit).pack( )
Button(win2, text='SPAM', command=sys.exit).pack( )
Label(root,text='Popups').pack()
root.mainloop( )
