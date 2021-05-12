from tkinter import *

root = Tk()

class App:
    def __init__(self):
        root.title("SPS")
        root.geometry("1920x1080")
        self.beginB = Button(root, text="Begin", command=self.begin,bg="green", height=10, width=30)
        self.beginB.grid(sticky = W)
    def begin(self):
        root.title("main window")
        self.beginB.destroy()
        del self.beginB
        self.goB = Button(root, text='Go on', command=self.go_on,
                                bg='red')
        self.goB.grid(sticky=E)
    def go_on(self):
        self.label = Label(root, text="you have continued")
        self.label.grid(row=1, sticky=S)

App()
root.mainloop()