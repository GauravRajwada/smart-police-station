# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:48:20 2020

@author: Gaurav
"""

from tkinter import *


class GUI(Tk):
    def __init__(self,title,heading):
        super().__init__()
        self.geometry("700x700")
        self.maxsize(700,700)
        self.minsize(700,700)
        self.title(title)
        self.wm_iconbitmap("E:/Python Project/Smart Police Station/GUI/title (1).ico")
        title_label = Label(text =heading, fg="Black", font="Airblack 15 bold", borderwidth=1, relief=FLAT).place(x=250,y=0)
        start_frame=Frame(self,bg='white',borderwidth=1,relief=FLAT).place()
        b1=Button(start_frame,fg='red',text='Start',command=self.command).place(x=290,y=670)
        b2=Button(start_frame,fg='red',text='stop',command=self.destroy).place(x=340,y=670)



    def command(self):
        Label(text=" ", fg="Black", font="Airblack 8 bold", borderwidth=1, relief=FLAT).pack()
        Label(text="Welcome", fg="Black", font="Airblack 8", borderwidth=1, relief=FLAT).pack()

if __name__ == '__main__':
    window = GUI(title='SMS',heading='Smart Poice Station')
    # window.status()
    # window.createbutton(" me")
    window.mainloop()

