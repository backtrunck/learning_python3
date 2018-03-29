from tkinter import *
from tkinter import messagebox



class Quitter(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        widget = Button(self,text='Quit',command=self.quit)
        widget.pack(side=LEFT)
    def quit(self):
        ans = messagebox.askokcancel('Verify exit','Really quit?')
        if ans:
            Frame.quit(self)

if __name__ == '__main__':
    Quitter().mainloop()
