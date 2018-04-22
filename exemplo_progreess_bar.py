#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      luiscar
#
# Created:     01/03/2018
# Copyright:   (c) luiscar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


""" For determinate mode you do not want to call start. Instead, simply configure the value of the widget or call the step method.

If you know in advance how many bytes you are going to download (and I assume you
 do since you're using determinate mode), the simplest thing to do is set the maxvalue option to the number
 you are going to read. Then, each time you read a chunk you configure the value to be the total number of bytes read.
 The progress bar will then figure out the percentage.

Here's a simulation to give you a rough idea: """

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="start", command=self.start)
        self.button.pack()
        #self.progress = ttk.Progressbar(self, orient="horizontal",
        #                                length=200, mode="determinate")
        self.progress = ttk.Progressbar(self,length=200)
        self.progress.config(orient="vertical",mode="determinate")
        self.progress2 = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="indeterminate")
        self.progress.pack()
        self.progress2.pack()

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        self.progress.config(orient="horizontal",mode="determinate")
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()
        self.progress2.start(50)

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 5000
        self.progress["value"] = self.bytes
        #self.progress2["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(1000, self.read_bytes)
            #showinfo(title="teste",message="Teste: %d" % self.bytes)
if __name__ == '__main__':
    s = SampleApp()

    s.mainloop()
