from tkinter import *

class HelloCallable:
    def __init__(self):
       self.msg = 'Hello __class__ world'
    def __call__(self):
       print(self.msg)
       import sys; sys.exit()

widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()
