# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:30:10 2020

@author: Gaurav
"""


from tkinter import *
from PIL import Image, ImageTk
import databse as db
from GUI import English as en

def command(text):

    T.insert(END,text)


def screen():
    command(db.fir(5))

root=Tk()
root.wm_iconbitmap("E:/Python Project/Smart Police Station/GUI/title (1).ico")
root.geometry("700x700")
root.maxsize(700,700)
root.minsize(700,700)
root.title('Smart Police Station')
#title_label = Label(text ="Smart Police Station",bg="white", fg="Black", font="Airblack 15 bold", borderwidth=1, relief=FLAT).place(x=250,y=0)


T = Text(root, height = 35, width = 50)
l = Label(root, text = "Smart Police Station")
l.config(font =("Airblack 15 bold"))
l.pack()

T.pack()
#T.insert(END, "Fact")

T.insert(END,"Gaurav")


"""For button"""
start_frame=Frame(root,bg='steelblue',borderwidth=1,relief=FLAT).place()
b1=Button(start_frame,fg='black',bg="white",text='Start',command=en.main()).place(x=290,y=670)
b2=Button(start_frame,fg='black',bg="white",text='stop',command=root.destroy).place(x=340,y=670)



root.mainloop()