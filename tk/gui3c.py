from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()
    def quit(self):
        print('hello class method world')
        import sys; sys.exit()

HelloClass()
mainloop()
