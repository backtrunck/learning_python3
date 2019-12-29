from tkinter import * 
def quit():
    print("Hello I'm must going...")
    import sys;sys.exit()

widget = Button(None, text='Hello event world', command = quit)
widget.pack()
widget.mainloop()
